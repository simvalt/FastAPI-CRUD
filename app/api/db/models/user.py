from sqlalchemy import Column, Table, MetaData
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import event

def after_create_handler(target, connection, **kw):
    print("🚨🚨 TABLA USERS ESTÁ SIENDO CREADA AUTOMÁTICAMENTE 🚨🚨")

metadata_obj = MetaData()

users = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("email", String(255)),
    Column("password", String(255)),
)


event.listen(users, "after_create", after_create_handler)