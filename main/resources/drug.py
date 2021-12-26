from app import app
from flask import request
from models.drug import DrugModel
from common.helpers.pagination import page_request_args

## 2. concept 검색
@app.route('/drug/concept', methods=['GET'])
def drugConcept():
  page_args = page_request_args()

  return DrugModel.get_drug_concept(page_args['page'], page_args['per_page'])

## 3. column 검색

@app.route('/drug', methods=['GET'])
def drug():
  name = request.args.get('name')
  page_args = page_request_args()

  if name:
    return DrugModel.find_drug_by_name(name, page_args['page'], page_args['per_page'])

  else:
    return DrugModel.get_drug_exposure(page_args['page'], page_args['per_page'])

@app.route('/drug/<string:drug_id>', methods=['GET'])
def drugById(drug_id):
  return DrugModel.find_drug_by_id(drug_id)
