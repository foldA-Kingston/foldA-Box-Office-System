#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.model_feedbackAnswer import FeedbackAnswerSchema # this might be wrong

class User (db.Model):
    __tablename__ = 'user'
    #Many tickets have one user
    #One User provides many Feed Back answers 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isAdmin = db.Column(db.Boolean) #is this right?
    emailAdress = db.Column(db.String)
    createDate = db.Column(db.Date)
    name = db.Column(db.String)
    birthDate = db.Column(db.Date)
    association =db.Column(db.String)
    feedbackAnswer = db.relationship('feedbackAnswer', backref='User')

    def __init__(self, isAdmin, emailAdress, createDate, name, birthDate, association, feedbackAnswer=[]):
        self.isAdmin = isAdmin
        self.emailAdress = emailAdress
        self.createDate = createDate
        self.name = name
        self.birthDate = birthDate
        self.association = association
        self.feedbackAnswer = feedbackAnswer

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
    feedbackAnswer = fields.Nested(FeedbackAnswerSchema, many=True)
