"""Tournament script for creature battles.

This script demonstrates the Strategy pattern by organizing tournaments
where creatures battle using different strategies based on their capabilities.

Tournaments are round-robin: each creature fights every other creature once.
"""

from typing import List, Tuple
from ex0.factory import CreatureFactory
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    BattleStrategy,
    InvalidStrategyError,
)


def battle(
    opponent1: Tuple[CreatureFactory, BattleStrategy, str],
    opponent2: Tuple[CreatureFactory, BattleStrategy, str],
) -> None:
    """Simulate a single battle between two opponents.

    Each opponent is defined as a tuple containing:
    - A CreatureFactory to create the creature
    - A BattleStrategy to determine battle behavior
    - A name for the creature

    Args:
        opponent1: First opponent (factory, strategy, name)
        opponent2: Second opponent (factory, strategy, name)

    Raises:
        InvalidStrategyError: If a strategy is invalid for its creature
    """
    factory1, strategy1, name1 = opponent1
    factory2, strategy2, name2 = opponent2

    creature1 = factory1.create_base(name1)
    creature2 = factory2.create_base(name2)

    # Validate strategies
    if not strategy1.is_valid(creature1):
        raise InvalidStrategyError(
            f"Invalid Creature '{creature1.name}' "
            f"for this {strategy1.__class__.__name__.lower()}"
        )
    if not strategy2.is_valid(creature2):
        raise InvalidStrategyError(
            f"Invalid Creature '{creature2.name}' "
            f"for this {strategy2.__class__.__name__.lower()}"
        )

    # Display battle
    print("* Battle *")
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" now fight!")
    strategy1.act(creature1)
    strategy2.act(creature2)


def run_tournament(
    opponents: List[Tuple[CreatureFactory, BattleStrategy, str]]
) -> None:
    """Run a round-robin tournament.

    where each opponent fights every other once. If an
    InvalidStrategyError occurs, the tournament is aborted.

    Args:
        opponents: List of opponents (factory, strategy, name)
    """
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                battle(opponents[i], opponents[j])
                print()
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    """Run Main function.

    Run all tournament demonstrations.
    """
    try:
        # --------------------------------------------------------------
        # Tournament 0 (basic) - Valid combinations
        # --------------------------------------------------------------
        print("Tournament 0 (basic)")
        print("[ (Flameling+Normal), (Healing+Defensive) ]")
        opponents0 = [
            (FlameFactory(), NormalStrategy(), "Flameling"),
            (HealingCreatureFactory(), DefensiveStrategy(), "Sproutling"),
        ]
        run_tournament(opponents0)
        print()

        # --------------------------------------------------------------
        # Tournament 1 (error) - Invalid combination
        # --------------------------------------------------------------
        print("Tournament 1 (error)")
        print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
        opponents1 = [
            (FlameFactory(), AggressiveStrategy(), "Flameling"),
            (HealingCreatureFactory(), DefensiveStrategy(), "Sproutling"),
        ]
        run_tournament(opponents1)
        print()

        # --------------------------------------------------------------
        # Tournament 2 (multiple) - Three opponents
        # --------------------------------------------------------------
        print("Tournament 2 (multiple)")
        print("[ (Aquabub+Normal), (Healing+Defensive),"
              " (Transform+Aggressive) ]")
        opponents2 = [
            (AquaFactory(), NormalStrategy(), "Aquabub"),
            (HealingCreatureFactory(), DefensiveStrategy(), "Sproutling"),
            (TransformCreatureFactory(), AggressiveStrategy(), "Shiftling"),
        ]
        run_tournament(opponents2)

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
