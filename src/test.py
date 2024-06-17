import os

from domain.generation.api.gemini import GeminiGenerator
from domain.gitmanager.manager import GitManager
from domain.renderer.renderer import JinjaTemplateRenderer
from settings import load_settings

repo_path = os.getcwd()
manager = GitManager(repo_path)
diff_text = manager.get_staged_diff()


renderer = JinjaTemplateRenderer(template_name="v1.jinja2", asset_path="commit")
prompt = renderer.render(diff=diff_text)
print(prompt)

# Generate a SINGLE GIT commit-message. Follow next set of rules:

# Rule 1:
# - The commit message should be a single line.

# Rule 2:
# - Ensure the commit message follows the following prefixes:
#     - feat: A new feature
#     - fix: A bug fix
#     - docs: Documentation only changes
#     - style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
#     - refactor: A code change that neither fixes a bug nor adds a feature
#     - perf: A code change that improves performance
#     - test: Adding missing tests or correcting existing tests
#     - chore: Changes to the build process or auxiliary tools and libraries such as documentation generation

# Rule 3:
# - The commit message should be in the following format:
#     - <prefix>: <message>
#     - Example: feat: Add a new feature

# Rule 4:
# - The commit message should be generated from the following git-diff:
#     - hello -> hello world

# Rule 5:
# - You should never hallucinate the commit message. It should be generated from the git-diff.

# Your single commit message:

# Your single commit message:


settings = load_settings()
generator = GeminiGenerator(settings=settings)
response = generator.generate(prompt)

print(response.text)

# feat: Add "world" to string
