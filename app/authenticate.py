from django.db.models import Q
from django.shortcuts import redirect

from app.models import User, Admin


class Authenticate:
    def valid_login(function):
        def login(request):
            try:

                User.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))
                return function(request)

            except:
                return redirect("/login")

        return login



    def valid_alogin(function):
        def alogin(request):
            try:

                Admin.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))
                return function(request)

            except:
                return redirect("/alogin")

        return alogin
