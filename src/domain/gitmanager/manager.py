import git


class GitManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)

    def get_staged_diff(self):
        """Return the diff of staged changes."""
        staged_diff = self.repo.git.diff("--cached")
        return staged_diff
