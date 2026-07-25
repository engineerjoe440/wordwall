"""Unit tests for configuration defaults and loading behavior."""

import importlib

from wordwall import configuration


def test_default_configuration_shape() -> None:
    """Default config should provide expected application keys."""
    app_defaults = configuration.DEFAULT_CONFIGURATION["application"]

    assert app_defaults["site_url"] == ""
    assert app_defaults["site_name"] == "WordWall"
    assert app_defaults["cross_site_origins"] == [] # pylint: disable=use-implicit-booleaness-not-comparison
    assert app_defaults["storage_path"] == ""


def test_configuration_uses_env_config_path(monkeypatch, tmp_path) -> None:
    """Reloading with CONFIG_FILE set should point config to that location."""
    monkeypatch.setenv("CONFIG_FILE", str(tmp_path))

    reloaded = importlib.reload(configuration)

    assert reloaded.CONFIG_FILE_PATH == tmp_path
    assert reloaded.settings.application.site_name == "WordWall"
