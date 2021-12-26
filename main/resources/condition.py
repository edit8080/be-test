from app import app
from flask import request

from models.condition import ConditionModel

@app.route('/condition/concept', methods=['GET'])
def ConditionByConcept():
  name = request.args.get('name')
  domain = request.args.get('domain')

  page = request.args.get('page', type=int)
  per_page = request.args.get('per_page', type=int)

  if name and domain:
    return ConditionModel.find_condition_concept_by_name_and_domain(name, domain, page, per_page)

  elif name:
    return ConditionModel.find_condition_concept_by_name(name, page, per_page)

  elif domain:
    return ConditionModel.find_condition_concept_by_domain(domain, page, per_page)

  else:
    return { 'msg': 'use name or domain query string to search concept' }, 400
