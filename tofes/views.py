from django.shortcuts import render
from django.http import HttpResponse
from .models import Right, Entry

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
    e = Entry(name1=request.POST['name'], fname = request.POST['fname'], input_age = request.POST['age'])
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

def counter(age1,age2):
    return Entry.objects.filter(input_age__lte = age2, input_age__gte = age1).count()
    

def stats(request):
        countnum =  Entry.objects.count()
        countnumkid = Entry.objects.filter(input_age__lte = 15, input_age__gte = 0 ).count()
        countnumwork = Entry.objects.filter(input_age__lte = 65, input_age__gte = 16).count()
        countnumold = Entry.objects.filter(input_age__gte = 66).count()
        lasttenentrys = Entry.objects.order_by('-created').all()[:10]
        # counter(age1,age2)
        # entry = Entry.objects.all()
        # for name1 in entry:
        #     countnum = countnum + 1
        
        # entrykid = Entry.objects.filter( input_age__lte = 15, input_age__gte = 0 )
        # for name1 in entrykid:
        #     countnumkid = countnumkid + 1
        
        # entrywork = Entry.objects.filter( input_age__lte = 65, input_age__gte = 15 )
        # for name1 in entrywork:
        #     countnumwork = countnumwork + 1

        # entryold = Entry.objects.filter( input_age__lte = 120, input_age__gte = 65 )
        # for name1 in entryold:
        #     countnumold = countnumold + 1
        return render(request, "stats.html",{"countnum":countnum,"countnumkid":countnumkid,
        "countnumwork":countnumwork,"countnumold":countnumold,"lasttenentrys":lasttenentrys})