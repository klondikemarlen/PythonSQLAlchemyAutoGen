##testing##        
# from sqlalchemy import Table, MetaData, Column, Integer, String, Float, Boolean

# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.hybrid import hybrid_property

# from sqlalchemy.exc import ArgumentError

# from sqlalchemy import inspect
# from sqlalchemy.orm import mapper

# from sqlalchemy import create_engine

from base_classes import Base


from jinja2 import Environment, FileSystemLoader, select_autoescape

from non_declarative_objects import Hero, Order

import pdb

class Column:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
        
    def __str__(self):
        return "<Column: name='{}', type='{}', value={}>".format(self.name, self.type, repr(self.value))
        
            
class BuildTable:
    # def __new__(cls):
        # return self.obj, cls

    def __init__(self, obj, tablename=''):
        self.obj = obj
        self.tablename = ''
        self.column_names = []
        #Attributes that require extra work.
        #They might be relationships, foreign keys or children or parents or something.
        #Or just basic lists, or dicts or booleans
        self.relationships = {'lists': [], 'dicts': [], 'nones': []}
        
        try:
            obj.__dict__
        except AttributeError:
            print()
            print("Some kind of base case.")
            print("Your object is a base class. Pass in a tablename in __init__")
            print("build a new class that uses this class as a dict of itself?")
            print()
        
        if tablename:
            self.tablename = tablename
        else:
            self.tablename = self.get_table_name()
            
        self.column_names = self.build_columns()
     
        # for column in self.column_names:
            # print(column)
        

        
    def build_columns(self):
        """Generate columns for table.
        
        Also updates relationship attribute which I will be implemented using recursion.
        """
        data = {}
        try:
            data = vars(self.obj)
        except TypeError as ex:
            if type(self.obj) == type(dict()):
                data = self.obj
            else:
                raise ex
        for name in sorted(data.keys()):
             
            column_type = type(data[name])
            if name.startswith("__"):
                pass #ignore this one.
            elif type(list()) == column_type:
                self.relationships['lists'].append(name)
            elif type(dict()) == column_type:
                self.relationships['dicts'].append(name)    
            elif type(None) == column_type:
                self.relationships['nones'].append(name)    
            elif type(int()) == column_type:
                yield Column(name, "Integer", data[name])
            elif type(str()) == column_type:
                yield Column(name, "String", data[name])
            elif type(float()) == column_type:
                yield Column(name, "Float", data[name])
            elif type(bool()) == column_type:
                yield Column(name, "Boolean", data[name])
            else:
                print(TypeError("Can't yet handle type {}".format(type(data[name]))))
            
    def get_table_name(self):
        try:
            return self.obj.__name__.lower()
        except AttributeError:
            return self.obj.__class__.__name__.lower()
        

########## New Template concept.

# print(vars(Order))

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(default_for_string=False, default=False)
)
template = env.get_template('generic.py')

# hero_table_cls = BuildTable(Hero())
# print(template.render(cls=hero_table_cls))
order_table_cls = BuildTable(Order)
print(template.render(cls=order_table_cls))

