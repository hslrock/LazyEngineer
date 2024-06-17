import git


class GitManager:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)

    def get_staged_diff(self):
        """Return the diff of staged changes."""
        staged_diff = self.repo.git.diff("--cached")
        return staged_diff

    def commit_with_message(self, commit_message):
        """Commit the staged changes with the provided commit message."""
        if self.repo.is_dirty(untracked_files=True):
            self.repo.index.commit(commit_message)
            print(f"Committed with message: {commit_message}")
        else:
            print("No changes to commit.")
