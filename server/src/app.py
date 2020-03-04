from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import enum
import bcrypt
import json

app = Flask(__name__)

app.config['DEBUG'] = True
# TODO: Put this in a env variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rqkxpfbo:Rpk8w646Zf5pIide1L9KP-_p4ElwNFsw@rajje.db.elephantsql.com:5432/rqkxpfbo'

app.config['JWT_SECRET_KEY'] = 'super-secret'  # TODO: Change this
jwt = JWTManager(app)

SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Event_Ticket(db.Model):
    __tablename__ = 'Event_Ticket'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    event_id = db.Column(db.Integer, db.ForeignKey('Event.id'), nullable=False)
    event = db.relationship('Event', backref='Event_Ticket')

    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'Ticket.id'), nullable=False)
    ticket = db.relationship(
        'Ticket', backref='Event_Ticket')


class Event(db.Model):
    __tablename__ = 'Event'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    artistName = db.Column(db.String)
    imageUrl = db.Column(db.String)
    embedMedia = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String)
    capacity = db.Column(db.Integer)
    isFull = db.Column(db.Boolean, nullable=False, default=False)

    purchasable_id = db.Column(db.Integer, db.ForeignKey(
        'Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='Event')


class PurchasableTypes2(enum.Enum):
    individual = 0
    dayPass = 1


class Purchasable(db.Model):
    __tablename__ = 'Purchasable'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    type = db.Column(db.Enum(PurchasableTypes2), nullable=False)
    numTickets = db.Column(db.Integer, nullable=False)
    isSoldOut = db.Column(db.Boolean, nullable=False, default=False)


class Ticket(db.Model):
    __tablename__ = 'Ticket'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    isPurchased = db.Column(db.Boolean, nullable=False, default=False)
    createDate = db.Column(
        db.DateTime, server_default=db.func.now(), nullable=False)
    purchaseDate = db.Column(db.DateTime)

    purchasable_id = db.Column(db.Integer, db.ForeignKey(
        'Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='Ticket')

    ticketClass_id = db.Column(db.Integer, db.ForeignKey(
        'TicketClass.id'), nullable=False)
    ticketClass = db.relationship(
        'TicketClass', backref='Ticket')

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('User', backref='Ticket')


class Purchasable_TicketClass(db.Model):
    __tablename__ = 'Purchasable_TicketClass'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    purchasable_id = db.Column(db.Integer, db.ForeignKey(
        'Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='Purchasable_TicketClass')

    ticketClass_id = db.Column(db.Integer, db.ForeignKey(
        'TicketClass.id'), nullable=False)
    ticketClass = db.relationship(
        'TicketClass', backref='Purchasable_TicketClass')


class TicketClass(db.Model):
    __tablename__ = 'TicketClass'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)
    emailAddress = db.Column(db.String, nullable=False, unique=True)
    createDate = db.Column(
        db.DateTime, server_default=db.func.now(), nullable=False)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String)
    birthDate = db.Column(db.Date)
    association = db.Column(db.String)
    password = db.Column(db.String, nullable=False)


class FeedbackAnswer(db.Model):
    __tablename__ = 'FeedbackAnswer'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    response = db.Column(db.String, nullable=False)

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
                   autoincrement=True, nullable=False, unique=True)
    text = db.Column(db.String, nullable=False)

    purchasable_id = db.Column(
        db.Integer, db.ForeignKey('Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='FeedbackQuestion')


def serialize(obj):
    result = {c.key: getattr(obj, c.key)
              for c in db.inspect(obj).mapper.column_attrs}
    result.pop("password", None)  # remove password if exists
    for key in result:  # convert enums to strings
        if isinstance(result[key], enum.Enum):
            result[key] = str(result[key]).split('.')[-1]
    return result


def getHashedPassword(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())


def checkPassword(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


# Create new user
@app.route("/users/", methods=['POST'])
def createUser():
    user = User(
        name=request.json.get("name"),
        emailAddress=request.json.get("emailAddress"),
        password=getHashedPassword(request.json.get("password"))
    )
    db.session.add(user)
    db.session.commit()
    user = db.session.query(User).filter(User.id == user.id).first()
    return serialize(user)


# Get users
@app.route("/users/", methods=['GET'])
@jwt_required
def getUsers():
    if identity['isAdmin']:
        users = db.session.query(User).all()
        return jsonify([serialize(user) for user in users])
    return "Forbidden", 403


# Get one user
@app.route("/users/<id>/", methods=['GET'])
@jwt_required
def getUser(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['id'] == id or identity['isAdmin']:
        user = db.session.query(User).filter(User.id == id).first()
        return serialize(user)
    return "Forbidden", 403


# Update one user
@app.route("/users/<id>/", methods=['PUT'])
@jwt_required
def updateUser(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['id'] == id or identity['isAdmin']:
        user = db.session.query(User).filter(User.id == id).first()
        user.name = request.json.get("name")
        db.session.commit()
        return serialize(user)
    return "Forbidden", 403


# Delete one user
@app.route("/users/<id>/", methods=['DELETE'])
@jwt_required
def deleteUser(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['id'] == id or identity['isAdmin']:
        user = db.session.query(User).filter(User.id == id).delete()
        db.session.commit()
        return "Deleted user {}".format(id)
    return "Forbidden", 403


# Create new event
@app.route("/events/", methods=['POST'])
@jwt_required
def createEvent():
    identity = get_jwt_identity()
    if identity['isAdmin']:
        event = Event(
            artistName=request.json.get("artistName"),
            description=request.json.get("description"),
            startTime=request.json.get("startTime"),
            endTime=request.json.get("endTime"),
            venue=request.json.get("venue"),
            capacity=request.json.get("capacity")
        )
        purchasable = None

        if request.json.get("purchasableId"):  # add to existing purchasable
            event.purchasable_id = request.json.get("purchasableId")

        else:  # create event AND purchasable
            purchasable = Purchasable(
                type=PurchasableTypes2(request.json['type']) if request.json.get(
                    'type') else PurchasableTypes2.individual,
                numTickets=request.json.get("capacity")
            )
            db.session.add(purchasable)
            db.session.flush()
            event.purchasable_id = purchasable.id

        db.session.add(event)
        db.session.commit()
        event = db.session.query(Event).filter(Event.id == event.id).first()
        purchasable = db.session.query(Purchasable).filter(
            Purchasable.id == purchasable.id).first()
        return {'event': serialize(event), 'purchasable': serialize(purchasable)}
    return "Forbidden", 403


# Get events
@app.route("/events/", methods=['GET'])
def getEvents():
    events = db.session.query(Event).all()
    return jsonify([serialize(event) for event in events])


# Get one event
@app.route("/events/<id>/", methods=['GET'])
def getEvent(id):
    event = db.session.query(Event).filter(Event.id == id).first()
    return serialize(event)


# Update one event
@app.route("/events/<id>/", methods=['PUT'])
@jwt_required
def updateEvent(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['isAdmin']:
        event = db.session.query(Event).filter(Event.id == id).first()
        event.artistName = request.json.get("artistName"),
        event.description = request.json.get("description"),
        event.startTime = request.json.get("startTime"),
        event.endTime = request.json.get("endTime"),
        event.venue = request.json.get("venue"),
        event.capacity = request.json.get("capacity")
        db.session.commit()
        return serialize(event)
    return "Forbidden", 403


# Delete one event
@app.route("/events/<id>/", methods=['DELETE'])
@jwt_required
def deleteEvent(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['isAdmin']:
        event = db.session.query(Event).filter(Event.id == id).delete()
        db.session.commit()
        return "Deleted event {}".format(id)
    return "Forbidden", 403


@app.route('/auth/', methods=['POST'])
def authenticate():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    emailAddress = request.json.get('emailAddress', None)
    password = request.json.get('password', None)

    if not emailAddress:
        return jsonify({"msg": "Missing emailAddress parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = db.session.query(User).filter(
        User.emailAddress == emailAddress).first()

    if checkPassword(password, user.password):
        # Identity can be any data that is json serializable
        access_token = create_access_token(
            identity={'emailAddress': emailAddress, 'id': user.id, 'isAdmin': user.isAdmin})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad emailAddress or password"}), 401


if __name__ == '__main__':
    app.run(host="127.0.0.1", port='8080', debug=True)
