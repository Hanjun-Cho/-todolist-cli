from flask import Blueprint
errors = Blueprint('errors', __name__, url_prefix='/errors')

@errors.route("/get_tasks/<date>", methods=['GET'])
def error_get_tasks(date):
    return {
        "error": "invalid date format",
    }
