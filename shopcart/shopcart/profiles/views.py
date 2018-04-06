from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
# from allauth.account.signals import password_changed
# from django.dispatch import receiver
# from django.contrib import messages

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)


@login_required
def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context )

@login_required
def dashboard(request):
    user = request.user
    context = {'user': user}
    template = 'dashboard.html'
    return render(request,template,context )


# @login_required
# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, 'You have Successfully changed your Password!.')
#             return redirect('settings:password')
#         else:
#             messages.warning(request, 'Please correct the error below.')  # <-
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'accounts/password_change.html', {'form': form})


# @receiver(password_changed)
# def password_change_callback(sender, request, user, **kwargs):
#     messages.success(request, 'You have Successfully changed your Password!.')
