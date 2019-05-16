from django.shortcuts import render
from django.http import HttpResponse
from .models import Right, Entry1

# Create your views here.
def index(request):
        return render(request, "index.html")

def index2(request):
    name = "yotam"
    return HttpResponse("<h1> Hello "+name+" </h1>")

def result(request):
    name = namecheck(request.POST['name'])
    fname = request.POST['fname']
    age = agecheck(request.POST['age'])
    agenum = request.POST['age']
    e = Entry1(name1=request.POST['name'], fname = request.POST['fname'], inputage = request.POST['age'])
    e.save()
    
    return render(request, "result.html",{"x":name, "f":fname, "a":age ,"agenum":agenum})


def namecheck(name):
    if name=="yotam": 
        return name.upper()
    else:
        return name
        
def agecheck(age):
    age = int(age)
    if 0<age<=15:
        return "kid"
    elif 15<age<65:
        return "working age"
    else:
        return "old"

def details(request):
    age= int(request.GET['agenum'])
    rights = Right.objects.filter(enabled = True, minage__lte = age, maxage__gte = age )
    # rights = ["one","two"]
    # if age == "kid":
    #     rights = ["three","four"]
    # if age == "old":
    #     rights = ["five", "six", "seven"]
    return render(request, "details.html",{"age":age, "rights":rights})

def stats(request):
        countnum = 0
        countnumkid = 0
        countnumwork = 0
        countnumold = 0
        entry = Entry1.objects.all()
        for name1 in entry:
            countnum = countnum + 1

        entrykid = Entry1.objects.filter( inputage__lte = 15, inputage__gte = 0 )
        for name1 in entrykid:
            countnumkid = countnumkid + 1
        
        entrywork = Entry1.objects.filter( inputage__lte = 65, inputage__gte = 15 )
        for name1 in entrywork:
            countnumwork = countnumwork + 1

        entryold = Entry1.objects.filter( inputage__lte = 120, inputage__gte = 65 )
        for name1 in entryold:
            countnumold = countnumold + 1
        return render(request, "stats.html",{"countnum":countnum,"countnumkid":countnumkid,"countnumwork":countnumwork,"countnumold":countnumold})