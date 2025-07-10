from django.shortcuts import render
from app.models import GeneralInfo


# Create your views here.
def index(request):


   # general_info = GeneralInfo.objects.first()
   # print(f"General Info: {GeneralInfo.location}")

   all_records = GeneralInfo.objects.all()
   print(all_records)
   context = {}
   return render(request, "index.html", context)

   

def about_us(request):
   context = {}
   return render(request, "about_us.html", context)
            