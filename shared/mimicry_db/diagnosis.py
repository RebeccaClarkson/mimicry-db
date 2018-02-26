from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from mimicry_db.base import Base
from mimicry_db.base import session

class Diagnosis(Base):
    __tablename__ = 'diagnoses_icd'
    __table_args__ = {'autoload':True}

    row_id = Column(Integer, primary_key=True)
    hadm_id = Column(Integer, ForeignKey('admissions.hadm_id'))
    subject_id = Column(Integer, ForeignKey('patients.subject_id'))
    icd9_code = Column(String, ForeignKey('d_icd_diagnoses.icd9_code'))

    @classmethod
    def summarize_by_icd9_code(klass, icd9_code):
        """ For a given icd9 code, return the number of admissions and patients
        diagnosed with this code """
        
        num_patients = session.query(klass.subject_id).filter(klass.icd9_code==icd9_code).distinct().count()
        num_admissions = session.query(klass.hadm_id).filter(klass.icd9_code==icd9_code).distinct().count()
        
        return num_patients, num_admissions

    def __repr__(self):
        args = (self.icd9_code, self.hadm_id, self.subject_id)
        return "<Diagnosis ICD9 %s from admission %s for patient %s>" % args 
