# coding: utf-8
from abc import ABC, abstractmethod
import numbers

# region Interface


class IRule(ABC):
    """Abstract Interface Class for rules"""

    def __init__(self, key: str, name: str, value: object, raise_errors: bool, originator: object):
        """
        Constructor

        Args:
            key (str): the key that rule is to apply to.
            name (str): the name of the field that value was assigned
            value (object): the value that is assigned to ``field_name``
            raise_errors (bool): determinins if rule could raise an error when validation fails
            originator (object): the object that attributes validated for

        Raises:
            TypeError: If any arg is not of the correct type
        """
        if not isinstance(name, str):
            msg = self._get_type_error_msg(name, 'name', 'str')
            raise TypeError(msg)
        self._name: str = name

        if not isinstance(key, str):
            msg = self._get_type_error_msg(key, 'key', 'str')
            raise TypeError(msg)
        self._key: str = key

        if not isinstance(raise_errors, bool):
            msg = self._get_type_error_msg(
                raise_errors, 'raise_errors', 'bool')
            raise TypeError(msg)
        self._raise_errors = raise_errors

        self._value: object = value
        self._originator: object = originator

    # region Abstract Methods
    @abstractmethod
    def validate(self) -> bool:
        '''Gets attrib field and value are valid'''
    # endregion Abstract Methods

    def _get_type_error_msg(self, arg: object, arg_name: str, expected_type: str) -> str:
        result = f"Argument Error: '{arg_name}' is expecting type of '{expected_type}'. Got type of '{type(arg).__name__}'"
        return result
    # region Properties

    @property
    def field_name(self) -> str:
        '''
        Name of the field assigned.

        :getter: Gets the name of the field assigned
        :setter: Sets the name of the field assigned
        '''
        return self._name

    @field_name.setter
    def field_name(self, value: str):
        if not isinstance(value, str):
            msg = self._get_type_error_msg(value, 'field_name', 'str')
            raise TypeError(msg)
        self._name = value

    @property
    def field_value(self) -> object:
        """
        The value assigned to ``field_name``

        :getter: Gets value assigned to ``field_name``
        :setter: Sets value assigned to ``field_name``
        """
        return self._value

    @field_value.setter
    def field_value(self, value: object):
        self._value = value

    @property
    def key(self) -> str:
        '''Gets the key currently being read'''
        return self._key

    @key.setter
    def key(self, value: str):
        if not isinstance(value, str):
            msg = self._get_type_error_msg(value, 'key', 'str')
            raise TypeError(msg)
        self._key = value

    @property
    def raise_errors(self) -> bool:
        """
        Determines if a rule can raise an error when validation fails.

        :getter: Gets if a rule could raise an error when validation fails
        :setter: Sets if a rule could raise an error when validation fails
        """
        return self._raise_errors

    @raise_errors.setter
    def raise_errors(self, value: bool):
        if not isinstance(value, bool):
            msg = self._get_type_error_msg(value, 'raise_errors', 'bool')
            raise TypeError(msg)
        self._raise_errors = value

    @property
    def originator(self) -> object:
        '''Gets object that attributes validated for'''
        return self._originator
    # endregion Properties
# endregion Interface

# region Attrib rules


class RuleAttrNotExist(IRule):
    '''
    Rule to ensure an attribute does not exist before it is added to class.
    '''

    def validate(self) -> bool:
        """
        Validates that ``field_name`` is not an existing attribute of ``originator`` instance.

        Raises:
            AttributeError: If ``raise_errors`` is ``True`` and ``field_name`` is already an attribue of ``originator`` instance.

        Returns:
            bool: ``True`` if ``field_name`` is not an existing attribue of ``originator`` instance;
            Otherwise, ``False``.
        """
        result = not hasattr(self.originator, self.field_name)
        if result == False and self.raise_errors == True:
            raise AttributeError(
                f"'{self.field_name}' attribute already exist in current instance of '{type(self.originator).__name__}'")
        return result


class RuleAttrExist(IRule):
    '''
    Rule to ensure an attribute does exist before its value is set.
    '''

    def validate(self) -> bool:
        """
        Validates that ``field_name`` is an existing attribute of ``originator`` instance.

        Raises:
            AttributeError: If ``raise_errors`` is ``True`` and ``field_name`` is not an attribue of ``originator`` instance.

        Returns:
            bool: ``True`` if ``field_name`` is an existing attribue of ``originator`` instance;
            Otherwise, ``False``.
        """
        result = hasattr(self.originator, self.field_name)
        if result == False and self.raise_errors == True:
            raise AttributeError(
                f"'{self.field_name}' attribute does not exist in current instance of '{type(self.originator).__name__}'")
        return result
# endregion Attrib rules

# region None


class RuleNone(IRule):
    '''
    Rule that matched only if value is ``None``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign to attribute is ``None``.

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not ``None``.

        Returns:
            bool: ``True`` if ``field_value`` is ``None``; Otherwise, ``False``.
        """
        if self.field_value is not None:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: {self.key} must be assigned a value")
            return False
        return True

class RuleNotNone(IRule):
    '''
    Rule that matched only if value is not ``None``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign to attribute is not ``None``.

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is ``None``.

        Returns:
            bool: ``True`` if ``field_value`` is not ``None``; Otherwise, ``False``.
        """
        if self.field_value is None:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: {self.key} must be assigned a value")
            return False
        return True

# endregion None

# region Number


class RuleNumber(IRule):
    '''
    Rule that matched only if value is a valid number.

    Note:
        If value is a of type ``bool`` then validation will fail for this rule.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a number

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not a number.

        Returns:
            bool: ``True`` if ``field_value`` is a number; Otherwise, ``False``.
        """
        # isinstance(False, int) is True
        # print(int(True)) 1
        # print(int(False)) 0
        if not isinstance(self.field_value, numbers.Number) or isinstance(self.field_value, bool):
            if self.raise_errors:
                raise TypeError(self._get_type_error_msg(
                    self.field_value, self.key, 'Number'))
            return False
        return True

# region Integer


class RuleInt(IRule):
    '''
    Rule that matched only if value is instance of ``int``.

    Note:
        If value is a of type ``bool`` then validation will fail for this rule.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is an int

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not an int.

        Returns:
            bool: ``True`` if ``field_value`` is an ``int``; Otherwise, ``False``.
        """
        # isinstance(False, int) is True
        # print(int(True)) 1
        # print(int(False)) 0
        if not isinstance(self.field_value, int) or isinstance(self.field_value, bool):
            if self.raise_errors:
                raise TypeError(self._get_type_error_msg(
                    self.field_value, self.key, 'int'))
            return False
        return True


class RuleIntZero(RuleInt):
    '''
    Rule that matched only if value is equal to ``0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is equal to ``0`` int.

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not equal to ``0`` int.

        Returns:
            bool: ``True`` if ``field_value`` equals ``0`` int; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value != 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be equal to 0 int value")
            return False
        return True

class RuleIntPositive(RuleInt):
    '''
    Rule that matched only if value is equal or greater than ``0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a posivite int

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not a positive int.

        Returns:
            bool: ``True`` if ``field_value`` is a positive int; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value < 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be a positive int value")
            return False
        return True


class RuleIntNegative(RuleInt):
    '''
    Rule that matched only if value is less than ``0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a negative int

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not a negative int.

        Returns:
            bool: ``True`` if ``field_value`` is a negative int; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value >= 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be a negative int value")
            return False
        return True


class RuleIntNegativeOrZero(RuleInt):
    '''
    Rule that matched only if value is equal or less than ``0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is equal to zero or a negative int

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not a negative int.

        Returns:
            bool: ``True`` if ``field_value`` is equal to zero or a negative int; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value > 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be equal to zero or a negative int value")
            return False
        return True
# endregion Integer

# region Float Rules


class RuleFloat(IRule):
    '''
    Rule that matched only if value is to type ``float``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a float

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not a float.

        Returns:
            bool: ``True`` if ``field_value`` is a positive float; Otherwise, ``False``.
        """
        if not isinstance(self.field_value, float):
            if self.raise_errors:
                raise TypeError(self._get_type_error_msg(
                    self.field_value, self.key, 'float'))
            return False
        return True


class RuleFloatZero(RuleFloat):
    '''
    Rule that matched only if value is equal to ``0.0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign equals ``0.0`` float

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not equal to ``0.0`` float.

        Returns:
            bool: ``True`` if ``field_value`` equals ``0.0`` float; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value != 0.0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be equal to 0.0 float value")
            return False
        return True

class RuleFloatPositive(RuleFloat):
    '''
    Rule that matched only if value is equal or greater than ``0.0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a positive float

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not a positive float.

        Returns:
            bool: ``True`` if ``field_value`` is a positive float; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value < 0.0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be a positive float value")
            return False
        return True


class RuleFloatNegative(RuleFloat):
    '''
    Rule that matched only if value is less than ``0.0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a negative float

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not a negative float.

        Returns:
            bool: ``True`` if ``field_value`` is a negative float; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value >= 0.0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be a negative float value")
            return False
        return True


class RuleFloatNegativeOrZero(RuleFloat):
    '''
    Rule that matched only if value is equal or less than ``0.0``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is equal to ``0.0`` or a negative float

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not a negative float.

        Returns:
            bool: ``True`` if ``field_value`` is equal to ``0.0`` or a negative float; Otherwise, ``False``.
        """
        if not super().validate():
            return False
        if self.field_value > 0.0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be equal to 0.0 or a negative float value")
            return False
        return True
# endregion Float Rules

# endregion Number

# region String


class RuleStr(IRule):
    '''
    Rule that matched only if value is of type ``str``.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a string

        Raises:
            TypeError: If ``raise_errors`` is ``True`` and ``field_value`` is not instance of string.

        Returns:
            bool: ``True`` if ``field_value`` is a string; Otherwise, ``False``.
        """
        if not isinstance(self.field_value, str):
            if self.raise_errors:
                raise TypeError(self._get_type_error_msg(
                    self.field_value, self.key, 'str'))
            return False
        return True


class RuleStrEmpty(RuleStr):
    '''
    Rule that matched only if value is equal to empty string.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a string and is an empty string.

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value``
                is not an empty string.

        Returns:
            bool: ``True`` if value is an empty string; Otherwise; ``False``.
        """
        if not super().validate():
            return False
        value = self.field_value
        if len(value) != 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: {self.key} must be empty str")
            return False
        return True


class RuleStrNotNullOrEmpty(RuleStr):
    '''
    Rule that matched only if value is not ``None`` or empty string.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a string and is not a empty string.

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value``
                is not instance of string or is empty string

        Returns:
            bool: ``True`` if value is valid; Otherwise; ``False``.
        """
        if not super().validate():
            return False
        value = self.field_value
        if len(value) == 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: {self.key} must not be empty str")
            return False
        return True


class RuleStrNotNullEmptyWs(RuleStrNotNullOrEmpty):
    '''
    Rule that matched only if value is not ``None``, empty or whitespace.
    '''

    def validate(self) -> bool:
        """
        Validates that value to assign is a string and is not a empty or whitespace string.

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value``
                is not instance of string or is empty or whitespace string

        Returns:
            bool: ``True`` if value is valid; Otherwise; ``False``.
        """
        if not super().validate():
            return False
        value = self.field_value.strip()
        if len(value) == 0:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must not be empty or whitespace str")
            return False
        return True
# endregion String

# region boolean


class RuleBool(IRule):
    """
     Rule that matched only if value is instance of bool.
    """

    def validate(self) -> bool:
        """
        Validates that value to assign is a bool

        Raises:
            ValueError: If ``raise_errors`` is ``True`` and ``field_value`` is not instance of bool.

        Returns:
            bool: ``True`` if ``field_value`` is a bool; Otherwise, ``False``.
        """
        if not isinstance(self.field_value, bool):
            if self.raise_errors:
                raise TypeError(self._get_type_error_msg(
                    self.field_value, self.key, 'bool'))
            return False
        return True
# endregion boolean
