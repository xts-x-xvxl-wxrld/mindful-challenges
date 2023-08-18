from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ReflectionForm, CustomChallengeForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Challenge, Reflection, CustomChallenge
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='sign_in')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='sign_in')
def cabinet(request):
    return render(request, 'cabinet.html')


@login_required(login_url='sign_in')
def challenges(request):
    challengesList = list(Challenge.objects.all())
    current_index = request.session.get('current_challenge_index', 0)
    reflection_form = ReflectionForm()

    if current_index >= len(challengesList) or current_index < 0:
        messages.info(request, 'You have completed all challenges')
        request.session['current_challenge_index'] = 0
        current_index = request.session.get('current_challenge_index')

    challengeObj = challengesList[current_index]

    if request.method == 'POST':
        if 'next-challenge' in request.POST:
            request.session['current_challenge_index'] = current_index + 1
            return redirect('challenges')
        elif 'reflection_submit' in request.POST:
            reflection_form = ReflectionForm(request.POST)
            if reflection_form.is_valid():
                reflection = reflection_form.save(commit=False)
                reflection.user = request.user
                reflection.challenge = challengeObj
                reflection.save()
                messages.info(request, 'Your reflection has been saved in your cabinet')
                request.session['current_challenge_index'] = current_index + 1
                return redirect('challenges')
            else:
                print('form invalid')

    return render(request, 'challenges.html', {'challenge': challengeObj, 'reflection_form': reflection_form})


@login_required(login_url='sign_in')
def makeYourChallenge(request):
    if request.method == 'POST':
        form = CustomChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.user = request.user
            challenge.save()
            messages.info(request, 'Your meditation challenge has been saved in your cabinet')
            return redirect('saved_challenges')
    else:
        form = CustomChallengeForm()

    return render(request, 'make_challenge.html', {'form': form})


@login_required(login_url='sign_in')
def savedChallenges(request):
    return render(request, 'saved_challenges.html')


@login_required(login_url='sign_in')
def yourChallenges(request):
    user = request.user
    allChallenges = CustomChallenge.objects.filter(user=user)
    current_index = request.session.get('current_custom_challenge_index', 0)

    challengeObj = None

    if allChallenges.exists():
        if current_index >= len(allChallenges) or current_index < 0:
            request.session['current_custom_challenge_index'] = 0
            current_index = request.session['current_custom_challenge_index']

        challengeObj = allChallenges[current_index]

    if request.method == 'POST':
        if 'next-challenge' in request.POST:
            request.session['current_custom_challenge_index'] = current_index + 1
            return redirect('your_challenges')
        elif 'previous-challenge' in request.POST:
            request.session['current_custom_challenge_index'] = current_index - 1
            return redirect('your_challenges')

    return render(request, 'your_challenges.html', {'challengeObj': challengeObj})


@login_required(login_url='sign_in')
def reflections(request):
    reflectionsAll = Reflection.objects.filter(user=request.user)

    current_index = request.session.get('current_reflection_index', 0)

    challenge = None
    reflectionText = None
    reflectionDate = None

    if reflectionsAll.exists():
        if current_index >= len(reflectionsAll) or current_index < 0:
            request.session['current_reflection_index'] = 0
            current_index = request.session['current_reflection_index']

        reflection = reflectionsAll[current_index]
        challengePk = reflection.challenge.pk
        challenge = Challenge.objects.get(pk=challengePk)

        reflectionText = reflection.reflection_text
        reflectionDate = reflection.date_created

    if request.method == 'POST':
        if 'next-reflection' in request.POST:
            request.session['current_reflection_index'] = current_index + 1
            return redirect('reflections')
        elif 'previous-reflections' in request.POST:
            request.session['current_reflection_index'] = current_index - 1
            return redirect('reflections')

    return render(request, 'reflections.html', {'challenge': challenge,
                                                'reflectionText': reflectionText,
                                                'reflectionDate': reflectionDate})


def signIn(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})


def signUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        form = CustomUserCreationForm()

    return render(request, 'sign_up.html', {'form': form})
