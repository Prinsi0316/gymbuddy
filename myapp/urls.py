# main/urls.py
from django.urls import path
from .views import (
    index_view,
    city_view,
    country_view,
    payment_view,
    state_view,
    subscriptions_view,
    workout_categories_view,
    workout_exercises_view,
    users_view,

)

urlpatterns = [
    path('', index_view, name='index_redirect'),
    path('index/', index_view, name='index'),
    path('cities/', city_view, name='cities'),
    path('countries/', country_view, name='countries'),
    path('payments/', payment_view, name='payments'),
    path('states/', state_view, name='states'),
    path('subscriptions/', subscriptions_view, name='subscriptions'),
    path('workout-categories/', workout_categories_view, name='workout_categories'),
    path('workout-exercises/', workout_exercises_view, name='workout_exercises'),
    path('users/', users_view, name='users'),


]
