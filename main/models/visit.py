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
    visit_concept = {
      9201: 'Inpatient Visit',
      9202: 'Outpatient Visit',
      9203: 'Emergency Room Visit'
    }
    return visit_concept[visit_concept_id]

  def json(self):
    return {
      'visit_concept': VisitModel.check_visit_concept(self.visit_concept_id),
      'visit_start_datetime': self.visit_start_datetime,
      'visit_end_datetime': self.visit_end_datetime,
    }

  