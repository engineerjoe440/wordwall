################################################################################
"""
WordWall - Simple, Self-Hosted Collaborative Word Cloud Generator.

(c) 2024 | Stanley Solutions | Joe Stanley
License: MIT
"""
################################################################################

from fastapi import APIRouter

from ...backend.wordwall.api import walls, words
from ..session import Manager

router = APIRouter(prefix="/api/v1")

router.include_router(router=walls.router)
router.include_router(router=words.router)

manager = Manager()
