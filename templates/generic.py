{# Jinja2 template for table schema. #}

class {{ cls.obj.__name__ }}(Base):
    __tablename__ = '{{ cls.tablename }}'
    
    id = Column(Integer, primary_key=True)
{% for column in cls.build_columns() %}
    {{ column.name }} = Column({{ column.type }}, default={{ column.value | tojson }}){% endfor %}