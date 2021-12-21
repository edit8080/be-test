from app import db

class PersonModel(db.Model):
  __tablename__ = "de.person"
  person_id = db.Column(db.BigInteger, primary_key=True)
  gender_concept_id = db.Column(db.Integer, db.ForeignKey('de.concept.concept_id'))
  birth_datetime = db.Column(db.datetime)
  race_concept_id = db.Column(db.Integer, db.ForeignKey('de.concept.concept_id'))
  ethnicity_concept_id = db.Column(db.Integer)
