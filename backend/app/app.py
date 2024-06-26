# lib import
from flask import Flask
from werkzeug.exceptions import NotFound
import traceback
# app import
from apis.health_check import hc_bp


app = Flask(__name__)


app.register_blueprint(hc_bp)

@app.errorhandler(NotFound)
def handle_exception(error):
    return "Not Found", 404



@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.critical(traceback.format_exc())
    return str(traceback.format_exc()), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)