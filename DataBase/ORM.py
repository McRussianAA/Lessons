from peewee import *
import datetime

dbhandle = SqliteDatabase('..//SQLite//library.db')

class BaseModel(Model):
    class Meta:
        database = dbhandle

class Book(BaseModel):
    id = PrimaryKeyField(null=False)
    Title = CharField(max_length=100)
    Authors = CharField(max_length=100)
    Year = IntegerField()
    Pages = IntegerField()


class Abonent(BaseModel):
    id = PrimaryKeyField(null=False)
    fullname = CharField(max_length=100)
    registration = DateField()
    book_id = ForeignKeyField(Book, to_field='id')

dbhandle.connect()
Abonent.create_table()
Book.create_table()

