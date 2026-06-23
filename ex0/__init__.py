"""
DataDeck Game - Creature Factory Package.

This package implements the abstract factory design pattern for creating
creature cards in the DataDeck game. It provides factory classes for
different creature families (Fire and Water) while hiding concrete
creature implementations.

Exports:
    CreatureFactory: Abstract base class for creature factories
    FlameFactory: Concrete factory for Fire-type creatures
    AquaFactory: Concrete factory for Water-type creatures
"""

from .factory import CreatureFactory, FlameFactory, AquaFactory

__all__ = ["CreatureFactory", "FlameFactory", "AquaFactory"]
