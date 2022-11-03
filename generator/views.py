from django.shortcuts import render
from django.http import HttpResponse
import random as rd

# Create your views here.
def gen_nums(request):
    res = rd.randint(1,1000)
    return HttpResponse(str(res))

def gen_pass(request):
    nums = '123456789'
    alphavit = 'abcdefghijklmnoprstuvwxyz'
    res = ''
    for i in range(10):
        mark = rd.randint(0, 2)
        if mark:
            res += rd.choice(alphavit)
        else:
            res += rd.choice(nums)
    return HttpResponse(res)

def gen_name(request):
    names = ['Саша','Ваня','Оля','Максим','Яра','Коля','Анастасия','Алексей','Стас','Юра','Сёма']
    res = rd.choice(names)
    return HttpResponse(res)