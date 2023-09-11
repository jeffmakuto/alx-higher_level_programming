#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """public instance method area and integer_validator"""
    def area(self):
        """raise exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value is an integer > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
