
from django.urls import path
from . import views
urlpatterns=[
    # path('account/',include('account.urls'))
    path('',views.login_view,name="login_page")
]