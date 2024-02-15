import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.users import User

mood_api = Blueprint('mood_api', __name__,
                   url_prefix='/api/mood')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(mood_api)

class MoodAPI:  
    class _LogEmoji(Resource):
        def post(emoji, date):
            body = request.get_json()

            emoji = body.get("emoji")
            date = body.get("date")

            moodJson = open("../instance/volumes/mood.json", "w")
            moodJson.write("{ 'emoji': " + emoji + ", 'date': " + date + "}")

            
    # building RESTapi endpoint
    api.add_resource(_LogEmoji, '/log')
    
    