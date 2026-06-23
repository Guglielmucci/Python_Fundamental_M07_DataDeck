"""
Abstract capability classes for creatures.

This module defines the abstract base classes for special capabilities
that can be mixed into creatures through multiple inheritance.

Classes:
    HealCapability: Abstract class for healing abilities
    TransformCapability: Abstract class for transformation abilities
"""

from abc import ABC, abstractmethod
from typing import Optional


class HealCapability(ABC):
    """
    Abstract base class for creatures with healing abilities.

    Classes inheriting from HealCapability must implement the heal method.
    """

    @abstractmethod
    def heal(self, target: Optional[str] = None) -> str:
        """
        Heal the creature or an optional target.

        Args:
            target: Optional target to heal (if None, heals self)

        Returns:
            A string describing the healing action
        """
        pass


class TransformCapability(ABC):
    """
    Abstract base class for creatures with transformation abilities.

    Classes inheriting from TransformCapability can change form,
    which affects their attack power. The transformation state
    is persistent and tracked internally.

    Attributes:
        _transformed (bool): Internal flag tracking transformation state
    """

    def __init__(self) -> None:
        """Initialize the transform capability with normal state."""
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """
        Transform the creature into a more powerful form.

        Returns:
            A string describing the transformation action
        """
        pass

    @abstractmethod
    def revert(self) -> str:
        """
        Revert the creature back to its normal form.

        Returns:
            A string describing the reversion action
        """
        pass

    def is_transformed(self) -> bool:
        """
        Check if the creature is currently transformed.

        Returns:
            True if transformed, False otherwise
        """
        return self._transformed
