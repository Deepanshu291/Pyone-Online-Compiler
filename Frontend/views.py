
import sys
from django.shortcuts import *
from Frontend.models import User
from django.contrib.auth import authenticate , login ,logout

# Create your views here.
def home(request):
    data ={}
    if request.method == 'POST':
        code = request.POST['codearea']
        input_part = request.POST['inputarea']
        intputdata = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        def input():
            a = input_part[0]
            del input_part[0]
            return a
        try:
            org_stout =sys.stdout
            sys.stdout = open('output.txt','w')
            exec(code)
            sys.stdout.close()
            sys.stdout = org_stout
            output = open('output.txt','r').read()
        except Exception as e:
            sys.stdout.close()
            sys.stdout = org_stout
            output = e
        print(output)
        data={
            'code':code,
            'input':intputdata,
            'output':output
        }
    
    return render(request, 'home.html',data)

def signup(req):
    # user = User()
    if req.method == "POST":
        name = req.POST['name']
        email = req.POST['email']
        psw = req.POST['psw']
        cpsw = req.POST['cpsw']
        if psw == cpsw:
            print(name,email,psw,cpsw)
            user = User(name = name, email = email,psw = psw, is_active= True)
            user.save()
            return redirect("/login")
        else: 
            print("Confirm password is not same")
        # pass 
    # return render(req, "loginpage.html")

def login(req):
    user = User()
    if req.method == "POST":
        lname = req.POST['lname']
        lpsw = req.POST['psw']
        user.authenticate(name=lname,psw=lpsw)
        print(lname,lpsw) 
        return redirect("/") 
    return render(req, "loginpage.html")