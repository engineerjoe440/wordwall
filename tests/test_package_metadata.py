"""Unit tests for package metadata constants."""

import wordwall


def test_package_version_is_semver_like_string() -> None:
    """Version should be exposed as a dotted string."""
    parts = wordwall.__version__.split(".")

    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_header_matches_module_docstring() -> None:
    """Header constant should mirror the module-level docstring."""
    assert wordwall.__header__ == wordwall.__doc__
