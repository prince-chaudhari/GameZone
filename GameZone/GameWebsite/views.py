from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required   
from .forms import UpdateUserForm, UpdateProfileForm
import re
import os
import datetime

# Create your views here.

def home(request):
    Profile.checkUser = False
    return render(request, "GameWebsite\\html_files\\home.html")

def browse(request):
    return render(request, "GameWebsite\\html_files\\browse.html")

def contact(request):
    return render(request, "GameWebsite\\html_files\\contact.html")

@login_required(login_url="../login/")
def rewards(request):
    
    if get_daily_coin(request.user.id) or not(request.user.profile.claim_daily_coin):    
        return render(request, "GameWebsite\\html_files\\rewards.html" , {'check' : True})
    else:
        return render(request, "GameWebsite\\html_files\\rewards.html" , {'check' : False})



def get_daily_coin(user_id):
    last_received_date = load_last_received_date(user_id)
    
    print(can_get_coin(last_received_date))
    if can_get_coin(last_received_date):
        # Give the user a coin
        
        # Update the last received date
        save_last_received_date(user_id, datetime.date.today())
        return True
    return False
            

def save_last_received_date(user_id, last_received_date):
    # Save the last received date to a file
    filename = f"last_received_date_{user_id}.txt"
    with open(filename, "w") as file:
        file.write(last_received_date.isoformat())

def can_get_coin(last_received_date):
    today = datetime.date.today()
    return last_received_date != today    

def load_last_received_date(user_id):
    # Load the last received date from a file
    filename = f"last_received_date_{user_id}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            last_received_date = datetime.date.fromisoformat(file.read())
    else:
        # If the file doesn't exist, assume the user hasn't received a coin yet
        last_received_date = datetime.date(2000, 1, 1)  # Initial date
        
    return last_received_date


@login_required(login_url="../login/")
def profile(request):
    
    return render(request, "GameWebsite\\html_files\\profile.html")

@login_required(login_url="../login/")
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        # userExists = User.objects.filter(username = user_form.username)

        # if userExists.exists():
        #     messages.info(request, "Username already taken !!")
        #     return redirect('../update_profile/')

        # regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        # if not(re.fullmatch(regex, user_form.email)):
        #     messages.info(request, "Invalid Email !!")
        #     return redirect('../update_profile/')

        if user_form.is_valid() and profile_form.is_valid():
            print("HAHAHHAHHA"*34)
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect("../")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'GameWebsite\\html_files\\update_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def login_page(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username !!")
            return redirect('../login/')

        user = authenticate(username = username, password = password) 

        if user is None:
            messages.info(request, "Invalid Password !!")
            return redirect('../login/')

        else:
            login(request, user)
            return redirect("../home")

    return render(request, "GameWebsite\\html_files\\login.html")

@login_required(login_url="../login/")
def logout_page(request):
    logout(request)
    return redirect("../login/")                

def signup(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken !!")
            return redirect('../signup/')

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not(re.fullmatch(regex, email)):
            messages.info(request, "Invalid Email !!")
            return redirect('../signup/')
        elif not(validate_password(password)):
            messages.info(request, "You password must be strong !!")
            return redirect('../signup/')
        elif password != confirm_password:
            messages.info(request, "Your password and confirm password are not same !!")
            return redirect('../signup/')

        user = User.objects.create(
            username = username,
            email = email
        )

        user.profile.user_game_coin += 100
    
        user.set_password(password)
        user.save()
        user.profile.save()

        # user = User.objects.get(username=username)

        return redirect('../login/')

    return render(request, "GameWebsite\\html_files\\signup.html")

def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not re.search("[a-z]", password):  
        return False  
    if not re.search("[A-Z]", password):  
        return False  
    if not re.search("[0-9]", password):  
        return False  
    return True      

# Game Views

def snake_game(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.snake_game_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\Snake_Game.html")

def tic_tac_toe(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.tic_tac_toe_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\Tic_Tac_Toe.html")

def hangman_game(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.hangman_game_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\Hangman_Game.html")
def memory_card_game(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.memory_card_game_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\Memory_Card_Game.html")

def rock_paper_scissors(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.rock_paper_scissors_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\Rock_Paper_Scissors.html")

def flappy_bird(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.flappy_bird_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\flappy_bird_game.html")

def puzzle_game(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.puzzle_game_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\puzzle_game.html")

def ping_pong(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    # profile = Profile(user = request.user.id)
    profile.ping_pong_count += 1
    profile.save()
    return render(request, "GameWebsite\\html_files\\pong_game.html")


# Update Coins
def update_score(request, coins):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    type_of_game = coins[-1]

    c = int(coins[0:len(coins)-1])
    
    # profile = Profile(user = request.user.id)
    profile.user_game_coin += c
    
    if type_of_game == "0":
        profile.claim_daily_coin=True
    elif type_of_game == "1":
        if c == 50:
            profile.snake_game_1 = False
        elif c == 100:
            profile.snake_game_2 = False
    elif type_of_game == "2":
        if c == 50:
            profile.momory_card_1 = False
        elif c == 100:
            profile.momory_card_2 = False
    elif type_of_game == "3":
        if c == 50:
            profile.tic_tac_toe_1 = False
        elif c == 100:
            profile.tic_tac_toe_2 = False
    elif type_of_game == "4":
        if c == 50:
            profile.rock_paper_scissors_1 = False
        elif c == 100:
            profile.rock_paper_scissors_2 = False
    elif type_of_game == "5":
        if c == 50:
            profile.hangman_1 = False
        elif c == 100:
            profile.hangman_2 = False
    elif type_of_game == "6":
        if c == 50:
            profile.car_1 = False
        elif c == 100:
            profile.car_2 = False
    elif type_of_game == "7":
        if c == 50:
            profile.puzzle_1 = False
        elif c == 100:
            profile.puzzle_2 = False
    elif type_of_game == "8":
        if c == 50:
            profile.hangman_1 = False
        elif c == 100:
            profile.hangman_2 = False
    elif type_of_game == "9":
        if c == 50:
            profile.hangman_1 = False
        elif c == 100:
            profile.hangman_2 = False

    profile.save()

    return render(request, "GameWebsite\\html_files\\rewards.html")

def purchase_game(request, coins):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    type_of_game = coins[-1]

    c = int(coins[0:len(coins)-1])
    
    # profile = Profile(user = request.user.id)
    profile.user_game_coin -= c

    
    if type_of_game == "1":
        profile.purchase_1 = True
    elif type_of_game == "2":
        profile.purchase_2 = True
    elif type_of_game == "3":
        profile.purchase_3 = True

    profile.save()
    return render(request, "GameWebsite\\html_files\\browse.html")
    
