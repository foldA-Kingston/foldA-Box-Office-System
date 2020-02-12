#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.model_event import EventSchema
from api.models.model_ticket import TicketSchema
from api.models.model_ticketClass import TicketClassSchema
from api.models.model_feedbackQuestion import FeedbackQuestionSchema

class Purchasable(db.Model):
    __tablename__ = 'purchasable'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(20),nullable=False)
    numTickets = db.Column(db.Integer)
    isSoldOut = db.Column(db.Boolean,nullable=False)
    event.id = db.Column(db.Integer, db.ForeignKey('event.id'))
    ticket.id = db.Column(db.Integer, db.ForeignKey('ticket.id')
    ticketClass.id = db.Column(db.Integer, db.ForeignKey('ticketClass.id'))
    feedbackQuestion.id = db.Column(db.Integer, db.ForeignKey('feedbackQuestion.id'))

    def __init__(self, id, type, numTickets, isSoldOut, events=[], tickets=[], ticketClass=[], feedbackQuestions=[]):
        self.id = id
        self.type = type
        self.numTickets = numTickets
        self.isSoldOut = isSoldOut
        self.events = events
        self.tickets = tickets
        self.ticketClass = ticketClass
        self.feedbackQuestions = feedbackQuestions
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
    events = fields.Nested(EventSchema, many=True)
    tickets = fields.Nested(TicketSchema, many=True)
    ticketClass = fields.Nested(TicketClassSchema, many=True)
    feedbackQuestions = fields.Nested(FeedbackQuestionSchema, many=True)
