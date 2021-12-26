from app import db
from sqlalchemy import func
from models.person import PersonModel
from models.concept import ConceptModel
from common.cls.pagination import Pagination

# Visit : Person = 1 : N
class VisitModel(db.Model):
  __tablename__ = "visit_occurrence"
  visit_occurrence_id = db.Column(db.BigInteger, primary_key=True)
  visit_concept_id = db.Column(db.Integer)
  visit_start_datetime = db.Column(db.DateTime)
  visit_end_datetime = db.Column(db.DateTime)

  person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
  person = db.relationship('PersonModel')

  preceding_visit_occurrence_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
  concept = db.relationship('ConceptModel')

  @classmethod
  def check_visit_concept(cls, visit_concept_id):
    visit_concept = {
      9201: 'Inpatient Visit',
      9202: 'Outpatient Visit',
      9203: 'Emergency Room Visit'
    }
    return visit_concept[visit_concept_id]

  def json(self):
    return {
      'visit_occurrence_id': self.visit_occurrence_id,
      'visit_concept': VisitModel.check_visit_concept(self.visit_concept_id),
      'visit_start_datetime': self.visit_start_datetime,
      'visit_end_datetime': self.visit_end_datetime,
      'person': self.person.json(),
      'concept': self.concept.json()
    }

  def tuple_to_json(self):
    return {
      'visit_occurrence_id': self.visit_occurrence_id,
      'visit_concept': VisitModel.check_visit_concept(self.visit_concept_id),
      'visit_start_datetime': self.visit_start_datetime,
      'visit_end_datetime': self.visit_end_datetime,
      'person': self.person.json()
    }

  @classmethod
  def find_visit_by_type(cls, type): # type = 'Inpatient' | 'Outpatient' | 'Emergency'
    visit_type_to_concept_id = {
      'Inpatient': 9201,
      'Outpatient': 9202,
      'Emergency': 9203
    }
    return [ visit.json() for visit in cls.query.filter_by(visit_concept_id=visit_type_to_concept_id[type]).all()]

  @classmethod
  def find_visit_by_gender(cls, gender): # gender = 'M' | 'F'
    return [ visit.json() for visit in db.session.query(VisitModel).join(PersonModel).filter(PersonModel.gender_source_value == gender).all()]

  @classmethod
  def find_visit_by_race(cls, race): # race = 'asian' | 'black' | 'white' | 'native' | 'other'
    return [ visit.json() for visit in db.session.query(VisitModel).join(PersonModel).filter(PersonModel.race_source_value == race).all()]

  @classmethod
  def find_visit_by_ethnicity(cls, ethnicity): # ethnicity = 'hispanic' | 'nonhispanic'
    return [ visit.json() for visit in db.session.query(VisitModel).join(PersonModel).filter(PersonModel.ethnicity_source_value == ethnicity).all()]

  @classmethod
  def convert_find_by_age_json(cls, row):
    return {
      'visit_occurrence_id': row[0],
      'visit_concept': VisitModel.check_visit_concept(row[1]),
      'visit_start_datetime': row[2],
      'visit_end_datetime': row[3],
      'person_id': row[4],
      'birth_datetime': row[5]
    }

  @classmethod
  def find_visit_by_age(cls, age_unit): # age_unit = 10 unit (10, 20, ...)
    statement = 'SELECT visit_occurrence_id, visit_concept_id, visit_start_date, visit_end_date, v.person_id, birth_datetime \
      FROM visit_occurrence AS v JOIN person AS p ON v.person_id = p.person_id\
      WHERE EXTRACT(year FROM AGE(CURRENT_DATE, birth_datetime)) BETWEEN :age_unit_start AND :age_unit_end'

    return [cls.convert_find_by_age_json(visit) for visit in db.session.execute(statement, {'age_unit_start': age_unit, 'age_unit_end': age_unit + 9} ).all()] # SQL execute result -> tuple Array

  ### concept 설명
  
  def concept_serialize(self):
    serialize = self.json()
    return { 'visit_occurrence_id': serialize['visit_occurrence_id'], 'preceding': serialize['concept'] }

  @classmethod
  def find_visit_concept_by_name(cls, name, page, per_page):
    concepts_sql = db.session.query(VisitModel).join(ConceptModel)\
      .filter(ConceptModel.concept_name.ilike("%"+name+"%"))

    concepts = Pagination(page, per_page).set_pagination(concepts_sql)
    return { 'concepts': [concept.concept_serialize() for concept in concepts['items']], 'page': concepts['page'], 'total': concepts['total'] } 

  @classmethod
  def find_visit_concept_by_domain(cls, domain, page, per_page):
    concepts_sql = db.session.query(VisitModel).join(ConceptModel)\
      .filter(func.lower(ConceptModel.domain_id) == func.lower(domain))
    
    concepts = Pagination(page, per_page).set_pagination(concepts_sql)
    return { 'concepts': [concept.concept_serialize() for concept in concepts['items']], 'page': concepts['page'], 'total': concepts['total'] } 

  @classmethod
  def find_visit_concept_by_name_and_domain(cls, name, domain, page, per_page):
    concepts_sql = db.session.query(VisitModel).join(ConceptModel)\
      .filter((ConceptModel.concept_name.ilike("%"+name+"%")) & (func.lower(ConceptModel.domain_id) == func.lower(domain)))
    
    concepts = Pagination(page, per_page).set_pagination(concepts_sql)
    return { 'concepts': [concept.concept_serialize() for concept in concepts['items']], 'page': concepts['page'], 'total': concepts['total'] } 
