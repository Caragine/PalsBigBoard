from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from . import models
from . import forms
from bets.models import Bet
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from accounts.models import UserBalance


User = get_user_model()

class BetList(generic.ListView):
    model = models.Bet
    template_name = 'bets/bet_list.html'

    def get_queryset(self):
        return Bet.objects.all().order_by("-create_date")
    
class UserBets(generic.ListView):
    model = models.Bet
    template_name = 'bets/user_bet_list.html'

    def get_queryset(self):
        try:
            self.bet_bettor1 = User.objects.get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.bet_bettor1.bettor1.all() | self.bet_bettor1.bettor2.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bettor1"] = self.bet_bettor1
        return context
    
class BetDetail(generic.DetailView):
    model = models.Bet
    template_name = 'bets/bet_detail.html'
        
class Leaderboard(generic.ListView):
    model = models.Bet
    template_name = 'bets/leaderboard.html'

    def get_queryset(self):
        return User.objects.all().order_by("-userbalance__balance")
    
class CreateBet(LoginRequiredMixin, generic.CreateView):
    fields = ('bettor2', 'bet_description', 'bettor1risk', 'bettor2risk')
    model = models.Bet

    class Meta:
        model = models.Bet
        labels = {'bettor1risk': "My Risk"}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.bettor1 = self.request.user
        self.object.save()
        return super().form_valid(form)

@user_passes_test(lambda u: u.is_superuser)    
def declare_winner(request, bet_id):
    bet = get_object_or_404(Bet, pk=bet_id)
    users = [bet.bettor1, bet.bettor2]
    original_create_date = bet.create_date

    if request.method == 'POST':
        winner_id = request.POST.get('winner')
        loser_id = request.POST.get('loser')
        if winner_id and loser_id:
            winner = User.objects.get(pk=winner_id)
            loser = User.objects.get(pk=loser_id)

            bet.winner = winner
            bet.loser = loser
            bet.settled = True
            bet.save()
            bet.create_date = original_create_date

            if winner == bet.bettor1:
                winner_balance, _ = UserBalance.objects.get_or_create(user=winner)
                loser_balance, _ = UserBalance.objects.get_or_create(user=loser)

                winner_balance.balance += bet.bettor2risk
                loser_balance.balance -= bet.bettor2risk
                winner_balance.save()
                loser_balance.save()
            else:
                winner_balance, _ = UserBalance.objects.get_or_create(user=winner)
                loser_balance, _ = UserBalance.objects.get_or_create(user=loser)

                winner_balance.balance += bet.bettor1risk
                loser_balance.balance -= bet.bettor1risk
                winner_balance.save()
                loser_balance.save()
            return redirect('bets:all')
    return render(request, 'bets/declare_winner.html', {'bet': bet, 'users': users})