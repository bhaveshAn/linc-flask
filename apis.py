from flask_rest_jsonapi import ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound
from sqlalchemy.orm.exc import NoResultFound

from db import db
from schemas import UserSchema, ExperienceSchema
from models import User, Experience


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User}


class UserDetail(ResourceDetail):
    def before_get_object(self, view_kwargs):
        if view_kwargs.get('experience_id'):
            try:
                experience = self.session.query(Experience).filter_by(id=view_kwargs['experience_id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'experience_id'},
                                     "Experience: {} not found".format(view_kwargs['experience_id']))
            else:
                if experience.user:
                    view_kwargs['id'] = experience.user.id
                else:
                    view_kwargs['id'] = None

    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User,
                  'methods': {'before_get_object': before_get_object}}


class UserRelationship(ResourceRelationship):
    schema = UserSchema
    data_layer = {'session': db.session,
                  'model': User}


class ExperienceList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(Experience)
        if view_kwargs.get('id'):
            try:
                self.session.query(User).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "User: {} not found".format(view_kwargs['id']))
            else:
                query_ = query_.join(User).filter(User.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            user = self.session.query(User).filter_by(id=view_kwargs['id']).one()
            data['user_id'] = user.id

    schema = ExperienceSchema
    data_layer = {'session': db.session,
                  'model': Experience,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}


class ExperienceDetail(ResourceDetail):
    schema = ExperienceSchema
    data_layer = {'session': db.session,
                  'model': Experience}


class ExperienceRelationship(ResourceRelationship):
    schema = ExperienceSchema
    data_layer = {'session': db.session,
                  'model': Experience}
