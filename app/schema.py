from ninja.orm import create_schema
from typing import List,Any
from datetime import datetime
from datetime import date
from ninja import Schema
from app import models


Employee = create_schema(models.Employee)


class Search(Schema):
    full_name : str

class BossSchema(Schema):
    id: int




class EmployeeSchemaIn(Schema):
    full_name : str
    position: str
    salary : int

class EmployeeSchemaOut(Schema):
    full_name : str
    position: str
    date_hire : Any = None
    salary : int
    boss : BossSchema

class LoginSchema(Schema):
    username: str
    password: str

class SignUpSchema(Schema):
    username: str
    email  : str
    password1: str
    password2 : str