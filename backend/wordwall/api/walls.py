################################################################################
"""
WordWall - Simple, Self-Hosted Collaborative Word Cloud Generator.

(c) 2024 | Stanley Solutions | Joe Stanley
License: MIT
"""
################################################################################

from fastapi import APIRouter
# pylint: disable=no-name-in-module
from pydantic import BaseModel
# pylint: enable=no-name-in-module

from ..session import Manager

router = APIRouter(prefix="/walls")

manager = Manager()

@router.get("/list-all")
async def get_list_of_all_walls() -> list[dict[str, str]]:
    """Return a List of All Wall-IDs."""
    return [{"id": w.id, "hash": w.hash} for w in manager.all_walls()]


@router.get("/{wall_id}/name")
async def get_wall_name(wall_id: str) -> str:
    """Provide the Friendly Name for the Wall."""
    return manager.get_by_id(wall_id=wall_id).name


@router.get("/{wall_id}/enabled")
async def get_wall_active_status(wall_id: str) -> bool:
    """Provide the Enabled Status for the Wall."""
    return manager.get_by_id(wall_id=wall_id).active

# pylint: disable=too-few-public-methods
class WallData(BaseModel):
    """Base Data for a Wall."""
    name: str
# pylint: enable=too-few-public-methods

# pylint: disable=too-few-public-methods
class WallEnable(BaseModel):
    """Base Data for Enabling a Wall."""
    enable: bool = True
# pylint: enable=too-few-public-methods

@router.post("/{wall_id}/name")
async def set_wall_name(wall_id: str, data: WallData):
    """Apply the Wall Settings (Change the Name, etc.)."""
    manager.get_by_id(wall_id=wall_id).name = data.name

@router.post("/{wall_id}/enabled")
async def enable_wall(wall_id: str, data: WallEnable):
    """Enable the Specified Wall.."""
    manager.get_by_id(wall_id=wall_id).active = data.enable
