from django.shortcuts import HttpResponse, render,redirect
from data import models
from data.form.type import TypeModelForm
from data.form.firm import FirmModelForm
from data.form.sell import SellModelForm
from data.form.car import CarModelForm
from data.form.user import UserModelForm

def index(request):
    return render(request, 'index.html')

def login(request):
    errmsg = ""
    if request.method == "POST":
        usertype = request.POST['seltype']
        username = request.POST['username']
        password = request.POST['password']
        object = models.UserManager.objects.filter(username=username,password=password,usertype=usertype)
        if not object:
            return render(request, 'login.html', {"errmsg": "用户名或密码输入错误"})
        else:
            if usertype == "买家":
                return redirect('/data/buylist/')
            elif usertype == "卖家":
                return redirect('/data/selllist/')
            else:
                return redirect('/data/carlist/')
    return render(request, 'login.html')

def register(request):
    err_msg = ''
    if request.method == 'POST':
        list_type = request.POST.get('seltype')
        list_name = request.POST.get('username')
        list_pwd = request.POST.get('password')
        if list_name:
            # 判断账户是否存在
            pub_list = models.UserManager.objects.filter(username=list_name)
            if pub_list:
                err_msg = '账户已存在'
                return render(request, 'alerttest.html')
            else:
                pub_obj = models.UserManager.objects.create(username=list_name, password=list_pwd,usertype=list_type)
                if list_type == "买家":
                    return redirect('/data/buylist/')
                elif list_type == "卖家":
                    return redirect('/data/selllist/')
                else:
                    return redirect('/data/carlist/')

        else:
            err_msg = '用户名不能为空'
            return render(request, 'alerttest.html')



def buy(request,nid):
    if request.method == "GET":
        obj = models.CarInfo.objects.get(id=nid)
        obj.catstatus = "已支付"
        models.OrderManager.objects.create(carname=obj.carname,carstatus=obj.catstatus)
        obj.save()
        return render(request, 'alert.html')

def search(request):
    if request.method == "POST":
        tmp = request.POST["ipholder"]
        print(tmp)
        carname_queryset = models.CarInfo.objects.filter(carname=tmp)
        if not carname_queryset:
            print(tmp)
            cartype_queryset = models.CarInfo.objects.filter(carsize=tmp)
            if not cartype_queryset:
                return render(request, 'buylist.html', {"buy_queryset": cartype_queryset})
            return render(request, 'buylist.html', {"buy_queryset": cartype_queryset})
        return render(request, 'buylist.html', {"buy_queryset": carname_queryset})

def selllist(request):
    sell_queryset = models.CarInfo.objects.all()
    return render(request, 'selllist.html', {"sell_queryset": sell_queryset})
def addsell(request):
    if request.method == "GET":
        form = SellModelForm()
        return render(request, 'sell_form.html', {"form": form})
    form = SellModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/selllist/')
    return render(request, 'sell_form.html', {"form": form})
def editsell(request,nid):
    obj = models.CarInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = SellModelForm(instance=obj)
        return render(request, 'sell_form.html', {"form": form})
    form = SellModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/selllist/')
    return render(request, 'sell_form.html', {"form": form})
def delsell(request,nid):
    models.CarInfo.objects.filter(id=nid).delete()
    return redirect('/data/selllist/')


def buylist(request):
    buy_queryset = models.CarInfo.objects.all()
    return render(request, 'buylist.html', {"buy_queryset": buy_queryset})


def carlist(request):
    car_queryset = models.CarInfo.objects.all()
    return render(request, 'carlist.html', {"car_queryset": car_queryset})

def editcar(request,nid):
    obj = models.CarInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = CarModelForm(instance=obj)
        return render(request, 'car_form.html', {"form": form})
    form = CarModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/carlist/')
    return render(request, 'car_form.html', {"form": form})

def delcar(request,nid):
    models.CarInfo.objects.filter(id=nid).delete()
    return redirect('/data/carlist/')


def typelist(request):
    type_queryset = models.Cartype.objects.all()
    return render(request, 'typelist.html',{"type_queryset":type_queryset})

def addtype(request):
    if request.method == "GET":
        form = TypeModelForm()
        return render(request, 'type_form.html', {"form": form})
    form = TypeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/typelist/')
    return render(request, 'type_form.html', {"form": form})

def edittype(request,nid):
    obj = models.Cartype.objects.filter(id=nid).first()
    if request.method == "GET":
        form = TypeModelForm(instance=obj)
        return render(request, 'type_form.html', {"form": form})
    form = TypeModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/typelist/')
    return render(request, 'type_form.html', {"form": form})
def deltype(request,nid):
    models.Cartype.objects.filter(id=nid).delete()
    return redirect('/data/typelist/')


def firmlist(request):
    firm_queryset = models.Carfirm.objects.all()
    return render(request, 'firmlist.html', {"firm_queryset": firm_queryset})
def addfirm(request):
    if request.method == "GET":
        form = FirmModelForm()
        return render(request, 'firm_form.html', {"form": form})
    form = FirmModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/firmlist/')
    return render(request, 'firm_form.html', {"form": form})
def editfirm(request,nid):
    obj = models.Carfirm.objects.filter(id=nid).first()
    if request.method == "GET":
        form = FirmModelForm(instance=obj)
        return render(request, 'firm_form.html', {"form": form})
    form = FirmModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/firmlist/')
    return render(request, 'firm_form.html', {"form": form})
def delfirm(request,nid):
    models.Carfirm.objects.filter(id=nid).delete()
    return redirect('/data/firmlist/')

def userlist(request):
    user_queryset = models.UserManager.objects.all()
    return render(request, 'userlist.html', {"user_queryset": user_queryset})
def adduser(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_form.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/data/userlist/')
    return render(request, 'user_form.html', {"form": form})
def edituser(request,nid):
    obj = models.UserManager.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=obj)
        return render(request, 'user_form.html', {"form": form})
    form = UserModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/data/userlist/')
    return render(request, 'user_form.html', {"form": form})
def deluser(request,nid):
    models.UserManager.objects.filter(id=nid).delete()
    return redirect('/data/userlist/')



def delmenu(request,nid):
    models.OrderManager.objects.filter(id=nid).delete()
    return redirect('/data/menulist/')

def menulist(request):
    menu_queryset = models.OrderManager.objects.all()
    return render(request, 'menulist.html', {"menu_queryset": menu_queryset})
