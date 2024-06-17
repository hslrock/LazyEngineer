import os
import sys
from pathlib import Path

from domain.generation.api.gemini import GeminiGenerator
from domain.gitmanager.manager import GitManager
from domain.renderer.renderer import JinjaTemplateRenderer
from src.settings import load_settings

SETTINGS = load_settings()


def commit(manager: GitManager, repo_path=Path):
    # Your commit script logic here
    print("Running lazyengineer commit")
    diff_text = manager.get_staged_diff()

    renderer = JinjaTemplateRenderer(template_name="v1.jinja2", asset_path="commit")
    prompt = renderer.render(diff=diff_text)

    generator = GeminiGenerator(settings=SETTINGS)
    response = generator.generate(prompt)
    manager.commit_with_message(response.text)


def pr():
    # Your pr script logic here
    print("Not implemented yet.")


def main():
    repo_path = os.getcwd()
    manager = GitManager(repo_path)

    if len(sys.argv) < 2:
        print("Usage: lazyengineer <command>")
        sys.exit(1)

    command = sys.argv[1]
    print("hello:")
    if command == "commit":
        commit(manager, repo_path)
    elif command == "pr":
        pr()
    else:
        print(f"Unknown command: {command}")
        print("Usage: lazyengineer <command>")
        sys.exit(1)


if __name__ == "__main__":
    main()
