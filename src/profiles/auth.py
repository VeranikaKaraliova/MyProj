from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView


class MyLogin(LoginView):
    template_name ='templates/registration/login.html'
    

class MyLogout(LogoutView):
    template_name = 'templates/registration/logout.html'

class MyPasswordChange(PasswordChangeView):
    template_name ='templates/registration/password_change.html'

class MyPasswordReset(PasswordResetView):
    template_name ='templates/registration/password_reset_form.html'

class MyPasswordResetDone(PasswordResetDoneView):
    template_name='templates/registration/password_reset_done.html'

class MyPasswordResetConfirm(PasswordResetConfirmView):
    template_name='templates/registration/password_onfirm.html'