from flask import Blueprint


health_check_bp = Blueprint("Heath_Check", __name__)


@health_check_bp.route("/")
def health_check():
    return "", 200, {}
