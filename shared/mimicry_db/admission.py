from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from mimicry_db.base import Base

class Admission(Base):
    __tablename__ = 'admissions'
    __table_args__ = {'autoload':True}

    hadm_id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('patients.subject_id'))

    diagnoses = relationship("Diagnosis", backref='admission')

    def number_of_diagnoses(self):
        return len(self.diagnoses)

    def __repr__(self):
        return "<Admission %s for patient %s @ %s>" % (self.hadm_id, self.subject_id, self.admittime)
