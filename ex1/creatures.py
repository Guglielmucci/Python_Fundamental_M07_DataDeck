"""
Concrete creature implementations with capabilities.

This module provides concrete creature classes that inherit from both
Creature (from ex0) and specific capability classes (from ex1).

Classes:
    Sproutling: Base Grass-type creature with healing
    Bloomelle: Evolved Grass/Fairy-type creature with healing
    Shiftling: Base Normal-type creature with transformation
    Morphagon: Evolved Normal/Dragon-type creature with transformation
"""

from typing import Optional
from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


# ----------------------------------------------------------------------
# Creature with healing capability
# ----------------------------------------------------------------------


class Sproutling(Creature, HealCapability):
    """
    Base Grass-type creature with healing capability.

    Sproutling can heal itself for a small amount.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Sproutling creature.

        Args:
            name: The creature's name
        """
        super().__init__(name, "Grass")

    def attack(self) -> str:
        """
        Attack with Vine Whip.

        Returns:
            Attack description string
        """
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[str] = None) -> str:
        """
        Heal itself for a small amount.

        Args:
            target: Ignored, always heals self

        Returns:
            Healing description string
        """
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """
    Evolved Grass/Fairy-type creature with healing capability.

    Bloomelle can heal itself and others for a large amount.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Bloomelle creature.

        Args:
            name: The creature's name
        """
        super().__init__(name, "Grass/Fairy")

    def attack(self) -> str:
        """
        Attack with Petal Dance.

        Returns:
            Attack description string
        """
        return f"{self.name} uses Petal Dance!"

    def heal(self, target: Optional[str] = None) -> str:
        """
        Heal itself and optionally others for a large amount.

        Args:
            target: Optional target to heal

        Returns:
            Healing description string
        """
        return f"{self.name} heals itself and others for a large amount"


# ----------------------------------------------------------------------
# Creature with transform capability
# ----------------------------------------------------------------------


class Shiftling(Creature, TransformCapability):
    """
    Base Normal-type creature with transformation capability.

    Shiftling can shift into a sharper form, boosting its attacks.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Shiftling creature.

        Args:
            name: The creature's name
        """
        Creature.__init__(self, name, "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """
        Attack normally or with boost if transformed.

        Returns:
            Attack description string
        """
        if self._transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """
        Transform into a sharper form.

        Returns:
            Transformation description string
        """
        self._transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        """
        Revert to normal form.

        Returns:
            Reversion description string
        """
        self._transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """
    Evolved Normal/Dragon-type creature with transformation capability.

    Morphagon can morph into a dragonic battle form for devastating attacks.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Morphagon creature.

        Args:
            name: The creature's name
        """
        Creature.__init__(self, name, "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        """
        Attack normally or with devastating power if transformed.

        Returns:
            Attack description string
        """
        if self._transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        """
        Morph into a dragonic battle form.

        Returns:
            Transformation description string
        """
        self._transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        """
        Stabilize back to normal form.

        Returns:
            Stabilization description string
        """
        self._transformed = False
        return f"{self.name} stabilizes its form."
