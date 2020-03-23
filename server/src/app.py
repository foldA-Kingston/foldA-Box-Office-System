from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlathanor import FlaskBaseModel, initialize_flask_sqlathanor
from flask_migrate import Migrate
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import enum
import bcrypt
from flask_cors import CORS

app = Flask(__name__)

app.config['DEBUG'] = True
# TODO: Put this in a env variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rqkxpfbo:Rpk8w646Zf5pIide1L9KP-_p4ElwNFsw@rajje.db.elephantsql.com:5432/rqkxpfbo'

app.config['JWT_SECRET_KEY'] = 'super-secret'  # TODO: Change this

CORS(app)

jwt = JWTManager(app)

SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app, model_class=FlaskBaseModel)
db = initialize_flask_sqlathanor(db)

migrate = Migrate(app, db)


class Event_Ticket(db.Model):
    __tablename__ = 'Event_Ticket'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    event_id = db.Column(db.Integer, db.ForeignKey(
        'Event.id'), nullable=False)
    event = db.relationship(
        'Event', backref='Event_Ticket', lazy="joined")

    ticket_id = db.Column(db.Integer, db.ForeignKey(
        'Ticket.id'), nullable=False)
    ticket = db.relationship(
        'Ticket', backref='Event_Ticket', lazy="joined")


class Purchasable_TicketClass(db.Model):
    __tablename__ = 'Purchasable_TicketClass'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    purchasable_id = db.Column(db.Integer, db.ForeignKey(
        'Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='Purchasable_TicketClass', lazy="joined")

    ticketClass_id = db.Column(db.Integer, db.ForeignKey(
        'TicketClass.id'), nullable=False)
    ticketClass = db.relationship(
        'TicketClass', backref='Purchasable_TicketClass', lazy="joined")


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
    name = db.Column(db.String, nullable=False)

    purchasable_id = db.Column(db.Integer, db.ForeignKey(
        'Purchasable.id'), nullable=False)
    purchasable = db.relationship(
        'Purchasable', backref='Event', lazy="joined")


class PurchasableTypes2(enum.Enum):
    individual = 0
    dayPass = 1


class Purchasable(db.Model):
    __tablename__ = 'Purchasable'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)

    description = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.Enum(PurchasableTypes2), nullable=False)
    numTickets = db.Column(db.Integer, nullable=False)
    isSoldOut = db.Column(db.Boolean, nullable=False, default=False)

    events = db.relationship(
        'Event', backref='Purchasable', lazy="joined")

    tickets = db.relationship(
        'Ticket', backref='Purchasable', lazy="joined")

    ticketClasses = db.relationship(
        'Purchasable_TicketClass', backref='Purchasable', lazy="joined")


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


class TicketClass(db.Model):
    __tablename__ = 'TicketClass'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    tickets = db.relationship(
        'Ticket', backref='TicketClass')

    purchasables = db.relationship(
        'Purchasable_TicketClass', backref='TicketClass')


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False, unique=True, supports_json=True)
    isAdmin = db.Column(db.Boolean, nullable=False,
                        default=False, supports_json=True)
    emailAddress = db.Column(db.String, nullable=False,
                             unique=True, supports_json=True)
    createDate = db.Column(
        db.DateTime, server_default=db.func.now(), nullable=False, supports_json=True)
    name = db.Column(db.String, nullable=False, supports_json=True)
    gender = db.Column(db.String, supports_json=True)
    birthDate = db.Column(db.Date, supports_json=True)
    association = db.Column(db.String, supports_json=True)
    password = db.Column(db.String, nullable=False)

    feedbackAnswers = db.relationship(
        'FeedbackAnswer', backref='User')

    tickets = db.relationship(
        'Ticket', backref='User')


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

    feedbackAnswers = db.relationship(
        'FeedbackAnswer', backref='FeedbackQuestion')


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
    name = request.json.get("name")
    emailAddress = request.json.get("emailAddress")
    password = request.json.get("password")

    if name and emailAddress and password:
        user = User(
            name=name,
            emailAddress=emailAddress,
            password=getHashedPassword(password)
        )
        db.session.add(user)
        db.session.commit()
        user = db.session.query(User).filter(User.id == user.id).one()
        return serialize(user)
    else:
        return "Bad request", 400


# Get users
@app.route("/users/", methods=['GET'])
@jwt_required
def getUsers():
    identity = get_jwt_identity()
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
        user = db.session.query(User).filter(User.id == id).one()
        return serialize(user)
    return "Forbidden", 403


# Update one user
@app.route("/users/<id>/", methods=['PUT'])
@jwt_required
def updateUser(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['id'] == id or identity['isAdmin']:
        user = db.session.query(User).filter(User.id == id).one()
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
            name=request.json.get("name"),
            startTime=request.json.get("startTime"),
            endTime=request.json.get("endTime"),
            venue=request.json.get("venue"),
            capacity=request.json.get("capacity")
        )
        purchasable = None

        if request.json.get("purchasableId"):  # add to existing purchasable
            event.purchasable_id = request.json.get("purchasableId")
            purchasable = db.session.query(Purchasable).filter(
                Purchasable.id == event.purchasable_id).one()

            # change individual to dayPass
            purchasable.type = PurchasableTypes2.dayPass

        else:  # create event AND purchasable
            purchasable = Purchasable(
                type=PurchasableTypes2(request.json['type']) if request.json.get(
                    'type') else PurchasableTypes2.individual,
                numTickets=request.json.get("capacity"), description=request.json.get("description"), name=request.json.get("name")
            )

            ticketClasses = request.json['ticketClasses']

            db.session.add(purchasable)
            db.session.flush()

            for tc_id in ticketClasses:
                relationship = Purchasable_TicketClass(
                    purchasable_id=purchasable.id, ticketClass_id=tc_id)
                db.session.add(relationship)

            event.purchasable_id = purchasable.id

        db.session.add(event)
        db.session.commit()

        event = db.session.query(Event).filter(Event.id == event.id).one()
        purchasable = db.session.query(Purchasable).filter(
            Purchasable.id == purchasable.id).one()

        tcs = db.session.query(Purchasable_TicketClass).filter(
            Purchasable_TicketClass.purchasable_id == purchasable.id).join(TicketClass, Purchasable_TicketClass.ticketClass_id == TicketClass.id).all()

        return {**serialize(event), "purchasable": {**serialize(purchasable), "ticketClasses": [{"id": tc.ticketClass.id, "description": tc.ticketClass.description, "price": tc.ticketClass.price} for tc in tcs]}}
    return "Forbidden", 403


# Get events
@app.route("/individualEvents/", methods=['GET'])
def getIndividualEvents():
    events = db.session.query(Event, Purchasable).filter(
        Event.purchasable_id == Purchasable.id).filter(Purchasable.type == PurchasableTypes2.individual).all()

    return jsonify([{**serialize(event), "purchasable": serialize(purchasable)} for (event, purchasable) in events])


# Get one event
@app.route("/events/<id>/", methods=['GET'])
def getEvent(id):
    event = db.session.query(Event).filter(Event.id == id).one()

    # add related purchasable to event
    purchasable = db.session.query(Purchasable).filter(
        Purchasable.id == event.purchasable_id).one()

    tcs = db.session.query(Purchasable_TicketClass).filter(Purchasable_TicketClass.purchasable_id == purchasable.id).join(
        TicketClass, Purchasable_TicketClass.ticketClass_id == TicketClass.id).all()

    return {**serialize(event), "purchasable": {**serialize(purchasable), "ticketClasses": [{"id": tc.ticketClass.id, "description": tc.ticketClass.description, "price": tc.ticketClass.price} for tc in tcs]}}


# Update one event
@app.route("/events/<id>/", methods=['PUT'])
@jwt_required
def updateEvent(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['isAdmin']:
        event = db.session.query(Event).filter(Event.id == id).one()
        event.artistName = request.json.get("artistName"),
        event.description = request.json.get("description"),
        event.name = request.json.get("name"),
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


# Create new purchasable
@app.route("/purchasables/", methods=['POST'])
@jwt_required
def createDayPass():
    identity = get_jwt_identity()
    if identity['isAdmin']:
        purchasable = Purchasable(
            type=request.json.get("type"),
            numTickets=request.json.get("numTickets"),
            description=request.json.get("description"),
            name=request.json.get("name")
        )
        db.session.add(purchasable)
        db.session.commit()
        purchasable = db.session.query(Purchasable).filter(
            Purchasable.id == purchasable.id).one()
        return serialize(purchasable)
    return "Forbidden", 403


# Get purchasables
@app.route("/purchasables/", methods=['GET'])
def getPurchasables():
    purchasables = db.session.query(Purchasable).all()

    return jsonify([
        {
            **serialize(p),
            "events": [serialize(e) for e in p.events],
            "startTime":  min([e.startTime for e in p.events]) if len(p.events) else None
        } for p in purchasables])


# Get day passes
@app.route("/dayPasses/", methods=['GET'])
def getDayPasses():
    purchasables = db.session.query(Purchasable).filter(
        Purchasable.type == PurchasableTypes2.dayPass).all()
    return jsonify([{**serialize(p), "events": [serialize(e) for e in p.events]} for p in purchasables])


# Get one purchasable
@app.route("/purchasables/<id>/", methods=['GET'])
def getPurchasable(id):
    purchasable = db.session.query(Purchasable).filter(
        Purchasable.id == id).one()

    tcs = db.session.query(Purchasable_TicketClass).filter(Purchasable_TicketClass.purchasable_id == purchasable.id).join(
        TicketClass, Purchasable_TicketClass.ticketClass_id == TicketClass.id).all()

    return {**serialize(purchasable), "events": [serialize(e) for e in purchasable.events], "ticketClasses": [{"id": tc.ticketClass.id, "description": tc.ticketClass.description, "price": tc.ticketClass.price} for tc in tcs]}


# Update one purchasable
@app.route("/purchasables/<id>/", methods=['PUT'])
@jwt_required
def updatePurchasable(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['isAdmin']:
        purchasable = db.session.query(Purchasable).filter(
            Purchasable.id == id).one()
        purchasable.type = request.json.get("type")
        purchasable.numTickets = request.json.get("numTickets")
        purchasable.description = request.json.get("description")
        purchasable.name = request.json.get("name")
        db.session.commit()
        return serialize(purchasable)
    return "Forbidden", 403


# Delete one purchasable
@app.route("/purchasables/<id>/", methods=['DELETE'])
@jwt_required
def deletePurchasable(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['isAdmin']:
        purchasable = db.session.query(Purchasable).filter(
            Purchasable.id == id).delete()
        db.session.commit()
        return "Deleted purchasable {}".format(id)
    return "Forbidden", 403


# Create new user
@app.route("/ticketClasses/", methods=['POST'])
@jwt_required
def createTicketClass():
    identity = get_jwt_identity()
    if identity['isAdmin']:
        description = request.json.get("description")
        price = request.json.get("price")

        if description and price:
            ticketClass = TicketClass(
                description=description,
                price=price
            )
            db.session.add(ticketClass)
            db.session.commit()
            ticketClass = db.session.query(TicketClass).filter(
                TicketClass.id == ticketClass.id).one()
            return serialize(ticketClass)
        else:
            return "Bad request", 400
    else:
        return "Forbidden", 403


# Get ticketClasses
@app.route("/ticketClasses/", methods=['GET'])
def getTicketClasss():
    ticketClasses = db.session.query(TicketClass).all()
    return jsonify([serialize(ticketClass) for ticketClass in ticketClasses])


# Create ticket for user
@app.route("/users/<id>/cart/", methods=['POST'])
@jwt_required
def addToCart(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['id'] == id or identity['isAdmin']:

        purchasableId = request.json.get("purchasableId")
        ticketClassId = request.json.get("ticketClassId")
        purchasable = db.session.query(Purchasable).filter(
            Purchasable.id == purchasableId).one()
        ticketClasses = db.session.query(Purchasable_TicketClass).filter(Purchasable_TicketClass.purchasable_id == purchasable.id).join(
            TicketClass, Purchasable_TicketClass.ticketClass_id == TicketClass.id).all()

        assert(ticketClassId in [serialize(tc)[
               'ticketClass_id'] for tc in ticketClasses])

        for i in range(request.json.get("quantity")):
            ticket = Ticket(
                isPurchased=False,
                purchasable_id=purchasableId,
                ticketClass_id=ticketClassId,
                user_id=id
            )
            db.session.add(ticket)
            db.session.flush()

            for eventId in request.json.get("events"):
                event = db.session.query(Event).filter(
                    Event.id == eventId).one()
                assert(event.purchasable_id == purchasable.id)
                relationship = Event_Ticket(
                    event_id=eventId,
                    ticket_id=ticket.id
                )
                db.session.add(relationship)
        db.session.commit()
        return "Success", 200
    return "Forbidden", 403


# Get user's tickets (cart)
# @app.route("/users/<id>/cart/", methods=['GET'])
# @jwt_required
# def getCart(id):
#     identity = get_jwt_identity()
#     id = int(id)
#     if identity['id'] == id or identity['isAdmin']:
#         tickets = db.session.query(Ticket).filter(Ticket.user_id == id)\
#             .join(Purchasable, Ticket.purchasable_id == Purchasable.id)\
#             .join(TicketClass, Ticket.ticketClass_id == TicketClass.id)\
#             .join(Event, Event.purchasable_id == Purchasable.id).all()
#         return jsonify([{**serialize(ticket), "purchasable": {**serialize(ticket.purchasable), "events": [serialize(event) for event in ticket.purchasable.events]}, "ticketClass": serialize(ticket.ticketClass)} for ticket in tickets])
#     return "Forbidden", 403

@app.route("/users/<id>/cart/", methods=['GET'])
@jwt_required
def getCart(id):
    identity = get_jwt_identity()
    id = int(id)
    if identity['id'] == id or identity['isAdmin']:
        purchasables = db.session.query(Purchasable).join(
            Ticket, Ticket.purchasable_id == Purchasable.id).join(TicketClass, TicketClass.id == Ticket.ticketClass_id).filter(Ticket.user_id == id)
        return jsonify([{**serialize(purchasable),
                         "events": [serialize(event) for event in purchasable.events],
                         "tickets": [{**serialize(ticket), "ticketClass": serialize(ticket.ticketClass)} for ticket in purchasable.tickets]} for purchasable in purchasables])
    return "Forbidden", 403

# Remove cart item
@app.route("/users/<id>/cart/<ticketId>/", methods=['DELETE'])
@jwt_required
def deleteCartItem(id, ticketId):
    identity = get_jwt_identity()
    id = int(id)
    ticketId = int(ticketId)
    if identity['id'] == id or identity['isAdmin']:
        ticket = db.session.query(Ticket).filter(
            Ticket.id == ticketId, Ticket.user_id == id, Ticket.isPurchased == False).delete()
        db.session.commit()
        return "Deleted ticket {}".format(ticketId)
    return "Forbidden", 403


# Get purchasable's tickets
# ...


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
        User.emailAddress == emailAddress).one()

    if checkPassword(password, user.password):
        # Identity can be any data that is json serializable
        access_token = create_access_token(
            identity={'emailAddress': emailAddress, 'id': user.id, 'isAdmin': user.isAdmin})
        return jsonify(access_token=access_token, emailAddress=emailAddress, userId=user.id, isAdmin=user.isAdmin), 200
    return jsonify({"msg": "Bad emailAddress or password"}), 401


if __name__ == '__main__':
    app.run(host="127.0.0.1", port='8080', debug=True)
