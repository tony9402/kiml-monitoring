import os

from git import Repo


def clone_or_pull(url, path):
    if not os.path.exists(path):
        Repo.clone_from(url, path)
    else:
        repo = Repo(path)
        repo.remotes.origin.pull()
