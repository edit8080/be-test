from app import app
from flask import request

from models.condition import ConditionModel

@app.route('/condition/concept', methods=['GET'])
def ConditionByConcept():
  name = request.args.get('name')
  domain = request.args.get('domain')

  if name and domain:
    return { 'concept': ConditionModel.find_condition_concept_by_name_and_domain(name, domain) }

  elif name:
    return { 'concept': ConditionModel.find_condition_concept_by_name(name) }

  elif domain:
    return { 'concept': ConditionModel.find_condition_concept_by_domain(domain) }

  else:
    return { 'msg': 'use name or domain query string to search concept' }, 400
