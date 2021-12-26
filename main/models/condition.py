from app import db
from sqlalchemy import func
from models.concept import ConceptModel
from common.cls.pagination import Pagination

class ConditionModel(db.Model):
  __tablename__ = 'condition_occurrence'
  condition_occurrence_id = db.Column(db.BigInteger, primary_key=True)
  condition_start_datetime = db.Column(db.DateTime)
  condition_end_datetime = db.Column(db.DateTime)

  condition_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  concept = db.relationship('ConceptModel')

  person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
  person = db.relationship('PersonModel')

  visit_occurrence_id = db.Column(db.BigInteger, db.ForeignKey('visit_occurrence.visit_occurrence_id'))
  visit = db.relationship('VisitModel')

  def json(self):
    return {
      'condition_occurrence_id': self.condition_occurrence_id,
      'condition_concept_name': self.concept.json()['concept_name'],
      'condition_start_datetime': self.condition_start_datetime,
      'condition_end_datetime': self.condition_end_datetime,
      'person_id': self.person_id,
      'visit_occurrence_id': self.visit_occurrence_id
    }

  @classmethod
  def get_condition_concept(cls, page=None, per_page=None):
    concept = {}

    # condition concept
    condition_concept_query = db.session.query(ConditionModel).join(ConceptModel)

    condition_concepts = Pagination(page, per_page).set_pagination(condition_concept_query)
    concept['condition_concept'] = list(set([condition.json()['condition_concept_name'] for condition in condition_concepts['items']]))

    return { 'concepts': concept }

  @classmethod
  def get_condition_occurrence(cls, page, per_page):
    condition_query = db.session.query(ConditionModel).join(ConceptModel)

    conditions = Pagination(page, per_page).set_pagination(condition_query)
    return { 'conditions': [condition.json() for condition in conditions['items']], 'page': conditions['page'], 'total': conditions['total'] } 

  @classmethod
  def find_condition_by_id(cls, id):
    condition = cls.query.filter(cls.condition_occurrence_id == id).first()

    return { 'condition': condition.json() }

  @classmethod
  def find_condition_by_name(cls, name, page, per_page):
    condition_query = db.session.query(ConditionModel).join(ConceptModel)\
      .filter(ConceptModel.concept_name.ilike("%"+name+"%"))

    conditions = Pagination(page, per_page).set_pagination(condition_query)
    return { 'conditions': [condition.json() for condition in conditions['items']], 'page': conditions['page'], 'total': conditions['total'] } 
