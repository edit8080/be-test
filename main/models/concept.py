from app import db

class ConceptModel(db.Model):
  __tablename__ = 'concept'
  concept_id = db.Column(db.Integer, primary_key=True)
  concept_name = db.Column(db.String(255))
  domain_id = db.Column(db.String(20))

  def json(self):
    return {
      'concept_id': self.concept_id,
      'concept_name': self.concept_name,
      'domain_id': self.domain_id
    }
