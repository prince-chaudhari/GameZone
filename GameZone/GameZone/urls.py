"""
URL configuration for GameZone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from GameWebsite.views import * 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("home/", home),
    path("browse/", browse),
    path("contact/", contact),
    path("rewards/", rewards),
    path("profile/", profile),
    path("login/", login_page),
    path("signup/", signup),
    path("logout/", logout_page),
    path("profile/update_profile/", update_profile),

    # Games URLS
    path("browse/snake_game/", snake_game),
    path("browse/tic_tac_toe/", tic_tac_toe),
    path("browse/rock_paper_scissors/", rock_paper_scissors),
    path("browse/hangman_game/", hangman_game),
    path("browse/memory_game/", memory_card_game),
    path("browse/puzzle_game/", puzzle_game),
    path("browse/flappy_bird/", flappy_bird),
    path("browse/ping_pong/", ping_pong),

    # Update Coins
    path("rewards/<coins>", update_score, name="update_score"),

    # Purchase Game
    path("browse/<coins>", purchase_game , name="purchase_game"),

    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
