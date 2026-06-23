"""
Factory implementations for creatures with capabilities.

This module provides concrete factory classes that extend the base
CreatureFactory to produce creatures with special capabilities.

Classes:
    HealingCreatureFactory: Factory for healing-capable creatures
    TransformCreatureFactory: Factory for transform-capable creatures
"""

from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    """
    Factory for creating creatures with healing capability.

    Creates Sproutling (base) and Bloomelle (evolved) creatures.
    """

    def create_base(self, name: str) -> Creature:
        """
        Create a base healing creature (Sproutling).

        Args:
            name: The name for the new creature

        Returns:
            A Sproutling instance
        """
        return Sproutling(name)

    def create_evolved(self, name: str) -> Creature:
        """
        Create an evolved healing creature (Bloomelle).

        Args:
            name: The name for the new creature

        Returns:
            A Bloomelle instance
        """
        return Bloomelle(name)


class TransformCreatureFactory(CreatureFactory):
    """
    Factory for creating creatures with transform capability.

    Creates Shiftling (base) and Morphagon (evolved) creatures.
    """

    def create_base(self, name: str) -> Creature:
        """
        Create a base transform creature (Shiftling).

        Args:
            name: The name for the new creature

        Returns:
            A Shiftling instance
        """
        return Shiftling(name)

    def create_evolved(self, name: str) -> Creature:
        """
        Create an evolved transform creature (Morphagon).

        Args:
            name: The name for the new creature

        Returns:
            A Morphagon instance
        """
        return Morphagon(name)
