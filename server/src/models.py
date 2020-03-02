# from app import db


# class event(db.Model):
#     __tablename__ = 'event'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     artistName = db.Column(db.String)
#     imageUrl = db.Column(db.String)
#     embedMedia = db.Column(db.String)
#     description = db.Column(db.String)
#     startTime = db.Column(db.Date)
#     endTime = db.Column(db.Date)
#     venue = db.Column(db.String)
#     capacity = db.Column(db.Integer)
#     isFull = db.Column(db.Boolean)
#     purchasable = db.relationship('Purchasable', backref='Event')
#     # tickets = db.relationship('TicketClass', backref='Event')


# class purchasable(db.Model):
#     __tablename__ = 'purchasable'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     type = db.Column(db.String(20), nullable=False)
#     numTickets = db.Column(db.Integer)
#     isSoldOut = db.Column(db.Boolean, nullable=False)
#     events = db.relationship('Event', backref='Purchasable')
#     tickets = db.relationship('Ticket', backref='Purchasable')
#     ticketClass = db.relationship('TicketClass', backref='Purchasable')
#     # feedbackQuestions = db.relationship(
#     #     'FeedbackQuestion', backref='Purchasable')


# class ticket(db.Model):
#     __tablename__ = 'ticket'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isPurchased = db.Column(db.Boolean)
#     surname = db.Column(db.String)
#     createDate = db.Column(db.DateTime, server_default=db.func.now())
#     purchaseDate = db.Column(db.DateTime)

#     event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
#     purchasable_id = db.Column(db.Integer, db.ForeignKey('purchasables.id'))
#     # ticketClass_id = db.Column(db.Integer, db.ForeignKey(
#     #     'ticketClasses.id'))  # TODO: How are we pluralizing?
#     userId_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# class user(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     isAdmin = db.Column(db.Boolean)
#     emailAddress = db.Column(db.String)
#     createDate = db.Column(db.Date)
#     name = db.Column(db.String)
#     birthDate = db.Column(db.Date)
#     association = db.Column(db.String)
#     # feedbackAnswers = db.relationship('feedbackAnswer', backref='User')
#     # tickets = db.relationship('feedbackAnswer', backref='User')
