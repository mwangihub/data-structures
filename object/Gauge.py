import abc
import copy

# R-2.4



class Flower:
    def __init__(self, name=None, no_petals=None, price=None):
        self._name = name
        self._no_petals = no_petals
        self._price = price

    def _set_name(self, f_name):
        self._name = f_name

    def get_name(self):
        return self._name


if __name__ == "__main__":
    flower = Flower()
    print(flower.get_name())


# R-2.15
class Vector:
    """Represent a vector in multidimensional space"""
    def __init__(self, data):
        """Create d-dimensional vector of zeros"""
        try:
            iter(data)
            copy_data = copy.deepcopy(list(data))
            for i in copy_data:
                if not isinstance(i, (int, float)):
                    raise TypeError('Iterable must contain sequence of numbers only.')
            self._coords = copy_data
        except TypeError:
            if isinstance(data, int):
                self._coords = [0] * data
            else:
                raise TypeError('Arg passed must be an iterable of numbers or int')
