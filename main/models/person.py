from app import db

class PersonModel(db.Model):
  __tablename__ = "person"
  person_id = db.Column(db.BigInteger, primary_key=True)
  gender_source_value = db.Column(db.String(50), db.ForeignKey('concept.concept_id'))
  birth_datetime = db.Column(db.DateTime)
  race_source_value = db.Column(db.String(50), db.ForeignKey('concept.concept_id'))
  ethnicity_source_value = db.Column(db.String(50))

  def json(self):
    return {
      'person_id': self.person_id,
      'gender': self.gender_source_value,
      'birth': self.birth_datetime,
      'race': self.race_source_value,
      'ethnicity': self.ethnicity_source_value,
    }

  @classmethod
  def get_all_person(cls):
    return [person.json() for person in cls.query.all()]

  @classmethod
  def find_person_by_gender(cls, gender):
    return [person.json() for person in cls.query.filter_by(gender_source_value=gender).all()]

  @classmethod
  def find_person_by_race(cls, race):
    return [person.json() for person in cls.query.filter_by(race_source_value=race).all()]

  @classmethod
  def find_person_by_ethnicity(cls, ethnicity):
    return [person.json() for person in cls.query.filter_by(ethnicity_source_value=ethnicity).all()]
