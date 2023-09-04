
from django.urls import path
from . import views
from .views import declare_winner

app_name = 'bets'

urlpatterns = [
    path('', views.BetList.as_view(), name='all'),
    path('new/', views.CreateBet.as_view(), name='create'),
    path('leaderboard/', views.Leaderboard.as_view(), name='leaderboard'),
    path('by/<username>/', views.UserBets.as_view(), name='for_user'),
    path("by/<username>/<int:pk>/",views.BetDetail.as_view(),name="single"),
    path('bet/<int:bet_id>/declare_winner', declare_winner, name='declare_winner')
]