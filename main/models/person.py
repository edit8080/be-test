from sqlalchemy.sql.functions import func
from app import db
from models.concept import ConceptModel
from models.death import DeathModel
from common.cls.pagination import Pagination

class PersonModel(db.Model):
  __tablename__ = "person"
  person_id = db.Column(db.BigInteger, primary_key=True)
  birth_datetime = db.Column(db.DateTime)

  gender_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  gender_concept = db.relationship('ConceptModel', foreign_keys=gender_concept_id)

  race_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  race_concept = db.relationship('ConceptModel', foreign_keys=race_concept_id)

  ethnicity_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  ethnicity_concept = db.relationship('ConceptModel', foreign_keys=ethnicity_concept_id)

  death = db.relationship('DeathModel')

  def json(self):
    return {
      'person_id': self.person_id,
      'gender': self.gender_concept.concept_name,
      'birth': self.birth_datetime,
      'race': self.race_concept.concept_name,
      'ethnicity': self.ethnicity_concept.concept_name,
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
    person_query = db.session.query(PersonModel)\
      .join((ConceptModel, PersonModel.gender_concept_id == ConceptModel.concept_id))\
      .filter(func.lower(ConceptModel.concept_name) == func.lower(gender))

    people = Pagination(page, per_page).set_pagination(person_query)

    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 

  @classmethod
  def find_person_by_race(cls, race, page=None, per_page=None):
    person_query = db.session.query(PersonModel)\
      .join((ConceptModel, PersonModel.race_concept_id == ConceptModel.concept_id))\
      .filter(func.lower(ConceptModel.concept_name) == func.lower(race))
    people = Pagination(page, per_page).set_pagination(person_query)

    return { 'person': [person.json() for person in people['items']], 'page': people['page'], 'total': people['total'] } 

  @classmethod
  def find_person_by_ethnicity(cls, ethnicity, page=None, per_page=None):
    person_query = db.session.query(PersonModel)\
      .join((ConceptModel, PersonModel.ethnicity_concept_id == ConceptModel.concept_id))\
      .filter(func.lower(ConceptModel.concept_name) == func.lower(ethnicity))
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

  @classmethod
  def get_person_concept(cls, page=None, per_page=None):
    concept = {}

    concept['gender'] = PersonModel.get_person_gender_concept(page, per_page)['concepts']['gender']
    concept['race'] = PersonModel.get_person_race_concept(page, per_page)['concepts']['race']
    concept['ethnicity'] = PersonModel.get_person_ethnicity_concept(page, per_page)['concepts']['ethnicity']

    return { 'concepts': concept }

  @classmethod
  def get_person_gender_concept(cls, page=None, per_page=None):
    concept = {}

    # gender concept
    people_concept_query = db.session.query(PersonModel)\
      .join((ConceptModel, PersonModel.gender_concept_id == ConceptModel.concept_id))

    people_concept = Pagination(page, per_page).set_pagination(people_concept_query)
    concept['gender'] = list(set([person.json()['gender'] for person in people_concept['items']]))

    return { 'concepts': concept }

  @classmethod
  def get_person_race_concept(cls, page=None, per_page=None):
    concept = {}

    # race concept
    people_concept_query = db.session.query(PersonModel)\
      .join((ConceptModel, PersonModel.race_concept_id == ConceptModel.concept_id))

    people_concept = Pagination(page, per_page).set_pagination(people_concept_query)
    concept['race'] = list(set([person.json()['race'] for person in people_concept['items']]))

    return { 'concepts': concept }

  @classmethod
  def get_person_ethnicity_concept(cls, page=None, per_page=None):
    concept = {}

    # ethnicity concept
    people_concept_query = db.session.query(PersonModel)\
      .join((ConceptModel, PersonModel.ethnicity_concept_id == ConceptModel.concept_id))

    people_concept = Pagination(page, per_page).set_pagination(people_concept_query)
    concept['ethnicity'] = list(set([person.json()['ethnicity'] for person in people_concept['items']]))

    return { 'concepts': concept }
