import requests
from django.shortcuts import render,HttpResponse,redirect
from app01.models import Staff
from app01.models import Account
from .utils.error import *
import hashlib
from .utils import getHomeData
# Create your views here.

# 默认参数 request

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(pwd.encode())
        pwd = md5.hexdigest()

        try:
            user=Account.objects.get(username=uname,password=pwd)
            request.session['username']=user.username
            return redirect('/app01/home')
        except:
            return errorResponse(request, '用户名或密码错误')

def registry(request):
    if request.method=='GET':
        return render(request,'registry.html')
    else:
        uname=request.POST.get('username')
        staff_id=request.POST.get('staff_id')
        pwd=request.POST.get('password')
        # print(uname,staff_id,pwd)
        try:
            Staff.objects.get(id=staff_id)
        except:
            return errorResponse(request,'非本公司职员无法注册')
        try:
            Account.objects.get(username=uname)
        except:
            md5=hashlib.md5()
            md5.update(pwd.encode())
            pwd=md5.hexdigest()
            Account.objects.create(id=int(staff_id),username=uname,password=pwd)
            return redirect('/app01/login')

        return errorResponse(request, '该用户名已经被注册')

def control(request):
    # 获取所有信息
    data_list=Staff.objects.all()
    # print(data_list)
    return render(request,"control.html",{"data_list":data_list})

def logout(request):
    request.session.clear()
    return redirect('login')

def home(request):
    uname=request.session.get('username')
    user=Account.objects.get(username=uname)
    staffinfo=Staff.objects.get(id=user.id)
    y,m,d=getHomeData.getNowTime()
    return render(request,'index.html',{
        'staffInfo':staffinfo,
        'userInfo':user,
        'dateInfo':{'year':y,'month':m,'day':d},
    })


# Create your views here.
def account_list(request):

    account_list = Account.objects.all()

    return render(request, "account_list.html", {"account_list": account_list})

def account_add(request):
    if request.method == "GET":
        return render(request, "account_add.html")

    # 获取用户提交的部门数据
    account_id = request.POST.get("account_id")
    uname = request.POST.get("username")
    pwd = request.POST.get("password")

    md5 = hashlib.md5()
    md5.update(pwd.encode())
    pwd = md5.hexdigest()

    # 保存到数据库
    Account.objects.create(id=account_id,username=uname,password=pwd)

    return redirect("/app01/account/list/")

def account_delete(request):

    id = request.GET.get('id')
    Account.objects.filter(id=id).delete()

    # 重定向回部门列表
    return redirect("/app01/account/list/")


def account_edit(request, nid):
    """部门编辑"""

    if request.method == "GET":
        # 根据nid,获取数据
        row_object = Account.objects.filter(id=nid).first()
        return render(request, 'account_edit.html', {"row_object": row_object})

    # 如果是POST请求,保存修改
    # id = request.POST.get("id")
    uname = request.POST.get("username")
    pwd = request.POST.get("password")

    md5 = hashlib.md5()
    md5.update(pwd.encode())
    pwd = md5.hexdigest()

    Account.objects.filter(id=nid).update(username=uname,password=pwd)

    # 重定向回部门列表
    return redirect('/app01/account/list/')

def staff_list(request):

    staff_list = Staff.objects.all()

    return render(request, "staff_list.html", {"staff_list": staff_list})

# from django import forms
# class StaffModelForm(forms.ModelForm):
#     class Meta:
#         model=Staff
#         fields=["id", "username", "position"]
#
#
# def staff_add(request):
#     if request.method == "GET":
#         form = StaffModelForm()
#     return render(request, "staff_add.html", {"form": form})

def data(request):
    return render(request, "index2.html" )

def info(request):
    return render(request, "main_info.html" )

def center(request):
    return render(request, "intelligence_center.html" )

def water(request):
    return render(request, "water.html" )
