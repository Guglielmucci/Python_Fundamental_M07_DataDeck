"""
Abstract factory implementation for creature creation.

This module provides the abstract factory pattern implementation
for creating creatures of different families (Fire and Water).
Each factory can create both base and evolved creatures.

Classes:
    CreatureFactory: Abstract base class for creature factories
    FlameFactory: Concrete factory for Fire-type creatures
    AquaFactory: Concrete factory for Water-type creatures
"""

from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """
    Abstract factory for creating creatures of a specific family.

    This class defines the interface for creature factories that can
    create both base and evolved versions of creatures from the same family.
    """

    @abstractmethod
    def create_base(self, name: str) -> Creature:
        """
        Create a base creature of this family.

        Args:
            name: The name to assign to the created creature

        Returns:
            A new base Creature instance
        """
        pass

    @abstractmethod
    def create_evolved(self, name: str) -> Creature:
        """
        Create an evolved creature of this family.

        Args:
            name: The name to assign to the created creature

        Returns:
            A new evolved Creature instance
        """
        pass


class FlameFactory(CreatureFactory):
    """
    Factory for creating Fire-type creatures.

    Creates Flameling (base) and Pyrodon (evolved) creatures.
    """

    def create_base(self, name: str) -> Creature:
        """
        Create a base Fire creature (Flameling).

        Args:
            name: The name for the new creature

        Returns:
            A Flameling instance
        """
        return Flameling(name)

    def create_evolved(self, name: str) -> Creature:
        """
        Create an evolved Fire creature (Pyrodon).

        Args:
            name: The name for the new creature

        Returns:
            A Pyrodon instance
        """
        return Pyrodon(name)


class AquaFactory(CreatureFactory):
    """
    Factory for creating Water-type creatures.

    Creates Aquabub (base) and Torragon (evolved) creatures.
    """

    def create_base(self, name: str) -> Creature:
        """
        Create a base Water creature (Aquabub).

        Args:
            name: The name for the new creature

        Returns:
            An Aquabub instance
        """
        return Aquabub(name)

    def create_evolved(self, name: str) -> Creature:
        """
        Create an evolved Water creature (Torragon).

        Args:
            name: The name for the new creature

        Returns:
            A Torragon instance
        """
        return Torragon(name)
