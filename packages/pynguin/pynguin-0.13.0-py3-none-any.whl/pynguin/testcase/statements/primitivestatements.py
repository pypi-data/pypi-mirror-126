#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2021 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
"""Provides primitive statements."""
from __future__ import annotations

import math
from abc import abstractmethod
from typing import TYPE_CHECKING, Dict, Generic, List, Optional, Set, Type, TypeVar

import pynguin.configuration as config
import pynguin.testcase.statements.statement as stmt
import pynguin.testcase.variable.variablereferenceimpl as vri
from pynguin.analyses.seeding.constantseeding import (
    dynamic_constant_seeding,
    static_constant_seeding,
)
from pynguin.utils import randomness
from pynguin.utils.generic.genericaccessibleobject import (
    GenericAccessibleObject,
    GenericEnum,
)

if TYPE_CHECKING:
    import pynguin.testcase.statements.statementvisitor as sv
    import pynguin.testcase.testcase as tc
    import pynguin.testcase.variable.variablereference as vr

# pylint:disable=invalid-name
T = TypeVar("T")


class PrimitiveStatement(Generic[T], stmt.Statement):
    """Abstract primitive statement which holds a value."""

    def __init__(
        self,
        test_case: tc.TestCase,
        variable_type: Optional[Type],
        value: Optional[T] = None,
    ) -> None:
        super().__init__(test_case, vri.VariableReferenceImpl(test_case, variable_type))
        self._value = value
        if value is None:
            self.randomize_value()

    @property
    def value(self) -> Optional[T]:
        """Provides the primitive value of this statement.

        Returns:
            The primitive value
        """
        return self._value

    @value.setter
    def value(self, value: T) -> None:
        self._value = value

    def accessible_object(self) -> Optional[GenericAccessibleObject]:
        return None

    def mutate(self) -> bool:
        old_value = self._value
        while self._value == old_value and self._value is not None:
            if (
                randomness.next_float()
                < config.configuration.search_algorithm.random_perturbation
            ):
                self.randomize_value()
            else:
                self.delta()
        return True

    def get_variable_references(self) -> Set[vr.VariableReference]:
        return {self.ret_val}

    def replace(self, old: vr.VariableReference, new: vr.VariableReference) -> None:
        if self.ret_val == old:
            self.ret_val = new

    @abstractmethod
    def randomize_value(self) -> None:
        """Randomize the primitive value of this statement."""

    @abstractmethod
    def delta(self) -> None:
        """Add a random delta to the value."""

    def __repr__(self) -> str:
        return (
            f"PrimitiveStatement({self._test_case}, {self._ret_val}, "
            + f"{self._value})"
        )

    def __str__(self) -> str:
        return f"{self._value}: {self._ret_val}"

    def structural_eq(
        self,
        other: stmt.Statement,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return (
            self._ret_val.structural_eq(other._ret_val, memo)
            and self._value == other._value
        )

    def structural_hash(self) -> int:
        return 31 + self._ret_val.structural_hash() + hash(self._value)


class IntPrimitiveStatement(PrimitiveStatement[int]):
    """Primitive Statement that creates an int."""

    def __init__(self, test_case: tc.TestCase, value: Optional[int] = None) -> None:
        super().__init__(test_case, int, value)

    def randomize_value(self) -> None:
        use_seed = (
            randomness.next_float()
            <= config.configuration.seeding.seeded_primitives_reuse_probability
        )
        if (
            config.configuration.seeding.dynamic_constant_seeding
            and dynamic_constant_seeding.has_ints
            and use_seed
            and config.configuration.seeding.constant_seeding
            and randomness.next_float()
            <= config.configuration.seeding.seeded_dynamic_values_reuse_probability
        ):
            self._value = dynamic_constant_seeding.random_int
        elif (
            config.configuration.seeding.constant_seeding
            and static_constant_seeding.has_ints
            and use_seed
        ):
            self._value = static_constant_seeding.random_int
        else:
            self._value = int(
                randomness.next_gaussian() * config.configuration.test_creation.max_int
            )

    def delta(self) -> None:
        assert self._value is not None
        delta = math.floor(
            randomness.next_gaussian() * config.configuration.test_creation.max_delta
        )
        self._value += delta

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return IntPrimitiveStatement(test_case, self._value)

    def __repr__(self) -> str:
        return f"IntPrimitiveStatement({self._test_case}, {self._value})"

    def __str__(self) -> str:
        return f"{self._value}: int"

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_int_primitive_statement(self)


class FloatPrimitiveStatement(PrimitiveStatement[float]):
    """Primitive Statement that creates a float."""

    def __init__(self, test_case: tc.TestCase, value: Optional[float] = None) -> None:
        super().__init__(test_case, float, value)

    def randomize_value(self) -> None:
        use_seed = (
            randomness.next_float()
            <= config.configuration.seeding.seeded_primitives_reuse_probability
        )
        if (
            config.configuration.seeding.dynamic_constant_seeding
            and dynamic_constant_seeding.has_floats
            and use_seed
            and config.configuration.seeding.constant_seeding
            and randomness.next_float()
            <= config.configuration.seeding.seeded_dynamic_values_reuse_probability
        ):
            self._value = dynamic_constant_seeding.random_float
        elif (
            config.configuration.seeding.constant_seeding
            and static_constant_seeding.has_floats
            and use_seed
        ):
            self._value = static_constant_seeding.random_float
        else:
            val = (
                randomness.next_gaussian() * config.configuration.test_creation.max_int
            )
            precision = randomness.next_int(0, 7)
            self._value = round(val, precision)

    def delta(self) -> None:
        assert self._value is not None
        probability = randomness.next_float()
        if probability < 1.0 / 3.0:
            self._value += (
                randomness.next_gaussian()
                * config.configuration.test_creation.max_delta
            )
        elif probability < 2.0 / 3.0:
            self._value += randomness.next_gaussian()
        else:
            self._value = round(self._value, randomness.next_int(0, 7))

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return FloatPrimitiveStatement(test_case, self._value)

    def __repr__(self) -> str:
        return f"FloatPrimitiveStatement({self._test_case}, {self._value})"

    def __str__(self) -> str:
        return f"{self._value}: float"

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_float_primitive_statement(self)


class StringPrimitiveStatement(PrimitiveStatement[str]):
    """Primitive Statement that creates a String."""

    def __init__(self, test_case: tc.TestCase, value: Optional[str] = None) -> None:
        super().__init__(test_case, str, value)

    def randomize_value(self) -> None:
        use_seed = (
            randomness.next_float()
            <= config.configuration.seeding.seeded_primitives_reuse_probability
        )
        if (
            config.configuration.seeding.dynamic_constant_seeding
            and dynamic_constant_seeding.has_strings
            and use_seed
            and config.configuration.seeding.constant_seeding
            and randomness.next_float()
            <= config.configuration.seeding.seeded_dynamic_values_reuse_probability
        ):
            self._value = dynamic_constant_seeding.random_string
        elif (
            config.configuration.seeding.constant_seeding
            and static_constant_seeding.has_strings
            and use_seed
        ):
            self._value = static_constant_seeding.random_string
        else:
            length = randomness.next_int(
                0, config.configuration.test_creation.string_length + 1
            )
            self._value = randomness.next_string(length)

    def delta(self) -> None:
        assert self._value is not None
        working_on = list(self._value)
        p_perform_action = 1.0 / 3.0
        if randomness.next_float() < p_perform_action and len(working_on) > 0:
            working_on = self._random_deletion(working_on)

        if randomness.next_float() < p_perform_action and len(working_on) > 0:
            working_on = self._random_replacement(working_on)

        if randomness.next_float() < p_perform_action:
            working_on = self._random_insertion(working_on)

        self._value = "".join(working_on)

    @staticmethod
    def _random_deletion(working_on: List[str]) -> List[str]:
        p_per_char = 1.0 / len(working_on)
        return [char for char in working_on if randomness.next_float() >= p_per_char]

    @staticmethod
    def _random_replacement(working_on: List[str]) -> List[str]:
        p_per_char = 1.0 / len(working_on)
        return [
            randomness.next_char() if randomness.next_float() < p_per_char else char
            for char in working_on
        ]

    @staticmethod
    def _random_insertion(working_on: List[str]) -> List[str]:
        pos = 0
        if len(working_on) > 0:
            pos = randomness.next_int(0, len(working_on) + 1)
        alpha = 0.5
        exponent = 1
        while (
            randomness.next_float() <= pow(alpha, exponent)
            and len(working_on) < config.configuration.test_creation.string_length
        ):
            exponent += 1
            working_on = working_on[:pos] + [randomness.next_char()] + working_on[pos:]
        return working_on

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return StringPrimitiveStatement(test_case, self._value)

    def __repr__(self) -> str:
        return f"StringPrimitiveStatement({self._test_case}, {self._value})"

    def __str__(self) -> str:
        return f"{self._value}: str"

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_string_primitive_statement(self)


class BytesPrimitiveStatement(PrimitiveStatement[bytes]):
    """Primitive Statement that creates bytes."""

    def __init__(self, test_case: tc.TestCase, value: Optional[bytes] = None) -> None:
        super().__init__(test_case, bytes, value)

    def randomize_value(self) -> None:
        length = randomness.next_int(
            0, config.configuration.test_creation.bytes_length + 1
        )
        self._value = randomness.next_bytes(length)

    def delta(self) -> None:
        assert self._value is not None
        working_on = list(self._value)
        p_perform_action = 1.0 / 3.0
        if randomness.next_float() < p_perform_action and len(working_on) > 0:
            working_on = self._random_deletion(working_on)

        if randomness.next_float() < p_perform_action and len(working_on) > 0:
            working_on = self._random_replacement(working_on)

        if randomness.next_float() < p_perform_action:
            working_on = self._random_insertion(working_on)

        self._value = bytes(working_on)

    @staticmethod
    def _random_deletion(working_on: List[int]) -> List[int]:
        p_per_char = 1.0 / len(working_on)
        return [char for char in working_on if randomness.next_float() >= p_per_char]

    @staticmethod
    def _random_replacement(working_on: List[int]) -> List[int]:
        p_per_char = 1.0 / len(working_on)
        return [
            randomness.next_byte() if randomness.next_float() < p_per_char else byte
            for byte in working_on
        ]

    @staticmethod
    def _random_insertion(working_on: List[int]) -> List[int]:
        pos = 0
        if len(working_on) > 0:
            pos = randomness.next_int(0, len(working_on) + 1)
        alpha = 0.5
        exponent = 1
        while (
            randomness.next_float() <= pow(alpha, exponent)
            and len(working_on) < config.configuration.test_creation.bytes_length
        ):
            exponent += 1
            working_on = working_on[:pos] + [randomness.next_byte()] + working_on[pos:]
        return working_on

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return BytesPrimitiveStatement(test_case, self._value)

    def __repr__(self) -> str:
        return f"BytesPrimitiveStatement({self._test_case}, {self._value!r})"

    def __str__(self) -> str:
        return f"{self._value!r}: bytes"

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_bytes_primitive_statement(self)


class BooleanPrimitiveStatement(PrimitiveStatement[bool]):
    """Primitive Statement that creates a boolean."""

    def __init__(self, test_case: tc.TestCase, value: Optional[bool] = None) -> None:
        super().__init__(test_case, bool, value)

    def randomize_value(self) -> None:
        self._value = bool(randomness.RNG.getrandbits(1))

    def delta(self) -> None:
        assert self._value is not None
        self._value = not self._value

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return BooleanPrimitiveStatement(test_case, self._value)

    def __repr__(self) -> str:
        return f"BooleanPrimitiveStatement({self._test_case}, {self._value})"

    def __str__(self) -> str:
        return f"{self._value}: bool"

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_boolean_primitive_statement(self)


class EnumPrimitiveStatement(PrimitiveStatement[int]):
    """Primitive Statement that references the value of an enum.
    We simply store the index of the element in the Enum."""

    def __init__(
        self,
        test_case: tc.TestCase,
        generic_enum: GenericEnum,
        value: Optional[int] = None,
    ):
        self._generic_enum = generic_enum
        super().__init__(test_case, generic_enum.generated_type(), value)

    def accessible_object(self) -> GenericEnum:
        return self._generic_enum

    @property
    def value_name(self) -> str:
        """Convenience method to access the enum name that is associated with
        the stored index.

        Returns:
            The associated enum value."""
        assert self._value is not None
        return self._generic_enum.names[self._value]

    def randomize_value(self) -> None:
        self._value = randomness.next_int(0, len(self._generic_enum.names))

    def delta(self) -> None:
        assert self._value is not None
        self._value += randomness.choice([-1, 1])
        self._value = (self._value + len(self._generic_enum.names)) % len(
            self._generic_enum.names
        )

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return EnumPrimitiveStatement(test_case, self._generic_enum, value=self.value)

    def __repr__(self) -> str:
        return f"EnumPrimitiveStatement({self._test_case}, {self._value})"

    def __str__(self) -> str:
        return f"{self.value_name}: Enum"

    def structural_eq(
        self,
        other: stmt.Statement,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> bool:
        return (
            super().structural_eq(other, memo)
            and isinstance(other, EnumPrimitiveStatement)
            and other._generic_enum == self._generic_enum
        )

    def structural_hash(self) -> int:
        return hash((super().structural_hash(), self._generic_enum))

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_enum_statement(self)


class NoneStatement(PrimitiveStatement):
    """A statement serving as a None reference."""

    def clone(
        self,
        test_case: tc.TestCase,
        memo: Dict[vr.VariableReference, vr.VariableReference],
    ) -> stmt.Statement:
        return NoneStatement(test_case, self.ret_val.variable_type)

    def accept(self, visitor: sv.StatementVisitor) -> None:
        visitor.visit_none_statement(self)

    def randomize_value(self) -> None:
        pass

    def delta(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"NoneStatement({self._test_case})"

    def __str__(self) -> str:
        return "None"
