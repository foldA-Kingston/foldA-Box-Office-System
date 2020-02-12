#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.model_feedbackAnswer import FeedbackAnswerSchema
from api.models.model_ticket import TicketSchema # this might be wrong

class User (db.Model):
    __tablename__ = 'user'
    #One user has many tickets
    #One User provides many Feed Back answers 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isAdmin = db.Column(db.Boolean) #is this right?
    emailAddress = db.Column(db.String)
    createDate = db.Column(db.Date)
    name = db.Column(db.String)
    birthDate = db.Column(db.Date)
    association =db.Column(db.String)
    feedbackAnswers = db.relationship('feedbackAnswer', backref='User')
    tickets = db.relationship('feedbackAnswer', backref='User')

    def __init__(self, isAdmin, emailAddress, createDate, name, birthDate, association, feedbackAnswers=[], tickets=[]):
        self.isAdmin = isAdmin
        self.emailAddress = emailAddress
        self.createDate = createDate
        self.name = name
        self.birthDate = birthDate
        self.association = association
        self.feedbackAnswers = feedbackAnswers
        self.tickets = tickets

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = User
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    isAdmin = fields.Boolean(required=True) #is this right?
    emailAdress = fields.String(required=True)
    createDate = fields.Date(required=True)
    name = fields.String(required=True)
    birthDate = fields.Date(required=True)
    association = fields.String(required=True)
    feedbackAnswers = fields.Nested(FeedbackAnswerSchema, many=True)
    tickets = fields.Nested(TicketSchema, many=True)
