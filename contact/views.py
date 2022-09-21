from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def send_message (request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        applicant_message = request.POST.get('message')

        message = f'the sender is\n{email}.\nThe message is:\n{applicant_message}'

        print(subject,email,message)

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['org3700@gmail.com'],
            fail_silently=False,
        )

    context = {'informations':myinfo}

    return render(request,'contact/contact.html',context)