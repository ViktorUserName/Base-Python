
from django.contrib import admin
from django.urls import path

from newmodel.views import NewModelView

from user.views import RegisterView, TokenView, MainView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NewModelView.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/token/', TokenView.as_view()),
    path('api/', MainView.as_view()),

]