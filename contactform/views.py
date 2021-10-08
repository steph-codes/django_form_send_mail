from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message
        }
        # print(data)

        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '',['ogundele370@gmail.com'])
        # third param is the email address we send mail from , leaveblank (optional) ''
        return HttpResponse('Thank you for subnmitting the from, check email for confirmation')

    return render(request, 'contactform/index.html', {})