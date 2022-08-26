
import codecs
import os
import subprocess
import sys
from typing import final
from django.shortcuts import *
from Frontend.models import User
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def   home(request):
    data ={}
    # if User().is_authenticated:
        
    #     messages.warning(request,"Login First Before Run the code")  
    # else:
    #     messages.success(request,"Login Successful")    
    if request.method == 'POST':
        code = request.POST['codearea']
        input_part = request.POST['inputarea']
        intputdata = input_part
        input_part = input_part.replace("\n"," ").split(" ")
        f = open("code.py", "w")
        # print(code)
        f.write(code)
        # output= RunCode()
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

def RunCode():
    compile_java('code.java')
    return execute_java('code.java')

def compile_java(java_file):
    subprocess.check_call(['javac', java_file])

def execute_java(java_file):
    java_class,ext = os.path.splitext(java_file)
    cmd = ['java', java_class]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = proc.communicate()
    return stdout.decode()


def signup(req):
    # user = User()
    if req.method == "POST":
        username = req.POST['name']
        email = req.POST['email']
        psw = req.POST['psw']
        cpsw = req.POST['cpsw']
        if psw == cpsw:
            print(username,email,psw)
            try:
                user = User.objects.create_user(username=username,email=email,password=psw)
                user.save()
                messages.success(req,"Account Create Successful")
            except:
               messages.warning(req,"Use another username") 
            
            return redirect("/login")
        else: 
            print("Confirm password is not same")
            messages.warning(req,"Confirm password is not same") 
            return redirect("login")
        # pass 
    # return render(req, "loginpage.html")

def loginpage(req):
    # user = User()
    # messages.success(req, "Signup Here")
    if req.method == "POST":
        lname = req.POST['lname']
        lpsw = req.POST['psw']
        user =  authenticate(username=lname,password=lpsw)
        # print(user)
        if user is not None:
            login(req,user)
            return redirect(to="home",)
        # print(lname,lpsw)
        messages.error(req,"Incorrect Username and Password")
        return redirect(to="login") 
    
    return render(req, "loginpage.html")

def userlogout(req):
        logout(req)
        return redirect(to='home')