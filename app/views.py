from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from app.models import (
    GeneralInfo,
    Service,
    Testinomial,
    FrequentlyAskedQuestion,
    ContactFormLog,
    Blog,
    )



# Create your views here.
def index(request):

   general_info = GeneralInfo.objects.first()
   
   services = Service.objects.all()

   testinomials = Testinomial.objects.all()

   faqs = FrequentlyAskedQuestion.objects.all()

   recent_blogs = Blog.objects.all().order_by('-created_at')[:3]  # Get the 3 most recent blogs

   for blog in recent_blogs:
       print(f"Blog : {blog }")
       print(f"blog.created_at : {blog.created_at }")
       print(f"blog.author : {blog.author }")
       print(f"blog.author.country : {blog.author.country }")
       


   context = {
       "location": general_info.location,
       "email": general_info.email,
       "phone": general_info.phone,
       "company_name": general_info.company_name,
       "open_hours": general_info.open_hours,
       "video_url": general_info.video_url,
       "twitter_url":general_info.twitter_url,
       "facebook_url":general_info.facebook_url,
       "instagram_url":general_info.instagram_url,
       "linkedin_url":general_info.linkedin_url,
       
       "services" : services,

       "testinomials" : testinomials,

       "faqs" : faqs,
       
       "recent_blogs": recent_blogs,

   }

   print(f"Context : { context }")

   return render(request, "index.html", context)


def contect_form(request):
   
    if request.method == 'POST':
        print("\n USer has submit a contact form \n")
        print(f"request.POST: {request.POST}")
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')

        context = {
            'name': name,
            'email': email,
            'message': message,
            'subject': subject,
        }
        html_content = render_to_string('email.html', context)

        is_success = False
        is_error = False
        error_message = ""

        try:

            send_mail(
                subject=subject,
                message=None,
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request, "There is an error, please try again later")
        
        else:
            is_success = True
            messages.success(request, "Your message has been sent successfully!")


        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_success=is_success,
            is_error=is_error,
            error_message=error_message,

        )
            

    if request.method == 'GET':
        print("\n User has acess the contact view by url\n")

    return redirect('home')