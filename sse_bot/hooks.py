from sse_bot.episode import Episode


def process_pr_event(pr):
    if not pr.is_merged():
        return

    new_episodes = find_new_episodes(pr.files())
    for episode_file in new_episodes:
        episode_text = episode_file.get()
        episode = Episode.parse(episode_text)


def find_new_episodes(files_list):
    return [
        file_info
        for file_info in files_list
        if file_info.is_new() and file_info.is_episode()
    ]


def parse_episode(episode_text):
    return Frontmatter.read(episode_text)
