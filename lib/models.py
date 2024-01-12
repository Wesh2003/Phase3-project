from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///library_database.db')

Base = declarative_base()

class Library(Base):
    '''a table containing all books in the library'''
    __tablename__ = 'librarys'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author = Column(String())
    description = Column(String())
    date_added = Column(DateTime(), default=func.current_date())

    readers = relationship('Reader', backref=backref('library'))
    recommendations = relationship('Recommendations', backref=backref('read'))


    def __repr__(self):
        return f'Library(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'author={self.author}, ' + \
            f'description={self.description}, ' + \
            f'date_added={self.date_added})'


class Reader(Base):
    '''A table containing users of the library'''

    __tablename__ = 'readers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    library_id = Column(Integer(), ForeignKey('librarys.id'))

    recommendations = relationship('Recommendations', backref=backref('reader'))


    def __repr__(self):
        return f'Reader(id={self.id}, ' + \
            f'first_name={self.first_name}, ' + \
            f'last_name={self.last_name}, ' + \
            f'gender={self.gender})'



class Recommendations(Base):
    '''A table containing recommendations to be addeed to the library'''

    __tablename__ = 'recommendations'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    author = Column(String())
    description = Column(String())
    date_added = Column(DateTime(), default=func.current_date())
    reader_id = Column(Integer(), ForeignKey('readers.id'))
    library_id = Column(Integer(), ForeignKey('librarys.id'))


    def __repr__(self):
        return f'Library(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'author={self.author}, ' + \
            f'description={self.description}, ' + \
            f'date_added={self.date_added})'


    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()





