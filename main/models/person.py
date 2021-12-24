from app import db
from models.death import DeathModel

class PersonModel(db.Model):
  __tablename__ = "person"
  person_id = db.Column(db.BigInteger, primary_key=True)
  gender_source_value = db.Column(db.String(50), db.ForeignKey('concept.concept_id'))
  birth_datetime = db.Column(db.DateTime)
  race_source_value = db.Column(db.String(50), db.ForeignKey('concept.concept_id'))
  ethnicity_source_value = db.Column(db.String(50))
  
  death_date = db.relationship('DeathModel')

  def json(self):
    return {
      'person_id': self.person_id,
      'gender': self.gender_source_value,
      'birth': self.birth_datetime,
      'race': self.race_source_value,
      'ethnicity': self.ethnicity_source_value,
      'death_date': self.death_date[0].json()['death_date'] if len(self.death_date) > 0 else None
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

  @classmethod
  def find_person_by_death(cls, death):
    if death == 'T':
      return [person.json() for person in db.session.query(PersonModel).join(DeathModel).all()]
    elif death == 'F':
      return [person.json() for person in db.session.query(PersonModel).outerjoin(DeathModel).filter(DeathModel.death_date.is_(None)).all()]
