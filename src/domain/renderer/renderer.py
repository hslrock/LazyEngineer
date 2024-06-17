from jinja2 import Environment
from jinja2 import FileSystemLoader

from utils.path import get_asset_path


class JinjaTemplateRenderer:
    def __init__(self, template_name: str, asset_path: str = "commit"):
        self.template_name = template_name
        print(get_asset_path(asset_path))
        self.env = Environment(loader=FileSystemLoader(get_asset_path(asset_path)))

    def render(self, **kwargs) -> str:
        template = self.env.get_template(self.template_name)
        return template.render(**kwargs)
