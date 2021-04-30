# To start creating a minimal application, in addition to importing Flask, we also need 
# to import SQLAlchemy class from the flask_sqlalchemy module:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask app instance:
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' #path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app) #database instance

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just created your first Flask application supporting databases!"


# Book to be a database model for the database instance db, it has to inherit from db.Model in the following way:

# class Book(db.Model):
# As you can see in the code editor, the Book model has 5 attributes of Column class. 
# The types of the column are the first argument to Column. We use the following column types:

# String(N), where N is the maximum number of characters
# Integer, representing a whole number
# Column can take some other parameters:

# unique: when True, the values in the column must be unique
# index: whenTrue, the column is searchable by its values
# primary_key: when True, the column serves as the primary key

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column
    title = db.Column(db.String(80), index = True, unique = True) 
    author_name = db.Column(db.String(50), index = True, unique = False)
    author_surname = db.Column(db.String(80), index = True, unique = False) 
    month = db.Column(db.String(20), index = True, unique = False) 
    year = db.Column(db.Integer, index = True, unique = False) 
    reviews = db.relationship('Review', backref = 'book', lazy = 'dynamic') 
    
    #Get a nice printout for Book objects
    def __repr__(self):
        return "{} in: {},{}".format(self.title, self.month, self.year)

#Declaring the Reader model
class Reader(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True, unique = False)
    surname = db.Column(db.String(80), unique = False, index = True)
    email = db.Column(db.String(120), unique = True, index = True)
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic')
  
    #get a nice printout for Reader objects
    def __repr__(self):
        return "Reader: {}".format(self.email)

#declaring the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key = True) #primary key column, 
    stars = db.Column(db.Integer, unique = False) #a review's rating
    text = db.Column(db.String(200), unique = False) #a review's text
    book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key 
    reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))

    #get a nice printout for Review objects
    def __repr__(self):
        return "Review: {} stars: {}".format(self.text, self.stars)

#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Congrats! You have just initialized your database!"


# We can initialize our database in two ways:

# Using the interactive Python shell.
# In the command-line terminal, navigate to the application folder and enter Python’s interactive mode:
# $ python3
# Import the database instance db from app.py:
# >>> from app import db
# (this assumes the application file is called app.py)
# Create all database tables according to the declared models:
# >>> db.create_all()
# From within the application file. After all the models have been specified the database is 
# initialized by adding db.create_all() to the main program. The command is written after all the defined models.


# Creating database entries: entities
from app import Reader, Book, Review

b1 = Book(id = 123, title = 'Demian', author_name = "Hermann", author_surname = 'Hesse', month = "February", year = 2020)
r1 = Reader(id = 342, name = 'Ann', surname = 'Adams', email = 'ann.adams@example.com')

b2 = Book(id = 533, title = 'The Stranger', author_name = 'Albert', author_surname = 'Camus', month = "April", year = 2019)
r2 = Reader(id = 765, name = 'Sam', surname = 'Adams', email = 'sam.adams@example.com')

print("My first reader:", r1.name)
print("My first author:", b2.author_surname)
print(len(r2.email))

# Creating database entries: relationships
rev1 = Review(id = 435, text = 'This book is amazing...', stars = 5, reviewer_id = r1.id, book_id = b1.id)
print(rev1) #prints the rev1 object
print(rev1.text) #prints the text of the review rev1
print(rev1.book_id) #prints the id of the book for which the review was written

#Checkpoint 1: 
rev2 = Review(id = 450, text = "This book is difficult!", stars = 2, reviewer_id = r2.id, book_id = b2.id)