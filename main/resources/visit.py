from app import app
from flask import request
from models.visit import VisitModel

@app.route('/visit/type/<string:type>', methods=['GET'])
def visitByType(type): # 방문 유형별 방문 수
  return { 'count': len(VisitModel.find_visit_by_type(type)) }

@app.route('/visit/gender/<string:gender>', methods=['GET'])
def visitByGender(gender): # 성별 방문 수
  return { 'count': len(VisitModel.find_visit_by_gender(gender)) }

@app.route('/visit/race/<string:race>', methods=['GET'])
def visitByRace(race): # 인종별 방문 수
  return { 'count': len(VisitModel.find_visit_by_race(race)) }

@app.route('/visit/ethnicity/<string:ethnicity>', methods=['GET'])
def visitByEthnicity(ethnicity): # 민족별 방문 수
  return { 'count': len(VisitModel.find_visit_by_ethnicity(ethnicity)) }

@app.route('/visit/age/<int:age_unit>', methods=['GET'])
def visitByAge(age_unit): # 방문시 연령대(10세 단위)별 방문 수
  if age_unit < 0:
    return { 'msg': 'The age must be positive'}, 400

  if not(age_unit % 10 == 0):
    return { 'msg': 'The age must be in units of 10'}, 400

  return { 'count': len(VisitModel.find_visit_by_age(age_unit)) }

@app.route('/visit/concept', methods=['GET'])
def VisitByConcept():
  name = request.args.get('name')
  domain = request.args.get('domain')

  if name and domain:
    return { 'concept': VisitModel.find_visit_concept_by_name_and_domain(name, domain) }

  elif name:
    return { 'concept': VisitModel.find_visit_concept_by_name(name) }

  elif domain:
    return { 'concept': VisitModel.find_visit_concept_by_domain(domain) }

  else:
    return { 'msg': 'use name or domain query string to search concept' }, 400
