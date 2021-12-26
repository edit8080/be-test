from app import db
from models.death import DeathModel
from common.cls.pagination import Pagination

class PersonModel(db.Model):
  __tablename__ = "person"
  person_id = db.Column(db.BigInteger, primary_key=True)
  gender_source_value = db.Column(db.String(50), db.ForeignKey('concept.concept_id'))
  birth_datetime = db.Column(db.DateTime)
  race_source_value = db.Column(db.String(50), db.ForeignKey('concept.concept_id'))
  ethnicity_source_value = db.Column(db.String(50))
  
  death = db.relationship('DeathModel')

  def json(self):
    return {
      'person_id': self.person_id,
      'gender': self.gender_source_value,
      'birth': self.birth_datetime,
      'race': self.race_source_value,
      'ethnicity': self.ethnicity_source_value,
      'death': False if len(self.death) == 0 else True
    }

  @classmethod
  def get_all_person(cls, page=None, per_page=None):
    person_query = cls.query
    people = Pagination(page,per_page).set_pagination(person_query)

    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 

  @classmethod
  def find_person(cls, person_id):
    person = cls.query.filter_by(person_id=person_id).first()

    return { 'person': person.json() }

  @classmethod
  def find_person_by_gender(cls, gender, page=None, per_page=None):
    person_query = cls.query.filter_by(gender_source_value=gender)
    people = Pagination(page, per_page).set_pagination(person_query)

    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 

  @classmethod
  def find_person_by_race(cls, race, page=None, per_page=None):
    person_query = cls.query.filter_by(race_source_value=race)
    people = Pagination(page, per_page).set_pagination(person_query)

    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 

  @classmethod
  def find_person_by_ethnicity(cls, ethnicity, page=None, per_page=None):
    person_query = cls.query.filter_by(ethnicity_source_value=ethnicity)
    people = Pagination(page, per_page).set_pagination(person_query)

    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 

  @classmethod
  def find_person_by_death(cls, isDead, page, per_page):
    if isDead:
      person_query = db.session.query(PersonModel).join(DeathModel)
    else:
      person_query = db.session.query(PersonModel).outerjoin(DeathModel).filter(DeathModel.death_date.is_(None))

    people = Pagination(page, per_page).set_pagination(person_query)
    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 
