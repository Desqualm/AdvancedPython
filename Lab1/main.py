#zadanie 1

class Figure:

    def __init__(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")
    def get_area(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")
    def get_circumferenc(self):
        raise NotImplementedError("Należy zaimplementować tę metodę")


class Square(Figure):
    """ Klasa do obsługi figury typu kwadrat"""

    def __init__(self, side=1):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def __str__(self) -> str:
        return f"Square({self.side})"

    def __add__(self, other):
        import math
        if isinstance(other, type(self)):
            new_side = math.sqrt(self.side ** 2 + other.side ** 2)
            return type(self)(new_side)
        elif isinstance(other, int):
            new_side = math.sqrt(self.side ** 2 + other ** 2)
            return type(self)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

    def __iadd__(self, other):
        import math
        if isinstance(other, type(self)):
            new_side = math.sqrt(self.side ** 2 + other.side ** 2)
            return type(self)(new_side)
        elif isinstance(other, int):
            new_side = math.sqrt(self.side ** 2 + other ** 2)
            return type(self)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )

    def __radd__(self, other):
        import math
        if isinstance(other, int):
            new_side = math.sqrt(self.side ** 2 + other ** 2)
            return type(self)(new_side)

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.side == other.side
        return False

# test do zadania 1
if __name__ == "__main__":
    s = Square()
    s2 = Square(5)
    print(s2.get_area())
    print(s.get_area())

    x = 6
    y = 3.3

    print("Typ zmiennej x to:", type(x))
    print("Typ zmiennej y to:", type(y))
    print(s.get_area())
    print(s.__radd__(x))
    print(s.__add__(x))
    print(s.__iadd__(x))
    print(s.side)

# zadanie 2

class Square(Figure):
    """ Klasa do obsługi figury typu kwadrat"""

    def __init__(self, side=1):
        self.side = side

    def __str__(self) -> str:
        return f"Square({self.side})"

    def __add__(this, other):
        import math
        if isinstance(other, type(this)):
            new_side = math.sqrt(this.side ** 2 + other.side ** 2)
            return type(this)(new_side)
        else:
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(this).__name__}' and '{type(other).__name__}'"
            )

    def __mul__(self, scale: int | float):
        return Square(self.side * scale)

    def __truediv__(self, scale: int | float):
        return Square(self.side / scale)

    def __eq__(self, other):
        if isinstance(other, Square):
            # lub
            # if isinstance(other, type(self)):
            return self.side == other.side
        return False

    def get_circumferenc(self):
        import math
        return self.side * 4

    def __gt__(self, other):
        return self.get_circumferenc() > other.get_circumferenc()

    def __lt__(self, other):
        return self.get_circumferenc() < other.get_circumferenc()

class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius

    def get_circumferenc(self):
        import math
        return 2 * math.pi * self.radius

    def __gt__(self, other):
        return self.get_circumferenc() > other.get_circumferenc()

    def __lt__(self, other):
        return self.get_circumferenc() < other.get_circumferenc()

# test do zadania 2

s = Square(7)
s2 = Square(2)

print(s.get_circumferenc())
print(s2.get_circumferenc())

print(s.__gt__(s2))
print(s2.__lt__(s))

c = Circle(5)
print(c.radius)
print(c.get_circumferenc())
c2 = Circle(7)

print(c.__gt__(c2))
print(c.__lt__(c2))

# zadanie 3

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Field({self.value})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.value == other.value
        else:
            return False

    def __setattr__(self, name, value):
        if isinstance(value, int):
            if 10 <= value <= 2000:
                self.__dict__[name] = value
            else:
                raise ValueError(f"Value for {name} must be in range between 10-2000")
        elif isinstance(value, str):
            self.__dict__[name] = value
        else:
            raise TypeError(f"Value for {name} must be either type of int or string")

# testy do zadania 3

#f = Field(5.5) błąd przez typ zmiennej
#print(f.value)

#f2 = Field(2) błąd przez zakres wartości
#print(f.value)

f3 = Field(25)
print(f3)