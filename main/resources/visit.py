from app import app
from flask import request
from models.visit import VisitModel
from common.helpers.pagination import page_request_args

### 1. 방문 수

@app.route('/stat/visit/type/<string:type>', methods=['GET'])
def visitStatByType(type): # 유형별 방문 수
  return { 'count': VisitModel.find_visit_by_type(type)['total'] }

@app.route('/stat/visit/gender/<string:gender>', methods=['GET'])
def visitStatByGender(gender): # 성별 방문 수
  return { 'count': VisitModel.find_visit_by_gender(gender)['total'] }

@app.route('/stat/visit/race/<string:race>', methods=['GET'])
def visitStatByRace(race): # 인종별 방문 수
  return { 'count': VisitModel.find_visit_by_race(race)['total'] }

@app.route('/stat/visit/ethnicity/<string:ethnicity>', methods=['GET'])
def visitStatByEthnicity(ethnicity): # 민족별 방문 수
  return { 'count': VisitModel.find_visit_by_ethnicity(ethnicity)['total'] }

@app.route('/stat/visit/age/<int:age_unit>', methods=['GET'])
def visitStatByAge(age_unit): # 연령대(10세 단위)별 방문 수
  if age_unit < 0:
    return { 'msg': 'The age must be positive'}, 400

  if not(age_unit % 10 == 0):
    return { 'msg': 'The age must be in units of 10'}, 400

  return { 'count': VisitModel.find_visit_by_age(age_unit)['total'] }

### 3. 방문 검색

@app.route('/visit/type/<string:type>', methods=['GET'])
def visitByType(type): # 유형별 방문 검색
  page_args = page_request_args()
  return VisitModel.find_visit_by_type(type, page_args['page'], page_args['per_page'])

@app.route('/visit/gender/<string:gender>', methods=['GET'])
def visitByGender(gender): # 성별 방문 검색
  page_args = page_request_args()
  return VisitModel.find_visit_by_gender(gender, page_args['page'], page_args['per_page'])

@app.route('/visit/race/<string:race>', methods=['GET'])
def visitByRace(race): # 인종별 방문 검색
  page_args = page_request_args()
  return VisitModel.find_visit_by_race(race, page_args['page'], page_args['per_page'])

@app.route('/visit/ethnicity/<string:ethnicity>', methods=['GET'])
def visitByEthnicity(ethnicity): # 민족별 방문 검색
  page_args = page_request_args()
  return VisitModel.find_visit_by_ethnicity(ethnicity, page_args['page'], page_args['per_page'])

@app.route('/visit/age/<int:age_unit>', methods=['GET'])
def visitByAge(age_unit): # 방문시 연령대(10세 단위)별 방문 수
  if age_unit < 0:
    return { 'msg': 'The age must be positive'}, 400

  if not(age_unit % 10 == 0):
    return { 'msg': 'The age must be in units of 10'}, 400

  page_args = page_request_args()
  return VisitModel.find_visit_by_age(age_unit, page_args['page'], page_args['per_page'])

@app.route('/visit/concept', methods=['GET'])
def VisitByConcept():
  name = request.args.get('name')
  domain = request.args.get('domain')

  page = request.args.get('page', type=int)
  per_page = request.args.get('per_page', type=int)

  if name and domain:
    return VisitModel.find_visit_concept_by_name_and_domain(name, domain, page, per_page)

  elif name:
    return VisitModel.find_visit_concept_by_name(name, page, per_page)

  elif domain:
    return VisitModel.find_visit_concept_by_domain(domain, page, per_page)

  else:
    return { 'msg': 'use name or domain query string to search concept' }, 400
