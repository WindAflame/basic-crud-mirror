import time
from flask_restx import Resource, Namespace

import datastore

ns = Namespace('health', description='Check API')

@ns.route('/', endpoint='')
class HealthGETResource(Resource):
    def get(self):
        current = time.time()
        uptime = current - datastore.start_time
        response = {
            "uptime": uptime,
            "message": "Ok",
            "date": current
        }
        return response, 200
