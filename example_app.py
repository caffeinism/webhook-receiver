from flask import Flask
app = Flask(__name__)           # create Flask app

from webhooks import WebHooks
webhooks = WebHooks(app, '/')   # create WebHooks via Flask

import subprocess

@webhooks.route('Push Hook')
def push(body):
    # I want to clone this repository when push webhook is requested
    code = subprocess.call(['git', 'clone', 'https://github.com/MakeDirtyCode/GitLab-WebHooks.git']).split())
    if code:
        return 'BAD REQUEST', 400
    else:
        return 'OK', 200

# @webhooks.route('Tag Push Hook')
# def tag_push(body):
#     return 'OK', 200

# @webhooks.route('Issue Hook')
# def issue(body):
#     return 'OK', 200

# @webhooks.route('Note Hook')
# def comment(body):
#     return 'OK', 200

# @webhooks.route('Merge Request Hook')
# def merge_request(body):
#     return 'OK', 200

# @webhooks.route('Wiki Page Hook')
# def wiki_page(body):
#     return 'OK', 200

# @webhooks.route('Pipeline Hook')
# def pipeline(body):
#     return 'OK', 200

# @webhooks.route('Job Hook')
# def job(body):
#     return 'OK', 200

app.run(host='0.0.0.0', port=5000)
