##testing##        
from sqlalchemy import Table, MetaData, Column, Integer, String, Float, Boolean

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from sqlalchemy.exc import ArgumentError

from sqlalchemy import inspect
from sqlalchemy.orm import mapper

from sqlalchemy import create_engine

from base_classes import Base


from jinja2 import Environment, FileSystemLoader, select_autoescape

from non_declarative_objects import Hero, Order

import pdb
            
            
class BuildTable:
    # def __new__(cls):
        # return self.obj, cls

    def __init__(self, obj, metadata, tablename=''):
        self.obj = obj
        try:
            obj.__dict__
        except AttributeError:
            print()
            print("Some kind of base case.")
            print("Your object is a base class. Pass in a tablename in __init__")
            print("build a new class that uses this class as a dict of itself?")
            print()
        
        self.metadata = metadata
        if tablename:
            self.tablename = tablename
        else:
            self.tablename = BuildTable.get_table_name(obj)
        self.column_names = BuildTable.get_column_names(obj)
        #Attributes that require extra work.
        #They might be relationships, foreign keys or children or parents or something.
        #Or just basic lists, or dicts or booleans
        self.relationships = {'lists': [], 'dicts': [], 'nones': []}
        self.table = self.build_table()
        
        
    def build_table(self):
        """Return a Table object.
        
        Doesn't yet accomodate relationships.
        metadata is a bad global ...
        """
        return Table(self.tablename, self.metadata,
            Column('id', Integer, primary_key=True),
            *self.build_columns()
        )

        
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
            if type(list()) == column_type:
                self.relationships['lists'].append(name)
            elif type(dict()) == column_type:
                self.relationships['dicts'].append(name)    
            elif type(None) == column_type:
                self.relationships['nones'].append(name)    
            elif type(int()) == column_type:
                yield Column(name, Integer, default=data[name])
            elif type(str()) == column_type:
                yield Column(name, String, default=data[name])
            elif type(float()) == column_type:
                yield Column(name, Float, default=data[name])
            elif type(bool()) == column_type:
                yield Column(name, Boolean, default=data[name])
            else:
                raise TypeError("Can't yet handle type {}".format(type(data[name])))


    def get_column_names(obj):
        """Get column names for a given object.
        
        Ignores functions, may ignore class attributes.
        """
        try:
            return (attr for attr in vars(obj))
        except TypeError as ex:
            if type(dict()) == type(obj):
                return sorted(obj.keys())
            raise ex
            
    def get_table_name(obj):
        return obj.__class__.__name__
        

########## New Template concept.

# print(vars(Order))

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(default_for_string=False, default=False)
)
template = env.get_template('generic.py')
print(template.render(cls=Hero))
exit()




        
##########Testing 
metadata = MetaData()       

hero = Hero()                
                
primary_attributes = {"Strength": 1, "Resilience": 1, "Vitality": 1, "Fortitude": 1, "Reflexes": 1, "Agility": 1, "Perception": 1, "Wisdom": 1, "Divinity": 1, "Charisma": 1, "Survivalism": 1, "Fortuity": 1}
                
meta_hero = BuildTable(hero, metadata=metadata)
hero_table = meta_hero.table

mapper(Hero, hero_table)
print(meta_hero.relationships)

meta_dict = BuildTable(primary_attributes, metadata=metadata)
dict_table = meta_dict.table
# pdb.set_trace()
mapper(primary_attributes, dict_table)

print(meta_dict.relationships)

# address = Table('address', metadata,
            # Column('id', Integer, primary_key=True),
            # Column('user_id', Integer, ForeignKey('user.id')),
            # Column('email_address', String(50))
            # )

# mapper(User, user, properties={
    # 'addresses' : relationship(Address, backref='user', order_by=address.c.id)
# })

# mapper(Address, address)



for t in metadata.sorted_tables:
    print("Table name: ", t.name)
    print("t is page_table: ", t is dict_table)

for column in dict_table.columns:
    print("Column Table name: {}, type: {}".format(column.name, column.type))

engine = create_engine('sqlite:///:memory:', echo=False)
metadata.bind = engine
metadata.create_all(checkfirst=True)

# Base.metadata.create_all(engine)


# primary_attributes = BaseDict({"Strength": 1, "Resilience": 1, "Vitality": 1, "Fortitude": 1, "Reflexes": 1, "Agility": 1, "Perception": 1, "Wisdom": 1, "Divinity": 1, "Charisma": 1, "Survivalism": 1, "Fortuity": 1})

#is a one to one list the same as just having a variable equal to a Base object?
# is primary_attributes = relationship(BaseDict, one to one) 
# equal to
# primary_attributes = BaseDict()?

# print(primary_attributes)

# import pdb; pdb.set_trace()
# primary_attributes['Badassery'] = 5
# print(primary_attributes)
# print(primary_attributes.keys())



# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# hero = Hero()
# hero.name = 'Haldon'
# session.add(hero)



# insp = inspect(Hero)
# for column in list(insp.columns):
    # print(repr(column))
# hero_table.update(hero)


