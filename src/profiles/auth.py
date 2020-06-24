from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView


class MyLogin(LoginView):
    template_name ='registration/login.html'

class MyLogout(LogoutView):
    template_name = 'registration/logout.html'

#class MyPasswordChange(PasswordChangeView):
#    template_name ='registration/change-password.html'

#class MyPasswordReset(PasswordResetView):
#    template_name ='registration/password_reset_form.html'

#class MyPasswordResetDone(PasswordResetDoneView):
#    template_name='registration/password_reset_done.html'