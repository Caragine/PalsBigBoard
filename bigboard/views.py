from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

class HomePage(TemplateView):
    template_name = 'bets/bet_list.html'

class WelcomePage(TemplateView):
    template_name = 'welcome.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

