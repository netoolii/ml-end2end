from flask import Flask
from apis.health_check import health_check_bp
from apis.classifier_v1 import classifier_v1_bp
import traceback
from werkzeug.exceptions import NotFound


app = Flask(__name__)
app.register_blueprint(health_check_bp)
app.register_blueprint(classifier_v1_bp)


@app.errorhandler(NotFound)
def handle_exception(error):
    return "Not Found", 404


@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.critical(traceback.format_exc())
    return str(traceback.format_exc()), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
