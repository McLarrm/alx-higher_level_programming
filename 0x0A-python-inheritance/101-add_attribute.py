#!/usr/bin/python3
""" Attribute to an object """


class MyClass:
    pass

obj = MyClass()
add_attribute(obj, 'name', 'John')
print(obj.name)

add_attribute(obj, 'age', 25)
