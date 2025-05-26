from datetime import datetime
from flask_restx import Namespace, Resource

import datastore as DS

ns = Namespace('health', description='Check API')

@ns.route('/', endpoint='')
class HealthGETResource(Resource):
    def get(self):
        current = datetime.now()
        uptime = current - DS.start_time
        response = {
            "status": "healthy",
            "start_time": DS.start_time.isoformat(),
            "up_time": uptime.total_seconds(),
            "books_count": len(DS.books)
        }
        return response, 200
