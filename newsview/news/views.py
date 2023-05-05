from django.shortcuts import render
from django.views.generic import DetailView, ListView
from datetime import datetime
from .models import *

class PostList(ListView):
    model = Post
    context_object_name = 'postlist'
    # template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class PostDetail(DetailView):
    model = Post
    context_object_name = 'postdetail'
    ordering = '-dateCreation'



