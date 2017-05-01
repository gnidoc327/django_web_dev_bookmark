from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
