#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.model_purchasable import Purchasable
from api.models.model_ticket import TicketSchema # this might be wrong

class Event(db.Model):
    __tablename__ = 'event'
    #Many Events give access to many tickets
    #Many Events contains one purchasable
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artistName = db.Column(db.String)
    imageUrl = db.Column(db.String)
    embedMedia = db.Column(db.String)
    description = db.Column(db.String)
    startTime = db.Column(db.Date)
    endTime = db.Column(db.Date)
    venue = db.Column(db.String)
    capacity = db.Column(db.Integer)
    isFull = db.Column(db.Boolean) #What is used for T/F?
    purchasable = db.relationship('Purchasable', backref='Event')
    tickets = db.relationship('TicketClass', backref='Event')

    def __init__(self, artistName, imageUrl, embedMedia, description, startTime, endTime, venue, capacity, isFull, purchasable, tickets=[]):
        self.artistName = artistName
        self.imageUrl = imageUrl
        self.embedMedia = embedMedia
        self.description = description
        self.startTime = startTime
        self.endTime = endTime
        self.venue = venue
        self.capacity = capacity
        self.isFull = isFull
        self.purchasable = purchasable
        self.tickets = tickets
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Event
        sqla_session = db.session
    
    id = fields.Number(dump_only=True)
    artistName = fields.String(required=True)
    imageUrl = fields.String(required=True)
    embedMedia = fields.String(required=True)
    description = fields.String(required=True)
    startTime = fields.Date(required=True)
    endTime = fields.Date(required=True)
    venue = fields.String(required=True)
    capacity = fields.Integer(required=True)
    isFull = fields.Boolean(required=True)
    purchasable = fields.Nested(PurchasableSchema, many=True) #need a refresher on foreign keys
    tickets = fields.Nested(TicketSchema, many=True)
