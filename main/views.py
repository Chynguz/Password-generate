import random

from django.http import HttpResponseRedirect
from django.shortcuts import render

# from django.contrib import messages  для вывода сообщения erorr

# Create your views here.


def main(request):
    return render(request, 'index.html')


def generate(request):
    try:
        if request.method == 'POST':
            length = int(request.POST.get('length'))
            if length <= 7:
                context = 'Слишком короткий пароль!'
                return render(request, 'smal.html', {'context': context})
            elif length > 32:
                context = 'Слишком длинный пароль! Потом забудешь!'
                return render(request, 'smal.html', {'context': context})
            else:
                upper = list('QWERTYUIOPASDFGHJKLZXCVBNM')
                alpha = list('qwertyuiopasdfghjklzxcvbnm')
                simb = ['!', '@', '$', '%', '&', '*']
                num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                number = num

                if request.POST.get('char'):
                    number += alpha
                if request.POST.get('upper'):
                    number += upper
                if request.POST.get('simbol'):
                    number += simb

                password = ''
                password1 = ''
                password2 = ''
                for j in range(length):
                    password += random.choice(number)
                    password1 += random.choice(number)
                    password2 += random.choice(number)
                return render(request, 'generate.html', {'length': length, 'password': password, 'password1': password1, 'password2': password2})
    except ValueError:
        return HttpResponseRedirect('/')
