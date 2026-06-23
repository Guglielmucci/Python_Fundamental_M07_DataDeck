"""
Capacitor - Test script for creature capabilities.

This script demonstrates the use of creatures with special capabilities:
- Healing creatures can heal themselves
- Transform creatures can change form to boost attacks

It tests both base and evolved versions of each creature type.
"""

from typing import cast
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory() -> None:
    """
    Test the healing creature factory.

    Creates base and evolved healing creatures and demonstrates
    their describe, attack, and heal methods.
    """
    print("Testing Creature with healing capability")
    try:
        heal_factory = HealingCreatureFactory()
        base = heal_factory.create_base("Sproutling")
        evolved = heal_factory.create_evolved("Bloomelle")

        print(" base:")
        print(base.describe())
        print(base.attack())
        print(cast(HealCapability, base).heal())
        print(" evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(cast(HealCapability, evolved).heal())
        print()
    except Exception as e:
        print(f"Error testing healing factory: {e}")


def test_transform_factory() -> None:
    """
    Test the transform creature factory.

    Creates base and evolved transform creatures and demonstrates
    their describe, attack, transform, and revert methods.
    """
    print("Testing Creature with transform capability")
    try:
        trans_factory = TransformCreatureFactory()
        base = trans_factory.create_base("Shiftling")
        evolved = trans_factory.create_evolved("Morphagon")

        print(" base:")
        print(base.describe())
        print(base.attack())
        print(cast(TransformCapability, base).transform())
        print(base.attack())
        print(cast(TransformCapability, base).revert())
        print(" evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(cast(TransformCapability, evolved).transform())
        print(evolved.attack())
        print(cast(TransformCapability, evolved).revert())
    except Exception as e:
        print(f"Error testing transform factory: {e}")


def main() -> None:
    """Run Main function.

    Main function to run all capability tests.
    """
    try:
        test_healing_factory()
        test_transform_factory()
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
