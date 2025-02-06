class UserNotFoundException(Exception):

    def __init__(self, user_id: str):
        self.message = f"User with id {user_id} not found"
        super().__init__(self.message)


class UserAlreadyExistsException(Exception):
    def __init__(self, email: str):
        self.message = f"User with email {email} already exists"
        super().__init__(self.message)
