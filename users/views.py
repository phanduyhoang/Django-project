from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

def verify_account(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    user.is_active = True
    user.save()

    # Generate a unique token for the user
    token_generator = default_token_generator
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)

    # Construct the verification link
    current_site = get_current_site(request)
    # Use localhost URL with correct port number
    verification_url = reverse('verify_email', kwargs={'uidb64': uid, 'token': token})
    verification_link = f"http://localhost:{settings.PORT}{verification_url}"

    # Send the verification link to the user via email
    subject = 'Activate Your Account'
    message = f'Click the following link to activate your account: {verification_link}'
    user_email = user.email
    send_mail(subject, message, 'from@example.com', [user_email])

    return redirect('login')



from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Mark user as inactive until verification
            user.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.http import HttpResponse
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('web-home')  # Return a simple HTTP response
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')