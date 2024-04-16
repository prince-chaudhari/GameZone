from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    user_game_coin = models.PositiveIntegerField(default = 0)
    profile_image = models.ImageField(null = True, blank = True, upload_to="pictures/") 

    # Game count
    snake_game_count = models.PositiveIntegerField(default = 0)
    hangman_game_count = models.PositiveIntegerField(default = 0)
    tic_tac_toe_count = models.PositiveIntegerField(default = 0)
    memory_card_game_count = models.PositiveIntegerField(default = 0)
    rock_paper_scissors_count = models.PositiveIntegerField(default = 0)
    ping_pong_count = models.PositiveIntegerField(default = 0)
    puzzle_game_count = models.PositiveIntegerField(default = 0)
    flappy_bird_count = models.PositiveIntegerField(default = 0)

    snake_game_1 = models.BooleanField(default = True)
    snake_game_2 = models.BooleanField(default = True)

    momory_card_1 = models.BooleanField(default = True)
    momory_card_2 = models.BooleanField(default = True)

    tic_tac_toe_1 = models.BooleanField(default = True)
    tic_tac_toe_2 = models.BooleanField(default = True)
    
    rock_paper_scissors_1 = models.BooleanField(default = True)
    rock_paper_scissors_2 = models.BooleanField(default = True)

    hangman_1 = models.BooleanField(default = True)
    hangman_2 = models.BooleanField(default = True)

    puzzle_1 = models.BooleanField(default = True)
    puzzle_2 = models.BooleanField(default = True)

    flappy_bird_1 = models.BooleanField(default = True)
    flappy_bird_2 = models.BooleanField(default = True)

    ping_pong_1 = models.BooleanField(default = True)
    ping_pong_2 = models.BooleanField(default = True)

    # Game Purchase
    purchase_1 = models.BooleanField(default = False)
    purchase_2 = models.BooleanField(default = False)
    purchase_3 = models.BooleanField(default = False)
    
    claim_daily_coin = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.user.username} Profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)   
        user_profile.save()     


post_save.connect(create_profile, sender=User)