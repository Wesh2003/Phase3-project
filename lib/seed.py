
from faker import Faker
import random, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Library, Reader, Recommendations

if __name__ == '__main__':
    engine = create_engine('sqlite:///library_database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Library).delete()
    session.query(Recommendations).delete()
    session.query(Reader).delete()

    fake = Faker()

    botw = Library(title = 'Harry Potter', author = 'J.K.Rowling', description = 'a wizard book')
    session.add(botw)
    session.commit()

    book_names = ['Spy kids', 'Nimona', 'Monkey King',
        'Extraction', 'Insidious', 'Murder Mystery']
    
    # -----------------------------------------------------
    books = []
    for i in range(10):
        book = Library(
            title=random.choice(book_names),
            author=fake.unique.name(),
            description=fake.sentence(),
            date_added= datetime.datetime.now()   
        )

        # add and commit individually to get IDs back
        session.add(book)
        session.commit()
        books.append(book)


    # -----------------------------------------------------
    genderss = ['male', 'female']
    readers = []
    for i in range(10):
        reader = Reader(
            first_name=fake.unique.name(),
            last_name=fake.unique.name(),
            gender = random.choice(genderss),
            library_id= random.randint(min(book.id for book in books), max(book.id for book in books))
        )

        session.add(reader)
        session.commit()
        readers.append(reader)
    

    # ------------------------------------------------------
    recommendationss = []
    recom_names = ['Spy kids', 'Nimona', 'Monkey King',
        'Extraction', 'Insidious', 'Murder Mystery', 'Rick and Morty']
    for i in range(10):
        recommendation = Recommendations(
            title=random.choice(recom_names),
            author=fake.unique.name(),
            description = random.choice(genderss),
            date_added= datetime.datetime.now(),
            reader_id= random.randint(min(reader.id for reader in readers), max(reader.id for reader in readers)),
            library_id = random.randint(min(book.id for book in books), max(book.id for book in books))
        )

        session.add(recommendation)
        session.commit()
        recommendationss.append(recommendation)
    