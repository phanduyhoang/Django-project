from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import InfoForm
# Create your views here.


posts=[
    {
        'author':'Engenius admin',
        'title':'First new',
        'content':'First content',
        'date_posted':'August 27,2018'
    },
        {
        'author':'Engenius admin',
        'title':'First new',
        'content':'First content',
        'date_posted':'August 28,2018'
    }
]


def home(request):
    return render(request, 'web/home.html')

def about(request):
    return HttpResponse('<h1>About</h1>')

def news(request):
    context={
        'posts':posts
    }
    return render(request, 'web/news.html',context)

def info_form_view(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            
            
            subject = 'New Form Submission'
            message = 'A new form has been submitted.'
            from_email = 'phan@poppysound.ru'  # Replace with your email
            recipient_list = ['pdhoang2805@gmail.com']  # Replace with the recipient's email

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            return HttpResponse('<h1>Got You!</h1>')  # Redirect to a success page
    else:
        form = InfoForm()

    return render(request, 'web/info_form.html', {'form': form})
