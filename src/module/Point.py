import math

class Point:
    """
    Represents a point in R^n space.

    Attributes
    ----------
        coor (tuple): A tuple of n coordinates that define the position of the point in R^n space.

    Methods
    ----------
        __init__(*coor): Initializes a new Point object with the given coordinates.
        __repr__(): Returns a string representation of the Point object.
        __len__(): Returns the number of coordinates in the Point object.
        distance_to(other): Returns the Euclidean distance between the Point object and the other Point object.
        
    Operators
    ----------
        __getitem__(index): `[]` Returns the coordinate at the given index in the Point object.
        __eq__(other): `=` Returns True if the Point object is equal to the other Point object.
        __add__(other): `+` Returns a new Point object that is the sum of the Point object and the other Point object.
        __sub__(other): `-` Returns a new Point object that is the difference between the Point object and the other Point object.
        __mul__(other): `*` Returns the dot product of the Point object and the other Point object, or a new Point object that is the scalar product of the Point object and the scalar other.
        __pow__(other): `**` Returns a new Point object that is the element-wise power of the Point object to the power of the scalar other.
    """
    
    def __init__(self, *coor):
        self.coor = coor

    def __repr__(self):
        return f"Point({', '.join(str(c) for c in self.coor)})"

    def __len__(self):
        return len(self.coor)

    def __getitem__(self, index):
        return self.coor[index]

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.coor == other.coor

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("unsupported operand type(s) for +: 'Point' and '{type(other).__name__}'")
        if len(self) != len(other):
            raise ValueError("Points must have the same dimension to add them")
        return Point(*[self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError("unsupported operand type(s) for -: 'Point' and '{type(other).__name__}'")
        if len(self) != len(other):
            raise ValueError("Points must have the same dimension to subtract them")
        return Point(*[self[i] - other[i] for i in range(len(self))])

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("unsupported operand type(s) for distance_to: 'Point' and '{type(other).__name__}'")
        if len(self) != len(other):
            raise ValueError("Points must have the same dimension to calculate distance between them")
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(self.coor, other.coor)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Point(*[self[i] * other for i in range(len(self))])
        elif isinstance(other, Point):
            if len(self) != len(other):
                raise ValueError("Points must have the same dimension to dot multiply them")
            return sum([self[i] * other[i] for i in range(len(self))])
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Point' and '{type(other).__name__}'")

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return Point(*[self[i] ** other for i in range(len(self))])
        else:
            raise TypeError(f"unsupported operand type(s) for **: 'Point' and '{type(other).__name__}'")
