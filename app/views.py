from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    context = {
        'course_title':'Django Course',
        'current_date': datetime.now(),
        'user' : {
            'name':'Anant',
            'email': 'anant372003@gmail.com',
        
        },
        'product_price':9999.999999,
        'random_text': 'wanna run and explore your Django database in VS Code like a pro? Say less! I got you covered step-by-step',

    }

    return render(request,"index.html",context)
