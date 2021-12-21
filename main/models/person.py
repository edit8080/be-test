from app import db

class PersonModel(db.Model):
  __tablename__ = "person"
  person_id = db.Column(db.BigInteger, primary_key=True)
  gender_concept_id = db.Column(db.Integer, db.ForeignKey('de.concept.concept_id'))
  birth_datetime = db.Column(db.DateTime)
  race_concept_id = db.Column(db.Integer, db.ForeignKey('de.concept.concept_id'))
  ethnicity_concept_id = db.Column(db.Integer)

  def json(self):
    return {
      'person_id': self.person_id,
      'gender_concept_id': self.gender_concept_id,
      'birth_datetime': self.birth_datetime,
      'race_concept_id': self.race_concept_id,
      'ethnicity_concept_id': self.ethnicity_concept_id,
    }

  @classmethod
  def get_all_person(cls):
    return [person.json() for person in cls.query.all()]
