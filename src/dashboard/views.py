from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from .models import Book


class BookDetail(DetailView):
    model = Book

    def get_context_data(self, *args, **kwargs):
        return super(BookDetail, self).get_context_data(*args, **kwargs)


class LoginRequiredMixin(object):
    # @classmethod
    # def as_view(cls, **kwargs):
    #     view = super(LoginRequiredMixin, cls).as_view(**kwargs)
    #     return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class DashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *arg, **kwargs):
        context = super(DashboardTemplateView, self).get_context_data(*arg, **kwargs)
        context['title'] = "This is title"
        return context


class MyView(LoginRequiredMixin, ContextMixin, TemplateResponseMixin, View):
    @method_decorator(login_required)  # work for get only
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'Some title here'
        return self.render_to_response(context)

        # @method_decorator(login_required)
        # def dispatch(self, request, *args, **kwargs):
        #     return super(MyView, self).dispatch(request, *args, **kwargs)
