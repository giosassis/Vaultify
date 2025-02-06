from sqlalchemy.orm import Session
from models.vault import Vault
from app.schemas import VaultCreate, VaultUpdate
from app.utils import gen_vault_id
from app.core.security import hash_password
from datetime import datetime
from typing import List, Optional

def get_current_utc_time():
    return datetime.utcnow()

class VaultRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[Vault]:
        return self.db.query(Vault).all()
    
    def get_by_id(self, vault_id: str) -> Optional[Vault]:
        return self.db.query(Vault).filter(Vault.id == vault_id).first()
    
    def create(self, vault_data: VaultCreate) -> Vault:
        new_vault = Vault(
            id=gen_vault_id(), 
            application_title=vault_data.application_title,
            email=vault_data.email,
            encrypted_password=hash_password(vault_data.password)  
        )

        self.db.add(new_vault)
        self.db.commit()
        self.db.refresh(new_vault)
        return new_vault

    def update(self, vault_id: str, updated_data: VaultUpdate) -> Optional[Vault]:
        vault = self.get_by_id(vault_id)
        if vault:
            for key, value in updated_data.dict(exclude_unset=True).items():
                setattr(vault, key, value)
            self.db.commit()
            self.db.refresh(vault)
        return vault

    def delete(self, vault: Vault) -> None:
        self.db.delete(vault)
        self.db.commit()
