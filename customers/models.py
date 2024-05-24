from mongoengine import Document, StringField, FloatField, BooleanField, EmailField, IntField, ObjectIdField

class Cliente(Document):
    DNI = StringField(required=True, max_length=200)
    nombre = StringField(required=True, max_length=200)
    email = EmailField(required=True)
    profesion = StringField(required=True, max_length=200)
    actividad_economica = StringField(required=True, max_length=200)
    empresa = StringField(required=True, max_length=200)
    ingresos = IntField(required=True)
    deudas = IntField(required=True)
    credit_scoring = IntField(required=True)
    cliente_actual = BooleanField(required=True)
    _class = StringField(required=False)
    meta = {
        'collection': 'clientes'
    }
