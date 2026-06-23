"""
DataDeck Game - Creature Capabilities Package.

This package extends the creature factory system with special capabilities:
- HealingCapability: Allows creatures to heal themselves and others
- TransformCapability: Allows creatures to transform and change attack power

Exports:
    HealingCreatureFactory: Factory for creatures with healing capability
    TransformCreatureFactory: Factory for creatures with transform capability
"""

from .factories import HealingCreatureFactory, TransformCreatureFactory

__all__ = ["HealingCreatureFactory", "TransformCreatureFactory"]
