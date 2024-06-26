from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from user.models import UserProfile
from card.models import UserCardAnswer
from card.models import Card

def login_handler(request):
    """Handler for user login"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            try:
                # User might try to login with email
                user = User.objects.get(email=username)
                if user.check_password(password):
                    request.session["user_id"] = user.id
                    login(request, user)
                    return redirect("/user")
                else:
                    return render(
                        request,
                        "site_login.html",
                        {"error_message": "Invalid username or password"},
                    )
            except ObjectDoesNotExist:
                return render(
                    request,
                    "site_login.html",
                    {"error_message": "User not registered   "},
                )
        else:
            request.session["user_id"] = user.id
            login(request, user)
            return redirect("/user")
    else:
        # Render the login form
        return render(request, "site_login.html")


INITIAL_GRADE = 4


def signup_handler(request):
    """Handler for user signup"""
    if request.method == "GET":
        lan_choices = Card.LAN_ORIGIN_CHOICES
        return render(request, "site_signup.html", {"lan_choices": lan_choices})

    if request.method == "POST":
        username = request.POST["username"]
        language = request.POST["language"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        try:
            user = User.objects.get(username=username)
            # if user does exist already, try to login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # authenticated, login
                login(request, user)
                return redirect("/user")
            else:
                # not authenticated, return error
                return render(
                    request,
                    "site_signup.html",
                    {"error_message": "Username taken, please choose a new one."},
                )
        except ObjectDoesNotExist:
            # if user does not exist, create user
            if password != password2:
                return render(
                    request,
                    "site_signup.html",
                    {"error_message": "Password does not match."},
                )
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                user_profile = UserProfile.objects.create(
                    user=user,
                    email=email,
                    target_lan=language,
                    grade=INITIAL_GRADE,
                    night_mode=False,
                )
                user_profile.save()
                login(request, user)
                return redirect("/user")
        except Exception as e:
                # Handle other exceptions
                return render(request, "site_signup.html", {"error_message": f"An error occurred: {str(e)}"})

def logout_handler(request):
    """Handler for user logout"""
    logout(request)
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    return redirect("/")


def about_handler(request):
    """Handler for the about page"""
    return render(request, "site_about.html")


def calculate_current_score(user):
    """Helper function for calculating the current score of the user."""
    # TODO: Need to calculatethe score based on the language selection
    two_months_ago = datetime.now() - timedelta(days=60)
    answers = UserCardAnswer.objects.filter(user=user, timestamp__gte=two_months_ago)
    scores = sorted(
        [grade_to_score(answer.card.grade) for answer in answers], reverse=True
    )[:10]
    average_score = sum(scores) / len(scores) if scores else 0
    return average_score


def progress_handler(request):
    """Handler for the progress page"""
    if request.user.is_authenticated:
        score = calculate_current_score(request.user)
    else:
        score = 0
    return render(request, "site_progress.html", {"score": score})


def grade_to_score(grade):
    """Helper function to get the score"""
    mapping = {
        "4": 400,
        "5": 500,
        "6a": 600,
        "6a+": 625,
        "6b": 650,
        "6b+": 675,
        "6c": 700,
        "6c+": 725,
        "7a": 750,
        "7a+": 775,
        "8": 800,
    }
    return mapping.get(grade, 0)
