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
    event.id = db.Column(db.Integer, db.ForeignKey('event.id'))
    ticket.id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    ticketClass.id = db.Column(db.Integer, db.ForeignKey('ticketClass.id'))
    feedbackQuestion.id = db.Column(db.Integer, db.ForeignKey('feedbackQuestion.id'))

    def __init__(self, id, type, numTickets, isSoldOut, event.id=None, ticket.id=None, ticketClass.id=None, feedbackQuestion.id=None):
        self.id = id
        self.type = type
        self.numTickets = numTickets
        self.isSoldOut = isSoldOut
        self.event.id = event.id
        self.ticket.id = ticket.id
        self.ticketClass.id = ticketClass.id
        self.feedbackQuestion.id = feedbackQuestion.id
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
    event.id = fields.Integer()
    ticket.id = fields.Integer()
    ticketClass.id = fields.Integer()
    feedbackQuestion.id = fields.Integer()
