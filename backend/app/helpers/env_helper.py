import os


def get_db_host():
    return os.environ.get("DB_HOST", "mariadb")


def get_db_name():
    return os.environ.get("DB_NAME", "workshop")


def get_db_user():
    return os.environ.get("DB_USER", "admin")


def get_db_password():
    return os.environ.get("DB_PASSWORD", "password")
