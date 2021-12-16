from app import models
from typing import List,Any
from . import schema
from ninja.pagination import paginate, PageNumberPagination
from django.contrib.auth.models import User
from ninja.errors import HttpError
from ninja import NinjaAPI
from django.http import HttpResponse
from .logic import create_token, AuthBearer

from django.shortcuts import get_object_or_404




api = NinjaAPI(auth=AuthBearer())


@api.get("employee/", response=List[schema.EmployeeSchemaOut], tags=['List of employee ( 50 / per page)'])
@paginate(PageNumberPagination)
def get_employee(request, **kwargs):
    return models.Employee.objects.all().order_by('date_hire')


@api.post('employee/create',response = schema.Employee, tags=['Create Employee'])
def create(request, data:schema.EmployeeSchemaIn):
    new = models.Employee.objects.create(
        full_name = data.full_name,
        position =  data.position,
        salary = data.salary,
    )
    try:
        new.save()
        return new
    except:
        raise HttpError(422,"something wrong happened")


@api.put('employee/update/{id}', tags=['Create Employee'])
def create(request, id:int, payload:schema.EmployeeSchemaIn):
    element = get_object_or_404(models.Employee, id=id)
    list_ = []
    for attr, value in payload.dict().items():
        if (value):
            list_.append(attr)
        setattr(element, attr, value)
    element.save(update_fields=list_)
    return {"success": True}


@api.get("search/", response=List[schema.EmployeeSchemaOut] ,tags=['Search employee by name '])
def get_search(request, title : str):
    key = title
    res = models.Employee.objects.filter(full_name__contains = key)


    return res




@api.post('signup', tags=["Register new user"],auth=None)
def Register(request, data: schema.SignUpSchema):
    username = data.username
    email = data.email
    password = data.password1
    confirm = data.password2

    if (User.objects.filter(username=username).exists() == True ) or (User.objects.filter(email=email).exists()==True):
        return HttpError(404, "Already exists" )
    else:
        user = User.objects.create(username=username, email=email)
        if password == confirm:
            user.save()
            return HttpResponse("you created account ")
        else:
            return HttpError(404,"Password are not same")






@api.post('login', tags=["login"],auth=None)
def login(request, data: schema.LoginSchema):
    username = data.username
    if User.objects.filter(username=username).exists() == True:
        user = User.objects.get(username=data.username)
        if user.check_password(data.password):
            return 200, (user.id, create_token(user.id))
        else:
            raise HttpError(404, "Неверная пароль")
    else:
        raise HttpError(404, "Неверная почта или пароль!")

