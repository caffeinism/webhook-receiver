
from flask import Flask

app = Flask(__name__)

from webhook_receiver import get_webhooks
webhooks = get_webhooks(app, target='gitlab', endpoint='/', token='test')

from webhook_receiver import Event
@webhooks.route(event=Event.PUSH)
def github_push_hook(data):
    # some task what you want
    return 'PUSH Success!', 200

@webhooks.route(event=Event.PING)
def github_push_hook(data):
    return 'PONG!', 200

app.run(host='0.0.0.0', port=5000)
