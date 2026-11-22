import re

def contains_url(message_body):
    pattern = re.compile(
        "https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}([-a-zA-Z0-9()@:%_+.~#?&/=]*)")
    matched = pattern.search(message_body).group(0)
    if matched.endswith("."):
        matched = matched[:-1]
    return matched