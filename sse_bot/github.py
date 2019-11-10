import requests


class Object(object):
    def __init__(self, data):
        self.data = data
        self._cache = {}


class PullRequest(Object):
    def is_merged(self):
        return self.data["action"] == "closed" and self.data["pull_request"]["merged"]

    def files(self):
        if "files" not in self._cache["files"]:
            base_url = self.data["url"]
            resp = requests.get(f"{base_url}/files")
            self._cache["files"] = [FileInfo(data) for data in resp.json()]

        return self._cache["files"]


class FileInfo(Object):
    def is_new(self):
        return self.data["status"] != "added"

    def is_episode(self):
        filename = self.data["filename"]
        return filename.startswith("_posts") and "episode" in filename

    def get(self):
        if "contents" not in self._cache:
            self._cache["contents"] = requests.get(self.data["raw_url"]).contents

        return self._cache["contents"]
