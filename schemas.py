from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from marshmallow import validate

CITIES = ['Mumbai', 'Bangalore', 'New Delhi', 'Chennai', 'Kolkata']


class UserSchema(Schema):
    class Meta:
        type_ = 'user'
        self_view = 'user_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'user_list'

    id = fields.Integer(as_string=True)
    name = fields.Str(required=True, allow_none=False)
    full_address = fields.Str(allow_none=True)
    city = fields.Str(validate=validate.OneOf(choices=CITIES), allow_none=True)
    primary_email = fields.Email(required=True)
    secondary_email = fields.Email(allow_none=True)
    date_of_birth = fields.Date(allow_none=True)
    primary_phone = fields.Integer(allow_none=True)
    secondary_phone = fields.Integer(allow_none=True)
    experiences = Relationship(self_view='user_experiences',
                               self_view_kwargs={'id': '<id>'},
                               related_view='experience_list',
                               related_view_kwargs={'id': '<id>'},
                               many=True,
                               schema='ExperienceSchema',
                               type_='experience')


class ExperienceSchema(Schema):
    class Meta:
        type_ = 'experience'
        self_view = 'experience_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer(as_string=True)
    company = fields.Str(required=True)
    designation = fields.Str()
    city = fields.Str(validate=validate.OneOf(choices=CITIES), allow_none=True)
    start_date = fields.Date()
    end_date = fields.Date()
    type = fields.Str(
        validate=validate.OneOf(choices=['Full-Time', 'Part-Time']),
        allow_none=True)
    role_description = fields.Str()
    duration = fields.Str(allow_none=True)
    user = Relationship(attribute='user',
                        self_view='experience_user',
                        self_view_kwargs={'id': '<id>'},
                        related_view='user_detail',
                        related_view_kwargs={'experience_id': '<id>'},
                        schema='UserSchema',
                        type_='user')
