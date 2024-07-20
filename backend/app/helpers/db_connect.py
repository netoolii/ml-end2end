from helpers.env_helper import get_db_host, get_db_name, \
                             get_db_user, get_db_password


class DBConnect:
    HOST = get_db_host()
    DATABASE = get_db_name()
    USER = get_db_user()
    PASSWORD = get_db_password()
    PORT = 3306

    @staticmethod
    def get_connection_string():
        connection_str = "mariadb+mariadbconnector://"
        connection_str += f"{DBConnect.USER}:{DBConnect.PASSWORD}@"
        connection_str += f"{DBConnect.HOST}:{DBConnect.PORT}/"
        connection_str += f"{DBConnect.DATABASE}"
        return connection_str
