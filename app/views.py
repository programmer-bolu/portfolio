from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from . import models
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.
def home(request):
    data = models.addUserData.objects.first()
    
    content = {
        'name' : data.full_name,
        'whyoards' : data.who_you_are_description,
        'ye1' : data.your_experience_1,
        'ye2' : data.your_experience_2,
        'ye3' : data.your_experience_3,
        'yff1' : data.your_frontend_framework_1,
        'yff2' : data.your_frontend_framework_2,
        'ybf1' : data.your_backend_framework_1,
        'ybf2' : data.your_backend_framework_2,
        'yf1' : data.your_fullstack_framework_1,
        'yf2' : data.your_fullstack_framework_2,
        'ysub' : data.your_specialty,
        'testimo': data.testimony,
        'tess' : data.testimony_sharer,
        'tesp' : data.testimony_sharer_position,
        'faq1' : data.frequently_asked_question_1,
        'faqa1' : data.frequently_asked_question_answer_1,
        'faq2' : data.frequently_asked_question_2,
        'faqa2' : data.frequently_asked_question_answer_2,
        'faq3' : data.frequently_asked_question_3,
        'faqa3' : data.frequently_asked_question_answer_3,
        'address': data.your_address,
        'contact': data.your_contact,
        'email': data.your_email 
    }
    return render(request, 'templates/index.html', content)

def contact(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        mess = f"""{name}
                   {email}
                   {message}"""
                   
        is_success = False
        is_error = False
        try:
            send_mail(
                subject = subject,
                message= mess ,
                from_email={settings.EMAIL_HOST_USER},
                recipient_list=[email],
                fail_silently=  False
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            print('Email Failed')
            messages.error(request, e)
        else:
            is_success = True
            print('Email has been sent out successfully')
            messages.success(request, 'Email sent successfully')
        
        
    return redirect(home)