from app import app
from flask import request

@app.route('/visit/type/<string:type>', methods=['GET'])
def visitByType(type): # 방문 유형별 방문 수
  pass

@app.route('/visit/gender/<string:gender>', methods=['GET'])
def visitByGender(gender): # 성별 방문 수
  pass

@app.route('/visit/race/<string:race>', methods=['GET'])
def visitByRace(race): # 인종별 방문 수
  pass

@app.route('/visit/ethnicity/<string:ethnicity>', methods=['GET'])
def visitByEthnicity(ethnicity): # 민족별 방문 수
  pass

@app.route('/visit/age/<number:age>', methods=['GET'])
def visitByAge(): # 방문시 연령대(10세 단위)별 방문 수
  pass
