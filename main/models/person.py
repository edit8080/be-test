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
      'ethnicity_concept_id': self.ethnicity_source_value,
    }

  @classmethod
  def get_all_person(cls):
    return [person.json() for person in cls.query.all()]
