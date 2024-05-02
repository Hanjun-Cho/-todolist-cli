from validation import DateValidation
from testData import testData
from flask import current_app, Blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/get_tasks/<date>", methods=['GET'])
def get_tasks(date):
    DateValidation(date).validate_date()
    return testData[date]

@api.route("/add_task/<date>", methods=['POST'])
def add_task(date):
    DateValidation(date).validate_date()
    form = request.form
    print(form)
    return get_tasks(date) 
