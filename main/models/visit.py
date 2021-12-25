from app import db

class VisitModel(db.Model):
  __tablename__ = "visit_occurrence"
  visit_occurrence_id = db.Column(db.BigInteger, primary_key=True)
  visit_concept_id = db.Column(db.BigInteger)
  visit_start_datetime = db.Column(db.Date)
  visit_end_datetime = db.Column(db.Date)

  person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
  person = db.relationship('PersonModel')

  @classmethod
  def check_visit_concept(visit_concept_id):
    if visit_concept_id == 9201:
      return 'Inpatient Visit'
    elif visit_concept_id == 9202:
      return 'Outpatient Visit'
    elif visit_concept_id == 9203:
      return 'Emergency Room Visit'

  def json(self):
    return {
      'visit_concept': VisitModel.check_visit_concept(self.visit_concept_id),
      'visit_start_datetime': self.visit_start_datetime,
      'visit_end_datetime': self.visit_end_datetime,
    }

  