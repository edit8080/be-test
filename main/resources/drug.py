from app import app
from flask import request
from models.drug import DrugModel

@app.route('/drug/concept', methods=['GET'])
def DrugByConcept():
  name = request.args.get('name')
  domain = request.args.get('domain')

  page = request.args.get('page', type=int)
  per_page = request.args.get('per_page', type=int)

  if name and domain:
    return DrugModel.find_drug_concept_by_name_and_domain(name, domain, page, per_page)

  elif name:
    return DrugModel.find_drug_concept_by_name(name, page, per_page)

  elif domain:
    return DrugModel.find_drug_concept_by_domain(domain, page, per_page)

  else:
    return { 'msg': 'use name or domain query string to search concept' }, 400
