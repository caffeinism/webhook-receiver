from webhook_receiver.gitlab_webhooks import GitLabWebHooks
from webhook_receiver.github_webhooks import GitHubWebHooks
from webhook_receiver.event import Event

def get_webhooks(app, target, endpoint, token=None):
    if target.lower() == 'github':
        return GitHubWebHooks(app, endpoint=endpoint, token=token)
    elif target.lower() == 'gitlab':
        return GitLabWebHooks(app, endpoint=endpoint, token=token)
    else:
        raise NotImplementedError
