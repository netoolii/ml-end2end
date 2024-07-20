from flask import Blueprint


hc_bp = Blueprint("Health Check", __name__)


@hc_bp.route("/")
def health_check():
    return "", 200, {}
