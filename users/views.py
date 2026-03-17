from django.shortcuts import render
from sms.service import send_otp
from users.forms import SignUpForm
from django.http import HttpResponse

def register(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            email = user.email
            send_otp(email)
            return HttpResponse(f'OTP sent to {email}')

    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

