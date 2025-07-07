from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
   products = [
       {"name": "laptop", "price": 100, "description": "This is product 1."},
       {"name": " smartphone", "price": 200, "description": "This is product 2."},
       {"name": "headphone ", "price": 300, "description": "This is product 3."},
       {"name": "camera ", "price": 400, "description": "This is product 4."},
   ]

   context = {
      "products": products,
   }

   return render(request,"index.html",context)
