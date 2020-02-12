#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isPurchased = db.Column(db.Boolean)
    surname = db.Column(db.String)
    createDate = db.Column(db.DateTime, server_default=db.func.now())
    purchaseDate = db.Column(db.DateTime)

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    purchasable_id = db.Column(db.Integer, db.ForeignKey('purchasables.id'))
    ticketClass_id = db.Column(db.Integer, db.ForeignKey(
        'ticketClasses.id'))  # TODO: How are we pluralizing?
    userId_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, isPurchased, purchaseDate, event_):
        self.isPurchased = isPurchased
        self.purchaseDate = purchaseDate

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class TicketSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Ticket
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    isPurchased = fields.Boolean(required=True)
    purchaseDate = fields.DateTime(required=False)
    createDate = fields.String(dump_only=True)
