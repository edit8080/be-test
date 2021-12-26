from app import db
from sqlalchemy import func
from models.concept import ConceptModel
from common.cls.pagination import Pagination

class DrugModel(db.Model):
  __tablename__ = 'drug_exposure'
  drug_exposure_id = db.Column(db.BigInteger, primary_key=True)
  drug_exposure_start_datetime = db.Column(db.DateTime)
  drug_exposure_end_datetime = db.Column(db.DateTime)

  drug_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  concept = db.relationship('ConceptModel')

  person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
  person = db.relationship('PersonModel')

  visit_occurrence_id = db.Column(db.BigInteger, db.ForeignKey('visit_occurrence.visit_occurrence_id'))
  visit = db.relationship('VisitModel')

  def json(self):
    return {
      'drug_exposure_id': self.drug_exposure_id,
      'drug_exposure_name': self.concept.json()['concept_name'],      
      'drug_exposure_start_datetime': self.drug_exposure_start_datetime,
      'drug_exposure_end_datetime': self.drug_exposure_end_datetime,
      'person_id': self.person_id,
      'visit_occurrence_id': self.visit_occurrence_id
    }

  @classmethod
  def get_drug_concept(cls, page=None, per_page=None):
    concept = {}

    # drug concept
    drug_concept_query = db.session.query(DrugModel).join(ConceptModel)

    drug_concept = Pagination(page, per_page).set_pagination(drug_concept_query)
    concept['drug_exposure'] = list(set([drug.json()['drug_exposure_name'] for drug in drug_concept['items']]))

    return { 'concepts': concept }

  @classmethod
  def get_drug_exposure(cls, page, per_page):
    drug_sql = db.session.query(DrugModel).join(ConceptModel)

    drugs = Pagination(page, per_page).set_pagination(drug_sql)
    return { 'drugs': [drug.json() for drug in drugs['items']], 'page': drugs['page'], 'total': drugs['total'] } 

  @classmethod
  def find_drug_by_id(cls, id):
    drug = cls.query.filter(cls.drug_exposure_id == id).first()

    return { 'drug': drug.json() }

  @classmethod
  def find_drug_by_name(cls, name, page, per_page):
    drug_sql = db.session.query(DrugModel).join(ConceptModel)\
      .filter(ConceptModel.concept_name.ilike("%"+name+"%"))

    drugs = Pagination(page, per_page).set_pagination(drug_sql)
    return { 'drugs': [drug.json() for drug in drugs['items']], 'page': drugs['page'], 'total': drugs['total'] } 
