from app import app
from flask import request
from models.drug import DrugModel

@app.route('/drug/concept', methods=['GET'])
def DrugByConcept():
  name = request.args.get('name')
  domain = request.args.get('domain')

  if name and domain:
    return { 'concept': DrugModel.find_drug_concept_by_name_and_domain(name, domain) }

  elif name:
    return { 'concept': DrugModel.find_drug_concept_by_name(name) }

  elif domain:
    return { 'concept': DrugModel.find_drug_concept_by_domain(domain) }

  else:
    return { 'msg': 'use name or domain query string to search concept' }, 400