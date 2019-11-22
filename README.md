# Simple GitLab webhook implementation with python+flask

Simple implementation for basic use only. 

```
from flask import Flask
app = Flask(__name__)           # create Flask app

from webhooks import WebHooks
webhooks = WebHooks(app, '/')   # create WebHooks via Flask

import subprocess

@webhooks.route('Push Hook')    # flask style routing
def push(body):
    # I want to clone this repository when push webhook is requested
    code = subprocess.call(['git', 'clone', 'https://github.com/MakeDirtyCode/GitLab-WebHooks.git'])
    if code:
        return 'BAD REQUEST', 400
    else:
        return 'OK', 200

app.run(host='0.0.0.0', port=5000)
```