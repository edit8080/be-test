from app import app
from flask import request
from common.helpers.pagination import page_request_args
from models.person import PersonModel

### 1. 환자 수

@app.route('/stat/person', methods=['GET'])
def personStat(): # 전체 환자 수
  return { 'count': PersonModel.get_all_person()['total'] }  

@app.route('/stat/person/gender/<string:gender>', methods=['GET'])
def personStatByGender(gender): # 성별 환자 수
  return { 'count': PersonModel.find_person_by_gender(gender)['total'] }

@app.route('/stat/person/race/<string:race>', methods=['GET'])
def personStatByRace(race): # 인종별 환자 수
  return { 'count': PersonModel.find_person_by_race(race)['total'] }

@app.route('/stat/person/ethnicity/<string:ethnicity>', methods=['GET'])
def personStatByEthnicity(ethnicity): # 민족별 환자 수
  return { 'count': PersonModel.find_person_by_ethnicity(ethnicity)['total'] }

@app.route('/stat/person/death', methods=['GET'])
def personStatByDeath(): # 사망 환자 수
   isDead = request.args.get('isDead') # 'True' or 'False'
   return { 'count': PersonModel.find_person_by_death(isDead == 'True')['total'] }

### 2. concept 검색

@app.route('/person/concept', methods=['GET'])
def personConcept(): # 전체 concept 검색
  page_args = page_request_args()
  return PersonModel.get_person_concept(page_args['page'], page_args['per_page'])

@app.route('/person/concept/gender', methods=['GET'])
def personGenderConcept(): # 성별 concept 검색
  page_args = page_request_args()
  return PersonModel.get_person_gender_concept(page_args['page'], page_args['per_page'])

@app.route('/person/concept/race', methods=['GET'])
def personRaceConcept(): # 인종 concept 검색 
  page_args = page_request_args()
  return PersonModel.get_person_race_concept(page_args['page'], page_args['per_page'])

@app.route('/person/concept/ethnicity', methods=['GET'])
def personEthnicityConcept(): # 민족 concept 검색
  page_args = page_request_args()
  return PersonModel.get_person_ethnicity_concept(page_args['page'], page_args['per_page'])

### 3. 환자 검색

@app.route('/person', methods=['GET'])
def person(): # 전체 환자 검색
  page_args = page_request_args()
  return PersonModel.get_all_person(page_args['page'], page_args['per_page'])

@app.route('/person/<string:person_id>', methods=['GET'])
def personById(person_id): # 환자ID 검색
  return PersonModel.find_person_by_id(person_id)

@app.route('/person/gender/<string:gender>', methods=['GET'])
def personByGender(gender): # 성별 환자 검색
  page_args = page_request_args()
  return PersonModel.find_person_by_gender(gender, page_args['page'], page_args['per_page'])

@app.route('/person/race/<string:race>', methods=['GET'])
def personByRace(race): # 인종별 환자 검색
  page_args = page_request_args()
  return PersonModel.find_person_by_race(race, page_args['page'], page_args['per_page'])

@app.route('/person/ethnicity/<string:ethnicity>', methods=['GET'])
def personByEthnicity(ethnicity): # 민족별 환자 검색
  page_args = page_request_args()
  return PersonModel.find_person_by_ethnicity(ethnicity, page_args['page'], page_args['per_page'])

@app.route('/person/death', methods=['GET'])
def personByDeath(): # 사망별 환자 검색
   isDead = request.args.get('isDead', type=str)

   if isDead == None:
     return { 'msg': 'Please call this api with "isDead" query string '}

   page_args = page_request_args()
   return PersonModel.find_person_by_death(isDead.lower() == 'True'.lower(), page_args['page'], page_args['per_page'])
