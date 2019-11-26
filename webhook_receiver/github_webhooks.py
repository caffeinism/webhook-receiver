import hashlib
import hmac
from webhook_receiver.event import Event
from webhook_receiver.flask_utils import get, get_header, get_json, get_data
from flask import abort

def get_digest(token):
    return hmac.new(bytes(token, 'utf-8'), get_data(), hashlib.sha1).hexdigest() if token else None
    
header_github_event_map = {
    'push': Event.PUSH,
    'issue': Event.ISSUE,
    'pull_request': Event.PULL_REQ, 
    'create': Event.CREATE, 
    'gollum': Event.WIKI, 

    'fork': Event.FORK,
    'ping': Event.PING,
}

from .webhooks import WebHooks
class GitHubWebHooks(WebHooks):
    def validation(self):
        digest = get_digest(self.token)

        if digest is not None:
            sig_parts = get_header("X-Hub-Signature").split("=", 1)
            
            if not isinstance(digest, str):
                digest = str(digest)

            if len(sig_parts) < 2 or sig_parts[0] != "sha1" or not hmac.compare_digest(sig_parts[1], digest):
                abort(400, "Invalid signature")

    def get_event(self):
        str_event = get_header('X-GitHub-Event')
        event = get(header_github_event_map, str_event)

        return event
