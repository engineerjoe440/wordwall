################################################################################
"""
WordWall - Simple, Self-Hosted Collaborative Word Cloud Generator.

(c) 2024 | Stanley Solutions | Joe Stanley
License: MIT
"""
################################################################################

from uuid import uuid4

from loguru import logger

#pylint: disable=too-few-public-methods
class Wall:
    """Structure to Represent a Wall."""

    id: str
    name: str

    def __init__(self):
        """Set Up New Wall Record."""
        self.id = str(uuid4())
        self.name = ""
        self._active = True

    @property
    def active(self) -> bool:
        """Indication whether the Wall is Active for New Words."""
        return self._active

    @active.setter
    def active(self, new: bool) -> None:
        """Set the State of the Active/Inactive Flag."""
        self._active = new

    @property
    def hash(self) -> str:
        """Return the 4-Character Hash of the Wall ID."""
        return str(hash(self.id))[-4:]
#pylint: enable=too-few-public-methods

ALL_WALLS: list[Wall] = []

class Manager:
    """Tracking Engine to Record all Active Word Walls."""

    _walls: list[Wall] = ALL_WALLS

    def new_wall(self) -> Wall:
        """Record a New Wall."""
        new_wall = Wall()
        self._walls.append(new_wall)
        logger.debug(f"Storing new wall information. ID: {new_wall.id}")
        return new_wall

    def all_walls(self) -> list[Wall]:
        """Return all Walls."""
        return self._walls

    def get_by_id(self, wall_id: str) -> Wall:
        """Locate the Wall by its ID."""
        for wall in self._walls:
            if wall.id == wall_id:
                return wall
        return None

    def get_by_hash(self, wall_hash: str) -> Wall:
        """Locate the Wall by its ID."""
        for wall in self._walls:
            if wall.hash == wall_hash:
                return wall
        return None
