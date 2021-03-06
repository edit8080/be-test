from datetime import datetime
from app import db
from sqlalchemy import func
from models.person import PersonModel
from models.concept import ConceptModel
from common.cls.pagination import Pagination

class VisitModel(db.Model):
  __tablename__ = "visit_occurrence"
  visit_occurrence_id = db.Column(db.BigInteger, primary_key=True)
  visit_start_datetime = db.Column(db.DateTime)
  visit_end_datetime = db.Column(db.DateTime)

  person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
  person = db.relationship('PersonModel')

  visit_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  concept = db.relationship('ConceptModel', foreign_keys=visit_concept_id)

  preceding_visit_occurrence_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  preceding_concept = db.relationship('ConceptModel', foreign_keys=preceding_visit_occurrence_id)

  def json(self):
    return {
      'visit_occurrence_id': self.visit_occurrence_id,
      'visit_concept_name': self.concept.concept_name,
      'visit_start_datetime': self.visit_start_datetime,
      'visit_end_datetime': self.visit_end_datetime,
      'person': self.person.json()
    }

  @classmethod
  def find_visit_by_type(cls, type, page=None, per_page=None):
    visit_query = db.session.query(VisitModel)\
      .join((ConceptModel, VisitModel.visit_concept_id == ConceptModel.concept_id))\
      .filter(ConceptModel.concept_name.ilike('%'+type+'%'))

    visits = Pagination(page, per_page).set_pagination(visit_query)

    return { 'visits': [visit.json() for visit in visits['items']], 'page': visits['page'], 'total': visits['total'] } 

  @classmethod
  def find_visit_by_gender(cls, gender, page=None, per_page=None):
    visit_query = db.session.query(VisitModel)\
      .join(PersonModel).join((ConceptModel, PersonModel.gender_concept_id == ConceptModel.concept_id))\
      .filter(func.lower(ConceptModel.concept_name) == func.lower(gender))

    visits = Pagination(page, per_page).set_pagination(visit_query)

    return { 'visits': [visit.json() for visit in visits['items']], 'page': visits['page'], 'total': visits['total'] } 

  @classmethod
  def find_visit_by_race(cls, race, page=None, per_page=None):
    visit_query = db.session.query(VisitModel)\
      .join(PersonModel).join((ConceptModel, PersonModel.race_concept_id == ConceptModel.concept_id))\
      .filter(func.lower(ConceptModel.concept_name) == func.lower(race))

    visits = Pagination(page, per_page).set_pagination(visit_query)

    return { 'visits': [visit.json() for visit in visits['items']], 'page': visits['page'], 'total': visits['total'] } 

  @classmethod
  def find_visit_by_ethnicity(cls, ethnicity, page=None, per_page=None):
    visit_query = db.session.query(VisitModel)\
      .join(PersonModel).join((ConceptModel, PersonModel.ethnicity_concept_id == ConceptModel.concept_id))\
      .filter(func.lower(ConceptModel.concept_name) == func.lower(ethnicity))
    
    visits = Pagination(page, per_page).set_pagination(visit_query)

    return { 'visits': [visit.json() for visit in visits['items']], 'page': visits['page'], 'total': visits['total'] } 

  @classmethod
  def find_visit_by_age(cls, age_unit, page=None, per_page=None): # age_unit = 10 unit (10, 20, ...)
    today = datetime.today()
    age = func.extract('year', func.age(today, PersonModel.birth_datetime))

    visit_query = db.session.query(VisitModel).join(PersonModel).filter((age >= age_unit) & (age <= age_unit+9))
    visits = Pagination(page, per_page).set_pagination(visit_query)

    return { 'visits': [visit.json() for visit in visits['items']], 'page': visits['page'], 'total': visits['total'] } 

  ### concept ??????
  
  @classmethod
  def get_visit_concept(cls, page=None, per_page=None):
    concept = {}
    concept['type'] = VisitModel.get_visit_type_concept(page, per_page)['concepts']['type']

    return { 'concepts': concept }

  @classmethod
  def get_visit_type_concept(cls, page=None, per_page=None):
    concept = {}

    # visit type concept
    visit_type_concept_query = db.session.query(VisitModel)\
      .join((ConceptModel, VisitModel.visit_concept_id == ConceptModel.concept_id))

    visit_concept = Pagination(page, per_page).set_pagination(visit_type_concept_query)
    concept['type'] = list(set([visit.json()['visit_concept_name'] for visit in visit_concept['items']]))

    return { 'concepts': concept }
