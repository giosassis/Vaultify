
# Vaultify

Vaultify is a password vault developed to help you manage your credentials safely and efficiently. Inspired by solutions like Dashlane, It offers a modern and intuitive interface and focuses on security and privacy. 

---

## Resources

- **Safe Storage**: All passwords are encrypted before being saved on the database to ensure the highest level of security.
- **Modern Interface**: The responsive dashboard is user-friendly and supports both light and dark modes for optimal visibility.
- **Secure Authentication**: User registration and login are supported with encrypted passwords for added protection.
- **Password Management**: Users can easily add, edit, and delete passwords and view all of their passwords in one place.
- **Open-source**: The software is open-source, free of charge, and open to contributions for enhanced flexibility and collaboration.

## Technologies Used

### Frontend
- **React**: A Javascript library used to create user interface.
- **Vite**: A modern, and fast build tool. 
- **Material-UI**: A components library that allows for consistent and responsive design.

### Backend
- **FastAPI**: A Python framework that facilitates rapid API development.
- **SQLAlchemy**: A Python ORM (Object-Relational Mapping) tool that simplifies database management.
- **MySQL**: A relational database management system that ensures secure storage of passwords.

### Infraestrutura
- **Docker**: Containerization of applications and databases
- **Docker Compose**: Container orchestration
- **phpMyAdmin**: Web interface for database management

## How to run the project locally

### Requirements 
- Docker and Docker Compose instaled
- Node.Js and Yarn (frontend)
- Python 3.9+ (backend).

### Step to step to run

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/giosassis/vaultify.git
   cd vaultify

2. **Build MySQL phpMyAdmin and container**:
    ```bash 
    docker-compose ud -d

3. **Configure the backend**:
    ```bash 
    cd backend 
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    uvicorn main:app --reload

4. **Configure the Frontend**:
    ```bash
    yarn 
    yarn dev 

5. **Access the aplication**:
- Frontend: `http://localhost:3000`
- phpMyAdmin: `http://localhost:8080`
- Backend:`http://localhost:8000`


## Structure of the project
```plain
vaultify/
├── backend/              
│   ├── main.py            
│   ├── models/            
│   ├── routes/            
│   └── requirements.txt   
├── frontend/              
│   ├── src/               
│   │   ├── components/    
│   │   ├── pages/         
│   │   ├── App.jsx       
│   │   └── main.jsx      
│   └── package.json      
├── docker-compose.yml     
└── README.md              

```
## How to contribute

Contributions are welcome! Follow the steps below:

- Fork the project.
- Create a branch for your feature (git checkout -b feature/nova-feature).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature/nova-feature).
- Open a pull request.

## License Type

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for more details. 

