from app import app
from flask import request
from models.person import PersonModel

@app.route('/person', methods=['GET'])
def person(): # 전체 환자 수
  return { 'count': len(PersonModel.get_all_person()) }  

@app.route('/person/gender/<string:gender>', methods=['GET'])
def personByGender(gender): # 성별 환자 수
  return { 'count': len(PersonModel.find_person_by_gender(gender))}

@app.route('/person/race/<string:race>', methods=['GET'])
def personByRace(race): # 인종별 환자 수
  return { 'count': len(PersonModel.find_person_by_race(race))}

@app.route('/person/ethnicity/<string:ethnicity>', methods=['GET'])
def personByEthnicity(ethnicity): # 민족별 환자 수
  return { 'count': len(PersonModel.find_person_by_ethnicity(ethnicity))}

@app.route('/person/death', methods=['GET'])
def personByDeath(): # 사망 환자 수
   isDead = request.args.get('isDead') # 'True' or 'False'
   return { 'count': len(PersonModel.find_person_by_death(isDead == 'True'))}
