"""
Concrete implementation of creature cards for the DataDeck game.

This module provides the abstract Creature base class and concrete
implementations for different creature types:
- Fire family: Flameling (base), Pyrodon (evolved)
- Water family: Aquabub (base), Torragon (evolved)

Classes:
    Creature: Abstract base class for all creatures
    Flameling: Base Fire-type creature
    Pyrodon: Evolved Fire/Flying-type creature
    Aquabub: Base Water-type creature
    Torragon: Evolved Water-type creature
"""

from abc import ABC, abstractmethod


class Creature(ABC):
    """
    Abstract base class for all creatures in the game.

    Attributes:
        name (str): The creature's name
        creature_type (str): The creature's type (e.g., "Fire", "Water")

    Methods:
        attack: Abstract method that returns the attack description
        describe: Returns a formatted description of the creature
    """

    def __init__(self, name: str, creature_type: str) -> None:
        """
        Initialize a new Creature instance.

        Args:
            name: The creature's name
            creature_type: The creature's type classification
        """
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """
        Execute the creature's attack.

        Returns:
            A string describing the attack action
        """
        pass

    def describe(self) -> str:
        """
        Get a description of the creature.

        Returns:
            A formatted string with the creature's name and type
        """
        return f"{self.name} is a {self.creature_type} type Creature"


# ----------------------------------------------------------------------
# Creature with fire capability
# ----------------------------------------------------------------------


class Flameling(Creature):
    """
    Base Fire-type creature.

    Flameling is the basic Fire family creature that uses Ember attack.
    """

    def __init__(self, name: str, creature_type: str = "Fire") -> None:
        """
        Initialize a Flameling creature.

        Args:
            name: The creature's name
            creature_type: The creature's type (defaults to "Fire")
        """
        super().__init__(name, creature_type)

    def attack(self) -> str:
        """
        Attack with Ember.

        Returns:
            Attack description string
        """
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """
    Evolved Fire/Flying-type creature.

    Pyrodon is the evolved form of Flameling with Flamethrower attack.
    """

    def __init__(self, name: str, creature_type: str = "Fire/Flying") -> None:
        """
        Initialize a Pyrodon creature.

        Args:
            name: The creature's name
            creature_type: The creature's type (defaults to "Fire/Flying")
        """
        super().__init__(name, creature_type)

    def attack(self) -> str:
        """
        Attack with Flamethrower.

        Returns:
            Attack description string
        """
        return f"{self.name} uses Flamethrower!"


# ----------------------------------------------------------------------
# Creature with water capability
# ----------------------------------------------------------------------

class Aquabub(Creature):
    """
    Base Water-type creature.

    Aquabub is the basic Water family creature that uses Water Gun attack.
    """

    def __init__(self, name: str, creature_type: str = "Water") -> None:
        """
        Initialize an Aquabub creature.

        Args:
            name: The creature's name
            creature_type: The creature's type (defaults to "Water")
        """
        super().__init__(name, creature_type)

    def attack(self) -> str:
        """
        Attack with Water Gun.

        Returns:
            Attack description string
        """
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """
    Evolved Water-type creature.

    Torragon is the evolved form of Aquabub with Hydro Pump attack.
    """

    def __init__(self, name: str, creature_type: str = "Water") -> None:
        """
        Initialize a Torragon creature.

        Args:
            name: The creature's name
            creature_type: The creature's type (defaults to "Water")
        """
        super().__init__(name, creature_type)

    def attack(self) -> str:
        """
        Attack with Hydro Pump.

        Returns:
            Attack description string
        """
        return f"{self.name} uses Hydro Pump!"
