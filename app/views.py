from django.shortcuts import render, redirect
from app.models import User, Admin
from app.forms import UserForm, AdminForm
from app.authenticate import Authenticate


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save()
        redirect('/')
    form = UserForm()
    return render(request, 'signup.html', {'form': form})


def adsignup(request):
    if request.method == "POST":
        aform = AdminForm(request.POST)
        aform.save()
        redirect('/')
    aform = AdminForm()
    return render(request, 'adsignup.html', {'form': aform})


def alogin(request):
    return render(request, 'alogin.html')


def login(request):
    return render(request, 'login.html')


def loginpage(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/menu')


def aloginpage(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/auser')


@Authenticate.valid_login
def menu(request):
    return render(request, 'menu.html')


def dashboard(request):
    users = User.objects.all()
    return render(request, "dashboard.html", {'users': users})


def admindashboard(request):
    admins = Admin.objects.all()
    return render(request, "admindashboard.html", {'ausers': admins})


@Authenticate.valid_alogin
def adminpanel(request):
    return render(request, 'dashboarddesign.html')


def edit(request, id):
    user = User.objects.get(user_id=id)
    # user=User.objects.raw('select * from user where user_id=(??)')
    return render(request, 'edit.html', {'user': user})


def adminedit(request, aid):
    admin = Admin.objects.get(admin_id=aid)
    # user=User.objects.raw('select * from user where user_id=(??)')
    return render(request, 'adminedit.html', {'admin': admin})


def update(request, id):
    user = User.objects.get(user_id=id)
    form = UserForm(request.POST, instance=user)
    form.save()
    return redirect('/')


def adminupdate(request, aid):
    admin = Admin.objects.get(admin_id=aid)
    aform = AdminForm(request.POST, instance=admin)
    aform.save()
    return redirect('/')


def delete(request, id):
    user = User.objects.get(user_id=id)
    user.delete()
    return redirect('/')


def adelete(request, aid):
    admin = Admin.objects.get(admin_id=aid)
    admin.delete()
    return redirect('/admins')
