from webhook_receiver.event import Event
from webhook_receiver.flask_utils import get, get_header, get_json
from flask import abort

header_gitlab_event_map = {
    'Push Hook': Event.PUSH, 
    'Issue Hook': Event.ISSUE, 
    'Merge Request Hook': Event.PULL_REQ, 
    'Tag Push Hook': Event.CREATE, 
    'Wiki Page Hook': Event.WIKI, 

    'Note Hook': Event.COMMENT, 
    'Pipeline Hook': Event.PIPELINE, 
}

from .webhooks import WebHooks
class GitLabWebHooks(WebHooks):
    def validation(self):
        if self.token and self.token != get_header('X-Gitlab-Token'):
            abort(400, 'Invalid signature')

    def get_event(self):
        str_event = get_header('X-Gitlab-Event')
        event = get(header_gitlab_event_map, str_event)

        return event
