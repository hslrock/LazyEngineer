from pathlib import Path


def get_env_path(env_name=".env") -> Path:
    return Path(__file__).parent.parent.parent / env_name


def get_asset_path(asset_path: str) -> Path:
    return Path(__file__).parent.parent / "assets" / asset_path
