from models.users import Users
from flask import current_app


class AuthHandler:

    def auth_login(username: str, password: str):
        try:
            return Users.query.filter(Users.username == username,
                                      Users.password == password).one()
        except Exception as e:
            current_app.logger.critical(str(e), exc_info=True)
            return None
