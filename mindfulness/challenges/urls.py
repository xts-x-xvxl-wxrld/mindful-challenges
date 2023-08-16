from django.urls import path
from .views import home, signIn, signUp, challenges, cabinet, makeYourChallenge, \
                savedChallenges, reflections, yourChallenges


urlpatterns = [
    path('', home, name='home'),
    path('sign-up/', signUp, name='sign_up'),
    path('sign-in/', signIn, name='sign_in'),
    path('cabinet/', cabinet, name='cabinet'),
    path('challenges/', challenges, name='challenges'),
    path('make-challenge/', makeYourChallenge, name='make_challenge'),
    path('reflections/', reflections, name='reflections'),
    path('saved-challenges/', savedChallenges, name='saved_challenges'),
    path('your-challenges/', yourChallenges, name='your_challenges'),
]