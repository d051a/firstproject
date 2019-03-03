from tokensapp.models import Token
from tokensapp.forms import TokenForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ACCOUNTING.generic.mixins import ContextPageMixin


class TokensList(ContextPageMixin, ListView):
    pagename = 'Токены'
    model = Token
    context_object_name = 'tokenslist'
    template_name = 'tokensapp/list_tokens.html'


class AddToken(ContextPageMixin, CreateView):
    pagename = 'Новый токен'
    model = Token
    form_class = TokenForm
    template_name = 'tokensapp/add_token.html'
    success_url = reverse_lazy('tokensapp:list_tokens')


class EditToken(ContextPageMixin, UpdateView):
    pagename = 'Изменение данных'
    model = Token
    form_class = TokenForm
    template_name = 'tokensapp/edit_token.html'
    success_url = reverse_lazy('tokensapp:list_tokens')


class DeleteToken(ContextPageMixin, DeleteView):
    model = Token
    success_url = reverse_lazy('tokensapp:list_tokens')
