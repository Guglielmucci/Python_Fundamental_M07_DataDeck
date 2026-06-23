"""
DataDeck Game - Battle Strategy Package.

This package implements the Strategy pattern for creature battles,
allowing different battle behaviors to be applied to creatures
based on their capabilities.

Exports:
    BattleStrategy: Abstract base class for battle strategies
    NormalStrategy: Basic attack-only strategy
    AggressiveStrategy: Transform-attack-revert strategy
    DefensiveStrategy: Attack-heal strategy
    InvalidStrategyError: Exception for invalid creature-strategy combinations
"""

from .strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)

__all__ = [
    "BattleStrategy",
    "NormalStrategy",
    "AggressiveStrategy",
    "DefensiveStrategy",
    "InvalidStrategyError",
]
