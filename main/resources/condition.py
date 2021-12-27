from app import app
from flask import request
from models.condition import ConditionModel
from common.helpers.pagination import page_request_args

## 2. concept 검색

@app.route('/condition/concept', methods=['GET'])
def conditionConcept():
  page_args = page_request_args()

  return ConditionModel.get_condition_concept(page_args['page'], page_args['per_page'])

## 3. column 검색

@app.route('/condition', methods=['GET'])
def condition():
  name = request.args.get('name')
  page_args = page_request_args()

  if name:
    return ConditionModel.find_condition_by_name(name, page_args['page'], page_args['per_page'])

  else:
    return ConditionModel.get_condition_occurrence(page_args['page'], page_args['per_page'])

@app.route('/condition/<string:condition_id>', methods=['GET'])
def conditionById(condition_id):
  return ConditionModel.find_condition_by_id(condition_id)