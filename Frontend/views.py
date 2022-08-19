import sys
from django.shortcuts import render

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
    
    return render(request, 'index.html',data)