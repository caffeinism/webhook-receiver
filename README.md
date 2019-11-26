# Simple GitLab webhook implementation with python+flask

Simple implementation for basic use only. 

```
from flask import Flask

app = Flask(__name__)

from webhooks import get_webhooks
webhooks = get_webhooks(app, target='gitlab', endpoint='/', token='test')

from webhooks import Event
@webhooks.route(event=Event.PUSH)
def github_push_hook(data):
    # some task what you want
    return 'PUSH Success!', 200

@webhooks.route(event=Event.PING)
def github_push_hook(data):
    return 'PONG!', 200

app.run(host='0.0.0.0', port=5000)
```
