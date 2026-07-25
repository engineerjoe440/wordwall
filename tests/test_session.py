"""Unit tests for wall/session management."""

from wordwall.session import ALL_WALLS, Manager


def setup_function() -> None:
    """Ensure global wall state is isolated per test."""
    ALL_WALLS.clear()


def teardown_function() -> None:
    """Ensure global wall state is isolated per test."""
    ALL_WALLS.clear()


def test_new_wall_registers_and_defaults() -> None:
    """A newly created wall is stored and starts active."""
    manager = Manager()

    wall = manager.new_wall()

    assert wall in manager.all_walls()
    assert wall.name == ""
    assert wall.active is True
    assert isinstance(wall.id, str)
    assert len(wall.hash) == 4


def test_get_by_id_and_hash_returns_same_wall() -> None:
    """Wall lookups by id/hash should resolve to the same object."""
    manager = Manager()
    wall = manager.new_wall()

    assert manager.get_by_id(wall.id) is wall
    assert manager.get_by_hash(wall.hash) is wall


def test_missing_wall_returns_none() -> None:
    """Unknown wall identifiers should return None."""
    manager = Manager()

    assert manager.get_by_id("missing") is None
    assert manager.get_by_hash("9999") is None


def test_wall_active_flag_can_be_toggled() -> None:
    """The active state can be updated through the property setter."""
    manager = Manager()
    wall = manager.new_wall()

    wall.active = False
    assert wall.active is False

    wall.active = True
    assert wall.active is True
