from flask_restful import Resource

class Person(Resource):
  def get(self): # 전체 환자 수
    pass

class PersonByGender(Resource):
  def get(self, gender): # 성별 환자 수
    pass

class PersonByRace(Resource):
  def get(self, race): # 인종별 환자 수
    pass

class PersonByEthnicity(Resource):
  def get(self, ethnicity): # 민족별 환자 수
    pass

class PersonByDeath(Resource):
  def get(self, death): # 사망 환자 수
    pass

def load_person(api):  
  api.add_resource(Person, '/person')
  api.add_resource(PersonByGender, '/person/gender/<string:gender>')
  api.add_resource(PersonByRace, '/person/race/<string:race>')
  api.add_resource(PersonByEthnicity, '/person/ethnicity/<string:gender>')
  api.add_resource(PersonByDeath, '/person/death/<string:death>')
