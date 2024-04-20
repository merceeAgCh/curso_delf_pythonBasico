class User:
    def __init__(self, nickname, password, email):
        self.nickname = nickname
        self.email = email
        self.password = password

    def get_nickname(self) -> str:
        return self.nickname
    def get_email(self) -> str:
        return self.email
    def get_password(self) -> str:
        return self.password
    def set_nickname(self, new_nickname:str) -> bool:

        """
        Toma un nurvo nombre de usuario y modifica el actual.
        Regresa un TRUE si se realizó el cambio, FALSE si no.
        """
        self.nickname = new_nickname
        return True
    def set_email(self, new_email:str) -> bool:
        """
        Toma un nuevo correo y modifica el actual.
        Regresa un TRUE si se realizó el cambio, FALSE si no.
        """
        self.email = new_email
        return True
    