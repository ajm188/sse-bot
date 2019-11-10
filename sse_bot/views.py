from flask import Blueprint

from sse_bot import github
from sse_bot import hooks


routes = Blueprint("sse_bot", __name__)


@routes.route("/pull_request_event", methods=["POST"])
def pull_request_event():
    payload = request.get_json()["payload"]
    hooks.process_pr_event(github.PullRequest(payload))
