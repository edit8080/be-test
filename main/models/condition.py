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
    condition_serialize = self.concept.json()

    return {
      'concept': {
        'concept_id': self.condition_concept_id,
        'concept_name': condition_serialize['concept_name'],
        'domain_id': condition_serialize['domain_id'],
      },
      'condition_start_datetime': self.condition_start_datetime,
      'condition_end_datetime': self.condition_end_datetime,
      'person_id': self.person_id,
      'visit_occurrence_id': self.visit_occurrence_id
    }

  ### concept 설명

  @classmethod
  def find_condition_concept_by_name(cls, name, page, per_page):
    concepts_sql = db.session.query(ConditionModel).join(ConceptModel)\
      .filter(ConceptModel.concept_name.ilike("%"+name+"%"))

    concepts = Pagination(page, per_page).set_pagination(concepts_sql)
    return { 'concepts': [concept.json() for concept in concepts['items']], 'page': concepts['page'], 'total': concepts['total'] } 

  @classmethod
  def find_condition_concept_by_domain(cls, domain, page, per_page):
    concepts_sql = db.session.query(ConditionModel).join(ConceptModel)\
      .filter(func.lower(ConceptModel.domain_id) == func.lower(domain))
    
    concepts = Pagination(page, per_page).set_pagination(concepts_sql)
    return { 'concepts': [concept.json() for concept in concepts['items']], 'page': concepts['page'], 'total': concepts['total'] } 

  @classmethod
  def find_condition_concept_by_name_and_domain(cls, name, domain, page, per_page):
    concepts_sql = db.session.query(ConditionModel).join(ConceptModel)\
      .filter((ConceptModel.concept_name.ilike("%"+name+"%")) & (func.lower(ConceptModel.domain_id) == func.lower(domain)))

    concepts = Pagination(page, per_page).set_pagination(concepts_sql)
    return { 'concepts': [concept.json() for concept in concepts['items']], 'page': concepts['page'], 'total': concepts['total'] } 
