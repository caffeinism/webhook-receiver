from flask import request, abort
from webhook_receiver.flask_utils import get, get_header, get_json

class WebHooks:
    def __init__(self, app, endpoint, token=None):
        self.route_map = {}
        self.token = token

        @app.route(endpoint, methods=['POST'])
        def receiver():
            self.validation()
            
            event = self.get_event()

            if event not in self.route_map:
                abort(400, 'Event is not registered')

            return self.route_map[event](get_json())

    def route(self, event):
        def decorator(func):
            if event in self.route_map:
                raise 'This mapping is duplicated'
            self.route_map[event] = func
            return func
        return decorator
    
    def validation(self):
        raise NotImplementedError

    def get_event(self):
        raise NotImplementedError
