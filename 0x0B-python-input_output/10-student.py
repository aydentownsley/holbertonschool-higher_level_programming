#!/usr/bin/python3
""" Student to JSON
"""


class Student:
    """
        first_name: first name
        last_name: last name
        age: age of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            self: student
        """
        if (attrs) and type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return (self.__dict__)
                else:
                    res = {}
                    for x in attrs:
                        if x in self.__dict__:
                            res.update({x: self.__dict__[x]})
                    return res
        else:
            return (self.__dict__)
