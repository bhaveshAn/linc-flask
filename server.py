from flask import Flask
from flask_rest_jsonapi import Api
from envparse import env

from db import db
from apis import (
    UserList, UserDetail, UserRelationship,
    ExperienceList, ExperienceDetail, ExperienceRelationship
)


env.read_envfile()

app = Flask(__name__)
app.config.from_object(env('APP_CONFIG', default='config.ProductionConfig'))
app.secret_key = 'mysecret'
api = Api(app)


api = Api(app)
api.route(UserList, 'user_list', '/users')
api.route(UserDetail, 'user_detail', '/users/<int:id>', '/experience/<int:experience_id>/user')
api.route(UserRelationship, 'user_experiences', '/users/<int:id>/relationships/experiences')
api.route(ExperienceList, 'experience_list', '/experiences', '/users/<int:id>/experiences')
api.route(ExperienceDetail, 'experience_detail', '/experiences/<int:id>')
api.route(ExperienceRelationship, 'experience_user', '/experiences/<int:id>/relationships/user')


if __name__ == '__main__':
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug=True)
