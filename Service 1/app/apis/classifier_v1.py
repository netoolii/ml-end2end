from flask import Blueprint
from flask_restx import Api, Resource, fields, reqparse
import time


API_VERSION = "v1"

classifier_v1_bp = Blueprint("Emotions_Classifier_v1", __name__)
classifier_v1 = Api(
    classifier_v1_bp,
    version=API_VERSION,
    title="Emotions Classifier",
    description="API that provides emotion classification using text",
)

classifier_resource = classifier_v1.parser()
classifier_resource.add_argument(
    "text", dest="text", required=True, type=str, help="Text to classifier the emotion"
)

classifier_response = classifier_v1.model(
    "ClassifierResponse",
    {
        "categories": fields.List(
            fields.String(
                description="Sentiment Category", skip_none=False, enum=["happy", "sad"]
            )
        ),
        "accuracies": fields.List(
            fields.Float(description="Sentiment Accuracies", skip_none=False)
        ),
    },
)


@classifier_v1.route("/classifier")
@classifier_v1.response(404, "Classifier not found")
class Classifier(Resource):
    @classifier_v1.marshal_with(classifier_response, skip_none=False)
    @classifier_v1.expect(classifier_resource)
    def post(self):
        start_date = time.time()
        args = classifier_resource.parse_args(strict=True)

        end_date = time.time() - start_date
        print(end_date)

        return {
            "categories": [],
            "accuracies": []
        }, 200
