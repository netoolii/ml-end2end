# lib import
from flask import Flask
from werkzeug.exceptions import NotFound
import traceback
# app import
from apis.health_check import hc_bp
from apis.auth import auth_bp
from apis.conversation import conversation_bp
from apis.posts import posts_bp
from apis.users import user_bp
from helpers.db_connect import DBConnect
from database import db


app = Flask(__name__)

app.config['SECRET_KEY'] = "frase_super_complexa_dificil_de_saber_pastel"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DBConnect.get_connection_string()

db.init_app(app)

app.register_blueprint(hc_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(conversation_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(user_bp)


@app.errorhandler(NotFound)
def handle_exception(error):
    return "Not Found", 404


@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.critical(traceback.format_exc())
    return str(traceback.format_exc()), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
