import re

from frontmatter import Frontmatter


# I'm going to assume that the "and" followed by a capital is the delineation
# between the topics in the show title, because I can't come up with a better
# way
TOPIC_DIVIDER = re.compile(r" and [A-Z]")


class Episode(object):
    @classmethod
    def parse(cls, text):
        return cls(Frontmatter.read(text))

    def __init__(self, data):
        self.data = data
        self.title = self.data["attributes"]["title"]
        parts = self.title.split(": ")
        self.show_number[0]
        topic_part = parts[2]
        match = TOPIC_DIVIDER.search(topic_part)
        self.first_topic = topic_part[: match.span()[0]]
        self.second_topic = topic_part[match.span()[1] - 1 :]

        body = self.data["body"]
        body_parts = body.split("\n\n")
        # Remove the first 3 chars which is the "1. " before the question
        self.first_question = body_parts[1][3:]
        # .strip() to remove the leading/trailing newlines, then remove the
        # first 3 chars for same reason as above
        self.second_question = body_parts[2].strip()[3:]
