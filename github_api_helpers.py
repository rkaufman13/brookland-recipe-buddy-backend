import json
import datetime
import requests
from config import get_settings

settings = get_settings()
api_key = settings.github_api_key

GITHUB_USER = 'rkaufman13'
REPO_NAME = 'Brookland-recipe-buddy'


def gh_sesh(user, token):
    s = requests.Session()
    s.auth = (user, token)
    s.headers = {'accept': 'application/vnd.github.v3+json'}
    return s


class GithubResponseObj:
    def __init__(self, json_all, next_page):
        self.json_all = json_all
        self.next_page = next_page


def gh_get_request(s, url):
    response = s.get(url)
    response_status = response.status_code
    if response_status > 200:
        print(f'\n This was the response code: {response_status}')
        exit()

    json = response.json()
    links = response.links

    try:
        next_page = links['next']['url']
    except:
        next_page = None

    full = GithubResponseObj(json, next_page)

    return full


def gh_post_request(s, url, data):
    response = s.post(url, data)
    response_status = response.status_code
    if response_status > 201:
        print(f'\n This was the response code: {response_status}')
        exit()

    json = response.json()

    return json


s = gh_sesh(GITHUB_USER, api_key)


def get_branch_sha(branch_name="master"):
    url = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/branches/{branch_name}'
    response = gh_get_request(s, url)
    sha = response.json_all['commit']['sha']
    return sha


def create_tree(base_tree_sha, content, path):
    url = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/git/trees'
    new_tree = {
        "base_tree": base_tree_sha,
        "tree": [{"path": f"_posts/{path}", "mode": "100644", "type": "blob", "content": content}]
    }
    data = json.dumps(new_tree)
    response = gh_post_request(s, url, data)
    return response.get('sha')


def create_new_branch(master_branch_sha):
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    new_sync_branch = f'new_branch_{now}'
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/git/refs"

    ref = f'heads/{new_sync_branch}'

    data = {
        "ref": f'refs/{ref}',
        "sha": master_branch_sha
    }

    data = json.dumps(data)

    response = gh_post_request(s, url, data)

    return response, ref, new_sync_branch


def create_commit(new_sha, main_sha):
    url = f' https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/git/commits'
    commit = {
        'message': 'commit created by api',
        'parents': [main_sha],
        'tree': new_sha
    }
    data = json.dumps(commit)
    response = gh_post_request(s, url, data)
    return response.get('sha')


def update_ref_pointer(new_ref, new_sha):
    url = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/git/refs/{new_ref}'
    new_pointer = {"sha": new_sha, "force": True}
    data = json.dumps(new_pointer)
    response = gh_post_request(s, url, data)


def create_pull_request(new_branch_name, branch_title):
    url = f'https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/pulls'
    pr = {"title": branch_title, "body": "Generated via api", "head": new_branch_name, "base": "main"}
    data = json.dumps(pr)
    response = gh_post_request(s, url, data)


def do_the_thing(content, filename):
    main_sha = get_branch_sha("main")
    new_branch, new_ref, branch_name = create_new_branch(main_sha)
    new_sha = create_tree(new_branch.get('object').get('sha'), content, filename)
    new_commit = create_commit(new_sha, main_sha)
    update_ref_pointer(new_ref, new_commit)
    create_pull_request(branch_name, filename)


if __name__ == '__main__':
    do_the_thing("come on this is a test", 'whatever.md')
