from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import enum

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rqkxpfbo:Rpk8w646Zf5pIide1L9KP-_p4ElwNFsw@rajje.db.elephantsql.com:5432/rqkxpfbo'

SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class event_ticket(db.Model):
    __tablename__ = 'event_ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event = db.relationship('event', backref='event_ticket')
    ticket = db.relationship('ticket', backref='event_ticket')


class event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artistName = db.Column(db.String)
    imageUrl = db.Column(db.String)
    embedMedia = db.Column(db.String)
    description = db.Column(db.String)
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    venue = db.Column(db.String)
    capacity = db.Column(db.Integer)
    isFull = db.Column(db.Boolean)

    purchasable = db.relationship('purchasable', backref='event')


class TypeEnum(enum.Enum):
    individual = 0
    dayPass = 1


class purchasable(db.Model):
    __tablename__ = 'purchasable'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(TypeEnum))
    numTickets = db.Column(db.Integer)
    isSoldOut = db.Column(db.Boolean, nullable=False)

    purchasable_ticketClass = db.relationship(
        'purchasable_ticketClass', backref='purchasable')


class ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isPurchased = db.Column(db.Boolean)
    createDate = db.Column(db.DateTime, server_default=db.func.now())
    purchaseDate = db.Column(db.DateTime)

    purchasable = db.relationship('purchasable', backref='ticket')
    ticketClass = db.relationship('ticketClass', backref='ticket')
    user = db.relationship('user', backref='ticket')


class purchasable_ticketClass(db.Model):
    __tablename__ = 'purchasable_ticketClass'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    purchasable = db.relationship(
        'purchasable', backref='purchasable_ticketClass')
    ticketClass = db.relationship(
        'ticketClass', backref='purchasable_ticketClass')


class ticketClass(db.Model):
    __tablename__ = 'ticketClass'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    price = db.Column(db.Integer)


class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isAdmin = db.Column(db.Boolean)
    emailAddress = db.Column(db.String)
    createDate = db.Column(db.DateTime, server_default=db.func.now())
    name = db.Column(db.String)
    gender = db.Column(db.String)
    birthDate = db.Column(db.Date)
    association = db.Column(db.String)


class feedbackAnswer(db.Model):
    __tablename__ = 'feedbackAnswer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    response = db.Column(db.String)
    feedbackQuestion = db.relationship(
        'feedbackQuestion', backref='feedbackAnswer'
    )
    user = db.relationship(
        'user', backref='feedbackAnswer'
    )


class feedbackQuestion(db.Model):
    __tablename__ = 'feedbackQuestion'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    purchasable = db.relationship('purchasable', backref='feedbackQuestion')

# @app.route('/')
# def hello():
#     return "Hello World!"


# @app.route("/readings/", methods=['POST'])
# def readings():
#     print(request.is_json)
#     content = request.get_json()
#     print(content)
#     return 'JSON posted'


# if __name__ == '__main__':
#     app.run(host="127.0.0.1", port='8080', debug=True)
