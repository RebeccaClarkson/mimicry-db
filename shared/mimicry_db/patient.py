from mimicry_db.base import Base
from mimicry_db.base import session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'patients'
    __table_args__ = {'autoload':True}

    subject_id = Column(Integer, primary_key=True)

    admission = relationship("Admission", backref='patient')
    diagnosis = relationship("Diagnosis", backref='patient')
  
    @classmethod
    def get_from_subject_ids(klass, subject_ids):
        if isinstance(subject_ids, int):
            subject_ids = [subject_ids]
        return session.query(klass).filter(klass.subject_id.in_(subject_ids)).all()


    def number_of_admissions(self):
        return len(self.admission)

    def __repr__(self):
        return "<Patient %s: %s %s>" % (self.subject_id, self.gender, self.dob)
