# main/views.py
from django.shortcuts import render
from .models import City, Country, State, Subscription, WorkoutCategory, Users
import random
def city_view(request):
    cities = City.objects.all()
    return render(request, 'city.html', {'cities': cities})

def country_view(request):
    countries = Country.objects.all()
    return render(request, 'country.html', {'countries': countries})

def payment_view(request):
    return render(request, 'payment.html')

def state_view(request):
    states = State.objects.all()
    return render(request, 'state.html', {'states': states})

def subscriptions_view(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscriptions.html', {'subscriptions': subscriptions})

def workout_categories_view(request):
    categories = WorkoutCategory.objects.all()
    return render(request, 'workout_categories.html', {'categories': categories})

def workout_exercises_view(request):
    # Assuming you have a WorkoutExercise model to show exercises
    return render(request, 'workout_exercises.html')
def home_view(request):
    # You can pass any data you want to display on the home page
    cities = City.objects.all()  # Example: list of cities
    subscriptions = Subscription.objects.all()  # Example: list of subscriptions
    return render(request, 'home.html', {
        'cities': cities,
        'subscriptions': subscriptions,
    })
def user_profile_view(request):
    if request.user.is_authenticated:  # Check if the user is logged in
        user = request.user
        subscriptions = Subscription.objects.filter(user=user)  # Assuming a relationship
        return render(request, 'user_profile.html', {
            'user': user,
            'subscriptions': subscriptions,
        })
    else:
        return render(request, 'login.html')


def users_view(request):
    # Example random user data
    users = [
        {'name': 'John Doe', 'joined_since': random.randint(2015, 2023)},
        {'name': 'Jane Smith', 'joined_since': random.randint(2015, 2023)},
        {'name': 'Mike Johnson', 'joined_since': random.randint(2015, 2023)},
        {'name': 'Emily Davis', 'joined_since': random.randint(2015, 2023)},
    ]

    context = {
        'users': users
    }

    return render(request, 'users.html', context)

