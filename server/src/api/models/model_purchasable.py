#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Purchasable(db.Model):
    __tablename__ = 'purchasable'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(20),nullable=False)
    numTickets = db.Column(db.Integer)
    isSoldOut = db.Column(db.Boolean,nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    ticketClass_id = db.Column(db.Integer, db.ForeignKey('ticketClass.id'))
    feedbackQuestion_id = db.Column(db.Integer, db.ForeignKey('feedbackQuestion.id'))

    def __init__(self, id, type, numTickets, isSoldOut, event_id=None, ticket_id=None, ticketClass_id=None, feedbackQuestion_id=None):
        self.id = id
        self.type = type
        self.numTickets = numTickets
        self.isSoldOut = isSoldOut
        self.event_id = event_id
        self.ticket_id = ticket_id
        self.ticketClass_id = ticketClass_id
        self.feedbackQuestion_id = feedbackQuestion_id
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class PurchasableSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Purchasable
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    type = fields.String(required=True)
    numTickets = fields.Integer(required=True)
    isSoldOut = fields.Boolean(required=True)
    event_id = fields.Integer()
    ticket_id = fields.Integer()
    ticketClass_id = fields.Integer()
    feedbackQuestion_id = fields.Integer()