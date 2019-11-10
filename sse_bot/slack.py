def format_topic(show_number, topic):
    return f"*{show_number}: {topic}*"


def format_question(question):
    lines = [l.strip() for l in question.split("\n\n")]
    # one quote marker to start, then separate paragraphs by
    # newline-quote-newline-quote-space
    return "> " + "\n>\n> ".join(lines)
