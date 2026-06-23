"""Battle simulation script for DataDeck creature testing.

This script demonstrates the use of the abstract factory pattern
by creating creatures through factories and simulating battles
between different creature families.
"""

from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory,
                 base_name: str,
                 evolved_name: str
                 ) -> None:
    """
    Test a creature factory by creating and using its creatures.

    Args:
        factory: The CreatureFactory instance to test
        base_name: Name for the base creature
        evolved_name: Name for the evolved creature
    """
    print("Testing factory")
    base = factory.create_base(base_name)
    evolved = factory.create_evolved(evolved_name)
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle_factories(f1: CreatureFactory,
                     f2: CreatureFactory,
                     n1: str,
                     n2: str
                     ) -> None:
    """
    Simulate a battle between creatures from two different factories.

    Args:
        f1: First creature factory
        f2: Second creature factory
        n1: Name for creature from first factory
        n2: Name for creature from second factory
    """
    print("Testing battle")
    c1 = f1.create_base(n1)
    c2 = f2.create_base(n2)
    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    """Run Main function.

    Running the creature factory tests and battle simulation.
    """
    ff = FlameFactory()
    af = AquaFactory()
    test_factory(ff, "Flameling", "Pyrodon")
    test_factory(af, "Aquabub", "Torragon")
    battle_factories(ff, af, "Flameling", "Aquabub")


if __name__ == "__main__":
    main()
