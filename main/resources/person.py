from flask_restful import Resource
from app import app

@app.route('/person', methods=['GET'])
def person(): # 전체 환자 수
  pass

@app.route('/person/gender/<string:gender>', methods=['GET'])
def personByGender(gender): # 성별 환자 수
  pass

@app.route('/person/race/<string:race>', methods=['GET'])
def personByRace(race): # 인종별 환자 수
  pass

@app.route('/person/ethnicity/<string:ethnicity>', methods=['GET'])
def personByGender(ethnicity): # 민족별 환자 수
  pass

@app.route('/person/death/<string:death>', methods=['GET'])
def personByGender(death): # 사망 환자 수
  pass
