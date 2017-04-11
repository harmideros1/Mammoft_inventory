from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import *
from django.conf import settings
from app.login.models import U_hash, calculate_hash
import string
import random
import socket
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage


def change_password(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')

    user_send = False
    if "update_Cambio_val" in request.POST:
        if request.POST.get("user") and not request.POST.get("cod_validate"):
            request.session['usr_change'] = request.POST.get("user")
            try:
                u = User.objects.get(username=request.session['usr_change'])
                if u.is_staff:
                    return HttpResponseRedirect('/error/denied')
                if u:
                    subject = "Solicitud cambio de password - Mammoft Inventory Managment"
                    mensaje = "Usuario: "+ u.username +"\nCódigo de validacion:"+str(u.u_hash.hash)
                    send_mail(subject, mensaje, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=False)

                    hash = u.u_hash.hash
                    usuario = u.username
                    user_send = True
                    context = {"user_send":user_send,
                               "hash":hash,
                               "usuario":usuario}
                    return render(request,"Content_login/Conten_login.html",context)
            except User.DoesNotExist:
                user_send = False
                context = {"msg":"El usuario no se encuentra en nuestra base de datos",
                           "user_send":user_send,}
                request.session.pop('usr_change')
                return render(request,"Content_login/Conten_login.html",context)

    if "update_cod" in request.POST:
        if request.POST.get("cod_validate"):
            can_change = False
            codigo_validacion = request.POST.get("cod_validate")
            usuario = request.session.get('usr_change')
            u = User.objects.get(username=usuario)
            hash = u.u_hash.hash
            if codigo_validacion == hash:
                can_change = True
                user_send = True
                context = {"user_send":user_send,
                           "can_change":can_change,
                           "usuario":usuario}
                return render(request,"Content_login/Conten_login.html",context)
            else:
                hash = u.u_hash.hash
                usuario = u.username
                user_send = True
                context = {"msg":"El codigo de validación no es correcto",
                           "user_send":user_send,
                           "hash":hash,
                           "usuario":usuario}
                return render(request,"Content_login/Conten_login.html",context)

    if "update_pass" in request.POST:
        if request.POST.get("pone") and request.POST.get("ptwo"):
            p1 = request.POST.get("pone")
            p2 = request.POST.get("ptwo")
            usuario = request.session.get('usr_change')
            u = User.objects.get(username=usuario)
            hash = u.u_hash.hash

            if p1 == p2:
                u.set_password(p1)
                u.save()
                U_hash.objects.filter(user_id=u, hash=hash).update(hash=calculate_hash())
                request.session.pop('usr_change')
                return HttpResponseRedirect('/home')
            else:
                can_change = True
                user_send = True
                context = {"msg":"Los password no coinciden",
                           "user_send":user_send,
                           "can_change":can_change,
                           "usuario":usuario}
                return render(request,"Content_login/Conten_login.html",context)
        else:
            usuario = request.session.get('usr_change')
            can_change = True
            user_send = True
            context = {"msg":"Aun no rellenas los campos",
                       "user_send":user_send,
                       "can_change":can_change,
                       "usuario":usuario}
            return render(request,"Content_login/Conten_login.html",context)

    context = {"user_send":user_send,}
    return render(request,"Content_login/Conten_login.html",context)

@login_required(login_url='/login')
def profile_view(request):
    u = User.objects.get(username=request.user)

    if "edit_profile" in request.POST:
        editing = True
        context = {'editing':editing,}
        return render(request, "user/profile.html", context)

    if "save_profile" in request.POST:
        myfile = request.FILES.get('picture')
        fs = FileSystemStorage()
        try:
            filename = fs.save("login/users/profile/" + myfile.name, myfile)
            U_hash.objects.filter(user_id=u).update(avatar=fs.url(filename))
        except AttributeError:
            pass

    if "calendar" in request.POST:
        nacimiento = request.POST.get("calendar")
        fn = datetime.strptime(nacimiento, '%d/%m/%Y').date()
        age = datetime.now().date() - fn
        age_ac = str((age.days / 365)).split('.')[0]
        U_hash.objects.filter(user_id=u).update(f_nacimiento=fn, edad=age_ac)

    if "gender" in request.POST:
        U_hash.objects.filter(user_id=u).update(sexo=request.POST.get('gender'))

    if "cargo" in request.POST:
        if request.POST.get('cargo').strip() != "":
            U_hash.objects.filter(user_id=u).update(cargo=request.POST.get('cargo'))

    if "direccion" in request.POST:
        if request.POST.get('direccion').strip() != "":
            U_hash.objects.filter(user_id=u).update(direccion=request.POST.get('direccion'))

        editing = False
        context = {'editing':editing}
        return render(request, "user/profile.html", context)

    context = {}
    return render(request, "user/profile.html", context)

@login_required(login_url='/login')
def index_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')

def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)

        if request.user.is_staff:
            logout(request)
            return HttpResponseRedirect('/error/denied')

        if request.user.is_authenticated:
            return HttpResponseRedirect('/home')
        else:
            mensaje = 'El usuario existe pero esta deshabilitado'
            logout(request)
    else:
        if request.POST:
            mensaje = 'El usuario o contraseña son incorrecto'
        else:
            mensaje = ''

    context = {'mensaje':mensaje}
    return render(request, "login_page.html", context)

@login_required(login_url='/login')
def home_page(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    return render(request, "home_page.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def denied(request):
    referer = request.META.get('HTTP_REFERER')
    context = {'referer':referer}
    return render(request, "extra/Oops.html", context)
