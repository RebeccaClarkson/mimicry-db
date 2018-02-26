from mimicry_db.base import Base
from mimicry_db.base import session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

class DiagnosisDescription(Base):
    __tablename__ = 'd_icd_diagnoses'
    __table_args__ = {'autoload':True}
    
    row_id = Column(Integer, primary_key=True)
    icd9_code = Column(String, primary_key=True)

    diagnoses = relationship("Diagnosis", backref='description')
    patients = relationship("Patient", secondary='diagnoses_icd')
    admissions = relationship("Admission", secondary='diagnoses_icd')

    @classmethod
    def find_diagnosed_diagnosis_descriptions(klass, limit=None):
        return session.query(klass).filter(klass.diagnoses != None).limit(limit).all()

    @classmethod
    def get_by_icd9(klass, icd9_code):
        return session.query(klass).filter(klass.icd9_code==icd9_code).first()

    @classmethod
    def find_by_icd9(klass, icd9_code_pattern):
        return session.query(klass).filter(klass.icd9_code.like(icd9_code_pattern)).all()

    @classmethod
    def find_by_long_title(klass, pattern):
        return session.query(klass).filter(klass.long_title.like(pattern)).all()

    def __repr__(self):
        return "<ICD9 %s:  %s>" % (self.icd9_code, self.long_title)
