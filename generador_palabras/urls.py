from django.urls import path,include

urlpatterns = [
    path('app/',include('random_word.urls')),
]
