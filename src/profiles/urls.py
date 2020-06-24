from django.urls import path
from . import auth
# from auth import MyLogin, MyLogout, MyPasswordChange, MyPasswordReset, MyPasswordResetDone, MyPasswordResetConfirm
app_name = "profiles"

urlpatterns = [
    path('login/', auth.MyLogin.as_view(), name="login"),
    path('logout/', auth.MyLogout.as_view(), name="logout"),
    path('password_change/', auth.MyPasswordChange.as_view(), name="password_change"),
    path('password_reset/', auth.MyPasswordReset.as_view(), name="password_reset"),
    path('password_change_done/', auth.MyPasswordResetDone.as_view(), name="password_change_done"),
    path('password_reset_confirm/', auth.MyPasswordResetConfirm.as_view(), name="password_reset_confirm"),
]