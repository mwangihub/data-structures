""" Class definition """
from typing import Type

'''Definitions'''


class CreditCard:
    _account: str
    _bank: str
    _customer: str
    _limit: int
    __name__ = 'Credit Card Example'
    __slots__ = '_customer', '_bank', '_account', '_limit'

    def __init__(self, customer=None, bank=None, account=None, limit=0):
        """ Encapsulation - using underscores to prevent inner variables. """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit

    def print_values(self):
        print(self._customer, self._bank, self._account, self._limit)

    def charge(self, price):
        pass


class PredatoryCreditCard(CreditCard):
    OVER_LIMIT_FEE = 5  # this is a class-level member

    def __init__(self, customer=None, bank=None, account=None, limit=0):
        super().__init__(customer, bank, account, limit)
        self.balance = None

    def charge(self, price):
        success = super().charge(price)
        if not success:
            # self.balance += self.OVER_LIMIT_FEE
            self.balance += PredatoryCreditCard.OVER_LIMIT_FEE
        return success


''' Iterators'''


class SequenceIterators:
    def __int__(self, sequence):
        """Keeping counter to -1 so that it starts 0 with first count"""
        self._sequence = sequence
        self._counter = -1

    def __next__(self):
        """Called when calling __iter__"""
        self._counter += 1
        if not self._counter < len(self._sequence):
            raise StopIteration()
        return self._sequence[self._counter]

    def __iter__(self):
        return self


''' 1. Class operator overloading '''


class OperatorOverload:
    def __init__(self, x):
        self.x = x

    def __add__(self, other_class):
        return self.x + other_class.x


def example_of_overload(v1=0, v2=0):
    obj: Type[OperatorOverload] = OperatorOverload
    var_1: OperatorOverload = obj(10) if not v1 else obj(v1)
    var_2: OperatorOverload = obj(10) if not v2 else obj(v2)
    print(var_1 + var_2)


''' 2. Class operator overloading (Using vectors) '''


class Vector:
    def __init__(self, coords):
        """ creates a vector with dimensions of `coords` filled with zeros """
        self._coords = list(range(1, coords + 1))

    def __len__(self):
        return len(self._coords)

    def __eq__(self, other):
        return self._coords == other._coords

    def __setitem__(self, j, val):
        self._coords[j] = val

    # >>> 438568
    def __getitem__(self, j):
        return self._coords[j]

    def __add__(self, other):
        if not len(self) == len(other):  # self.__eq__(self):
            print('Dimensions must agree. i.e be equivalent')
            return
        result = Vector(len(self))
        for j in range(len(self)):
            print(self[j])
            result[j] = self[j] + other[j]
        return result

    def __str__(self):
        return f"< {str(self._coords)} >"


def example_of_overload_vector():
    var1 = Vector(3)
    var2 = Vector(3)
    print("Adding vectors: ", var2 + var1)


''' 4. Class Numeric progression  '''

""" Class Inheritance """


class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def progression(self, length):
        for i in range(length):
            print((next(self)), end=" - ")
        # print(' - '.join(str(next(self)) for i in range(length)))


'''
    Arithmetic progression adds a fixed constant to one term of the progression to produce the next.\n
    For example, using an increment of 4 for an arithmetic progression that starts at 0\n
    results in the sequence 0, 4, 8, 12, . . . .
'''


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


'''
    In geometric progression, each value is produced by multiplying the preceding value by a fixed \n
    constant, known as the base of the geometric progression. The starting point of a \n
    geometric progression is traditionally 1, rather than 0, because multiplying 0 by any \n
    factor results in 0. As an example, a geometric progression with base 2 proceeds as
    1, 2, 4, 8, 16, . . . .
'''


class GeometricProgression(Progression):

    def __init__(self, base=1, start=0):
        super().__init__(start)
        self._base = base

    def _advance(self):
        """ i.e self._current = self._current * self._base """
        self._current *= self._base


'''
Each value of a Fibonacci series is the
sum of the two most recent values. To begin the series, the first two values are
conventionally 0 and 1, leading to the Fibonacci series 0, 1, 1, 2, 3, 5, 8, . . . . More
generally, such a series can be generated from any two starting values. For example,
if we start with values 4 and 6, the series proceeds as 4, 6, 10, 16, 26, 42, . . . 
'''


class FibonacciProgression(Progression):
    """
    Fibonacci must have two values first
    0725 795811
    To get next number add last two
    To get current number minus the current two numbers
    """

    def __init__(self, first_number=0, next_number=1):
        super().__init__(first_number)
        self._prev_number = next_number - first_number

    def _advance(self):
        # self._prev_number, self._current = self._current, self._prev_number + self._current
        current = self._current
        self._current = self._prev_number + self._current
        self._prev_number = current


''' Abstract methods. '''
from abc import ABCMeta, ABC, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, index):
        """Return the element at index `index` of the item"""

    def __contains__(self, item):
        for i in range(len(self)):
            if not self[i] == item:
                return False
            return True


class InformalParserInterface:

    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass


class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation."""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        __check_implemented__ = (
                hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text)
        )
        return __check_implemented__


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """
    This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """


class Animal(ABC):
    def __init__(self):
        self._food = None

    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abstractmethod
    def diet(self):
        """Set diet of the animal"""

    @abstractmethod
    def feed(self, time):
        """Implement feeding"""


class Lion(Animal, InformalParserInterface):
    @property
    def diet(self):
        return ["antelope", "cheetah", "buffalo"]

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}")


class TestingAbstractClasses:
    def run(self):
        self.__slots__ = ''
        lion = Lion()
        lion.food_eaten = "antelope"
        return lion.feed("0000 Hrs")


if __name__ == "__main__":
    # example_of_overload()
    # example_of_overload_vector()
    # Progression(3).progression(10)
    # ArithmeticProgression(2, 3).progression(10)
    # GeometricProgression(2, 3).progression(10)
    # FibonacciProgression(4, 6).progression(3)
    TestingAbstractClasses().run()
