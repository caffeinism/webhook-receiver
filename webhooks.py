from flask import request

class WebHooks:
    def __init__(self, app, endpoint, token=None):
        self.route_map = {}
        self.token = token

        @app.route(endpoint, methods=['POST'])
        def receiver():
            headers = request.headers
            
            if self.token != headers.get('X-Gitlab-Token', None):
                return 'Token does not exist', 400
            
            if 'X-Gitlab-Event' not in headers:
                return 'Event does not exist', 400

            event = headers.get('X-Gitlab-Event', '')

            if event not in self.route_map:
                return 'Event is not registered', 400
            
            body = request.json

            return self.route_map[event](body)
    
    def route(self, event):
        def decorator(func):
            if event in self.route_map:
                raise 'This mapping is duplicated'
            self.route_map[event] = func
            return func
        return decorator