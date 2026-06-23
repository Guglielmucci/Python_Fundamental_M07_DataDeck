"""
Battle strategy implementations for creature tournaments.

This module provides the abstract strategy pattern implementation
for different battle behaviors that can be applied to creatures.

Classes:
    InvalidStrategyError: Exception raised for invalid strategy-creature pairs
    BattleStrategy: Abstract base class for all battle strategies
    NormalStrategy: Basic attack strategy (valid for any creature)
    AggressiveStrategy: Transform-based strategy (requires TransformCapability)
    DefensiveStrategy: Healing-based strategy (requires HealCapability)
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from ex0.creature import Creature


class InvalidStrategyError(Exception):
    """Raise an Exception when a strategy is applied to an incompatible creature.

    This occurs when a strategy's is_valid() method returns False
    but act() is called anyway.
    """

    pass


class BattleStrategy(ABC):
    """Abstract base class for battle strategies.

    Strategies define how a creature behaves during battle.
    Each strategy can validate whether it's compatible with a given creature.
    """

    @abstractmethod
    def is_valid(self, creature: "Creature") -> bool:
        """Check if this strategy is valid for the given creature.

        Args:
            creature: The creature to validate against

        Returns:
            True if the strategy can be applied, False otherwise
        """
        pass

    @abstractmethod
    def act(self, creature: "Creature") -> None:
        """Execute the strategy's actions with the given creature.

        Args:
            creature: The creature performing the actions

        Raises:
            InvalidStrategyError: If the strategy is invalid for this creature
        """
        pass


class NormalStrategy(BattleStrategy):
    """Run a Basic attack strategy valid for any creature.

    This strategy simply performs a normal attack.
    """

    def is_valid(self, creature: "Creature") -> bool:
        """Strategy is valid for all creatures.

        Args:
            creature: The creature to validate

        Returns:
            Always True
        """
        return True

    def act(self, creature: "Creature") -> None:
        """Perform a basic attack.

        Args:
            creature: The creature performing the attack
        """
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for NormalStrategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Aggressive transform-based strategy.

    This strategy transforms the creature, attacks, then reverts.
    Only valid for creatures with TransformCapability.
    """

    def is_valid(self, creature: "Creature") -> bool:
        """Check if creature has transform capability.

        Args:
            creature: The creature to validate

        Returns:
            True if creature has TransformCapability, False otherwise
        """
        from ex1.capabilities import TransformCapability
        return isinstance(creature, TransformCapability)

    def act(self, creature: "Creature") -> None:
        """Execute transform-attack-revert sequence.

        Args:
            creature: The creature performing the actions

        Raises:
            InvalidStrategyError: If creature lacks TransformCapability
        """
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for AggressiveStrategy"
            )
        from ex1.capabilities import TransformCapability
        tc = cast(TransformCapability, creature)
        print(tc.transform())
        print(creature.attack())
        print(tc.revert())


class DefensiveStrategy(BattleStrategy):
    """Defensive healing-based strategy.

    This strategy attacks first, then heals.
    Only valid for creatures with HealCapability.
    """

    def is_valid(self, creature: "Creature") -> bool:
        """
        Check if creature has healing capability.

        Args:
            creature: The creature to validate

        Returns:
            True if creature has HealCapability, False otherwise
        """
        from ex1.capabilities import HealCapability
        return isinstance(creature, HealCapability)

    def act(self, creature: "Creature") -> None:
        """Execute attack-heal sequence.

        Args:
            creature: The creature performing the actions

        Raises:
            InvalidStrategyError: If creature lacks HealCapability
        """
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for DefensiveStrategy"
            )
        from ex1.capabilities import HealCapability
        hc = cast(HealCapability, creature)
        print(creature.attack())
        print(hc.heal())
