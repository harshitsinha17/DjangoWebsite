from django.shortcuts import render
from .models import Members

# Create your views here.
def index (request):
    memb1 = Members()
    memb1.img = "portfolio-1.jpg"
    memb1.name = "Jon Snow"
    memb1.designation = " Clerk "

    memb2 = Members()
    memb2.img = "portfolio-2.jpg"
    memb2.name = "Rishabh Pant"
    memb2.designation = " Marketing manager "

    memb3 = Members()
    memb3.img = "portfolio-3.jpg"
    memb3.name = "Ronaldo"
    memb3.designation = " CEO "

    memb = [memb1,memb2,memb3]

    memb = Members.objects.all()


    return render(request, 'index.html',{'mem':memb})
