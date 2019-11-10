from frontmatter import Frontmatter

from sse_bot import slack


class Episode(object):
    @classmethod
    def parse(cls, text):
        return cls(Frontmatter.read(text))

    def __init__(self, data):
        self.data = data
        self.title = self.data["attributes"]["title"]
        parts = self.title.split(": ")
        self.show_number = parts[0]

        topic_parts = [part.strip().capitalize() for part in parts[2].split(" and ")]
        self.first_topic = topic_parts[0]
        self.second_topic = topic_parts[1]

        body = self.data["body"]
        questions_start = body.find("\n\n") + 2
        questions_parts = body[questions_start:].split("\n\n\n")
        # Remove the first 3 chars which is the "1. " before the question
        self.first_question = question_parts[1][3:]
        self.second_question = body_parts[2][3:].strip()  # one trailing newline

    def slack_format_topics(self):
        return [
            slack.format_topic(self.show_number, topic)
            for topic in [self.first_topic, self.second_topic]
        ]

    def slack_format_questions(self):
        return [
            slack.format_question(question)
            for question in [self.first_question, self.second_question]
        ]
