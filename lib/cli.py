import click
from sqlalchemy import create_engine
from models import Library, Reader, Recommendations
from sqlalchemy.orm import sessionmaker
from datetime import date
import time
'''
Put all functions here 
'''


# Add new book to library
# Delete book from library 
# get info of book from library 
# find a book from library 


# Add reader 
# delete reader 
# get reader info 




# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')

# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo(f"Hello {name}!")


# @click.command()
# def hello():
#     click.echo('Makiraaa!')

# @click.group()
# def cli():
#     pass

# @click.command()
# def initdb():
#     click.echo('Initialized the database')

# @click.command()
# def dropdb():
#     click.echo('Dropped the database')

# cli.add_command(initdb)
# cli.add_command(dropdb)

# @click.command()
# @click.option('--name', prompt=True)
# def hello(name):
#     click.echo(f"Hello {name}!")

def starting_the_program():
    print("Starting the program...\n")
    click.echo("Please select an option from the sections below\n")
    click.echo("---------library Section ---------- \n")
    click.echo("1. List all books in library\n")
    click.echo("2. List info of a specific book\n")
    click.echo("3. Add new book to library \n")
    click.echo("4. Update a book's information in library\n")
    click.echo("5. Delete a book from library\n")
    click.echo("---------Reader Section ---------- \n")
    click.echo("6. Add new reader \n")
    click.echo("7. List all readers \n")
    click.echo("8. Update a reader's info\n")
    click.echo("9. Delete a reader \n")
    click.echo("---------Recommendations Section ---------- \n")
    click.echo("10. List all recommended book \n")
    click.echo("11. List info of a recommended book \n")
    click.echo("12. Add a new recommendation\n")
    click.echo("13. Update info of a recommended book \n")
    click.echo("14. Delete a book from recommended list\n")
    option = input("Please write what you want to do:\n")
    if (option == "1"):
        def listing_all_books():
            books = session.query(Library.title, Library.author, Library.description).all()
            click.echo(books)
        listing_all_books()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "2"):
        def list_info_of_specific_book():
            book_name = input("Enter name of book to find:\n")
            book = session.query(Library.title, Library.author, Library.description).filter(Library.title == book_name).first()
            if book:
                click.echo(f"Title: {book.title}\nAuthor: {book.author}\nDescription: {book.description}")
            else:
                click.echo(f"No book with the title '{book.title}' was found.")
        list_info_of_specific_book()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "3"):
        def adding_new_book_to_library():
            name = input("Enter title of the book you want to be added: \n")
            author = input("Enter author of the book you want to be added: \n")
            description = input("Enter descritpion of the book you want to be added: \n")
            book = Library(title = name, author = author, description = description)
            session.add(book)
            session.commit()
        adding_new_book_to_library()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "4"):
        def updating_book_info_in_library():
            name = input("Enter book title of the book you want updated: \n")
            book = session.query(Library).filter(Library.title == name).first()
            if book is None:
                click.echo("No such book.")
                click.echo("-------------------\n")
                click.echo("-------------------\n")
                click.echo("-------Returning to main page------\n")
                click.echo("-------------------\n")
                click.echo("-------------------\n")
                time.sleep(4)
                starting_the_program()
            else:
                new_description = input("Enter a new description of this book:\n").strip()
                book.description = new_description
                session.commit()
                click.echo("The information has been updated.")
        updating_book_info_in_library()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "5"):
        def deleting_a_book_from_the_library():
            name = input("Enter book title of the book you want deleted: \n")
            book = session.query(Library).filter(Library.title==name).first()
            session.delete(book)
            session.commit()
            click.echo("Book deleted from library.")
        deleting_a_book_from_the_library()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "6"):
        def add_new_reader():
            first_name = input("\nPlease enter your first name:\n")
            last_name = input("Now please enter your last name:\n")
            gender = input("Please enter your gender:\n")
            new_reader = Reader(first_name = first_name, last_name = last_name, gender = gender)
            session.add(new_reader)
            session.commit()
            click.echo("New reader added")
        add_new_reader()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "7"):
        def listing_all_readers():
            readers = session.query(Reader).all()
            click.echo(readers)
        listing_all_readers()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "8"):
        def updating_reader_info_in_reader_list():
            name = input("Enter first name of the reader whose information is to be updated:\n")
            reader = session.query(Reader).filter(Reader.first_name == name).first()
            if reader is None:
                click.echo("No such reader exists.")
                click.echo("-------------------\n")
                click.echo("-------------------\n")
                click.echo("-------Returning to main page------\n")
                click.echo("-------------------\n")
                click.echo("-------------------\n")
                time.sleep(4)
                starting_the_program()
            else:
                new_last_name = input("Enter a new last name of the reader:\n").strip()
                reader.last_name = new_last_name
                session.commit()
                click.echo("The information has been updated.")
        updating_reader_info_in_reader_list()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "9"):
        def deleting_a_reader():
            name = input("Enter first name of the reader to be deleted:\n")
            reader = session.query(Reader).filter(Reader.first_name == name).first()
            session.delete(reader)
            session.commit()
            click.echo("Reader has been deleted.")
        deleting_a_reader()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "10"):
        def listing_all_recommendations():
            recommendations = session.query(Recommendations.title, Recommendations.author, Recommendations.description).all()
            click.echo(recommendations)
        listing_all_recommendations()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "11"):
        def list_info_of_a_recommendation():
            book_name = input("Enter the title of the recommended book to be found:\n")
            recom_book = session.query(Recommendations.title, Recommendations.author, Recommendations.description).filter(Recommendations.title == book_name).first()
            if recom_book:
                click.echo(f"Title: {recom_book.title}\nAuthor: {recom_book.author}\nDescription: {recom_book.description}")
            else:
                click.echo(f"No book with the title '{recom_book.title}' was found.")
        list_info_of_a_recommendation()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "12"):
        def adding_new_recom_book_to_recommended_list():
            name = input("Enter the title of the recommended book to be added:\n")
            author = input("Enter the author of the recommended book to be added:\n")
            description = input("Enter the description of the recommended book to be added:\n")
            recom_book = Recommendations(title = name, author = author, description = description)
            session.add(recom_book)
            session.commit()
        adding_new_recom_book_to_recommended_list()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "13"):
        def updating_book_info_in_recommended_list():
            name = input("Enter the title of the recommended book to be updated:\n")
            book = session.query(Recommendations).filter(Recommendations.title == name).first()
            if book is None:
                click.echo("No such book.")
                click.echo("-------------------\n")
                click.echo("-------------------\n")
                click.echo("-------Returning to main page------\n")
                click.echo("-------------------\n")
                click.echo("-------------------\n")
                time.sleep(4)
                starting_the_program()
            else:
                new_description = input("Enter a new description of this book:\n").strip()
                book.description = new_description
                session.commit()
                click.echo("The information has been updated in recommendations.")
        updating_book_info_in_recommended_list()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    elif(option == "14"):
        def deleting_a_book_from_the_recommended_list():
            name = input("Enter the title of the recommended book to be deleted:\n")
            book = session.query(Recommendations).filter(Recommendations.title==name).first()
            session.delete(book)
            session.commit()
            click.echo("Book deleted from recommendations.")
        deleting_a_book_from_the_recommended_list()
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        click.echo("-------Returning to main page------\n")
        click.echo("-------------------\n")
        click.echo("-------------------\n")
        time.sleep(4)
        starting_the_program()
    else:
        click.echo("Please enter a valid option.\n")
        starting_the_program()



if __name__ == '__main__':
    engine = create_engine('sqlite:///library_database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # adding_new_book_to_library("lula", "killo", "a testing bnook")
    # updating_book_info_in_library("Insidious")
    # list_info_of_specific_book("insidious")
    # deleting_a_book_from_the_library("Insidious")
    # add_new_reader()
    #listing_all_users()
    # updating_reader_info_in_reader_list()

    starting_the_program()
    
    
    
    


