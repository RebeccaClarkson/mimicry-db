from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

dbname = 'mimicry'; username = 'pguser'; pw = 'pguser'
engine_string = 'postgresql://%s:%s@localhost/%s?client_encoding=utf-8' %(username, pw,  dbname)
engine = create_engine(engine_string, echo=False)

class MimicryBase(object):
    @classmethod
    def get(klass, offset=0):
        return session.query(klass).offset(offset).first()

    @classmethod
    def query_with_subject_ids(klass, query, subject_ids, limit=None):
        if isinstance(subject_ids, int):
            subject_ids = [subject_ids]
        return session.query(klass).filter(and_(query, klass.subject_id.in_(subject_ids))).limit(limit)

Base = declarative_base(engine, cls=MimicryBase)

def load_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

session = load_session()
