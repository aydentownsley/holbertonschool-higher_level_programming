#!/usr/bin/python3
"""
Base Class Module
-------
This module is creating
a Base Object, to be used
to inherit from.
"""
import json


class Base:
    """
        Base: Ancesteral Object
        nb: number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            self: object
            ---
            id: of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries and len(list_dictionaries) is not 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        list_of_dicts = []
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w') as f:
            for i in list_objs:
                list_of_dicts.append(i.to_dictionary())
            f.write(cls.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ is 'Square':
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        list_of = []
        f_name = '{}.json'.format(cls.__name__)
        with open(f_name, 'r') as f:
            cr_dict = cls.from_json_string(f.read())
            for i in cr_dict:
                list_of.append(cls.create(**i))
            return list_of
        return []
