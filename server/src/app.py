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


class Event_Ticket(db.Model):
    __tablename__ = 'Event_Ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'))
    event = db.relationship('Event', backref='Event_Ticket')

    ticket_id = db.Column(db.Integer, db.ForeignKey('Ticket.id'))
    ticket = db.relationship(
        'Ticket', backref='Event_Ticket')


class Event(db.Model):
    __tablename__ = 'Event'
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

    purchasable_id = db.Column(db.Integer, db.ForeignKey('Purchasable.id'))
    purchasable = db.relationship(
        'Purchasable', backref='Event')


class PurchasableTypes1(enum.Enum):
    individual = 0
    dayPass = 1


class Purchasable(db.Model):
    __tablename__ = 'Purchasable'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Enum(PurchasableTypes1))
    numTickets = db.Column(db.Integer)
    isSoldOut = db.Column(db.Boolean, nullable=False)


class Ticket(db.Model):
    __tablename__ = 'Ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isPurchased = db.Column(db.Boolean)
    createDate = db.Column(db.DateTime, server_default=db.func.now())
    purchaseDate = db.Column(db.DateTime)

    purchasable_id = db.Column(db.Integer, db.ForeignKey('Purchasable.id'))
    purchasable = db.relationship(
        'Purchasable', backref='Ticket')

    ticketClass_id = db.Column(db.Integer, db.ForeignKey('TicketClass.id'))
    ticketClass = db.relationship(
        'TicketClass', backref='Ticket')

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    user = db.relationship('User', backref='Ticket')


class Purchasable_TicketClass(db.Model):
    __tablename__ = 'Purchasable_TicketClass'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    purchasable_id = db.Column(db.Integer, db.ForeignKey('Purchasable.id'))
    purchasable = db.relationship(
        'Purchasable', backref='Purchasable_TicketClass')

    ticketClass_id = db.Column(db.Integer, db.ForeignKey('TicketClass.id'))
    ticketClass = db.relationship(
        'TicketClass', backref='Purchasable_TicketClass')


class TicketClass(db.Model):
    __tablename__ = 'TicketClass'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    price = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)
    emailAddress = db.Column(db.String, nullable=False)
    createDate = db.Column(
        db.DateTime, server_default=db.func.now(), nullable=False)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String)
    birthDate = db.Column(db.Date)
    association = db.Column(db.String)


class FeedbackAnswer(db.Model):
    __tablename__ = 'FeedbackAnswer'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    response = db.Column(db.String)

    feedbackQuestion_id = db.Column(
        db.Integer, db.ForeignKey('FeedbackQuestion.id'), nullable=False)
    feedbackQuestion = db.relationship(
        'FeedbackQuestion', backref='FeedbackAnswer')

    user_id = db.Column(
        db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship(
        'User', backref='FeedbackAnswer')


class FeedbackQuestion(db.Model):
    __tablename__ = 'FeedbackQuestion'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    text = db.Column(db.String, nullable=False)

    purchasable_id = db.Column(
        db.Integer, db.ForeignKey('Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='FeedbackQuestion')


def serialize(obj):
    return {c.key: getattr(obj, c.key)
            for c in db.inspect(obj).mapper.column_attrs}


@app.route('/')
def hello():
    return "Hello World!"


@app.route("/users/", methods=['POST'])
def createUser():
    # print(request.is_json)
    # content = request.get_json()
    # print(content)
    # return 'JSON posted'
    if request.form:
        user = User(name=request.form.get("name"),
                    emailAddress=request.form.get("emailAddress"))
        db.session.add(user)
        db.session.commit()
        users = db.session.query(User)
        return [serialize(user) for user in users][-1]


@app.route("/users/", methods=['GET'])
def getUsers():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON posted'


@app.route("/users/<id>/", methods=['PUT'])
def updateUser():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON posted'


@app.route("/users/<id>/", methods=['DELETE'])
def deleteUser():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON posted'


@app.route("/auth/", methods=['GET'])
def getAuthToken():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'JSON posted'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port='8080', debug=True)
