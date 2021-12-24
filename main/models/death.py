from app import db

class DeathModel(db.Model):
  __tablename__ = "death"
  death_date = db.Column(db.DateTime)

  person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'), primary_key=True)

  def json(self):
    return {
      'death_date': self.death_date
    }
