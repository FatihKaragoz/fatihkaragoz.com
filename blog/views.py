from django.shortcuts import render,redirect
from django.views import generic
# Create your views here.

def Forward(request):
    return redirect('blog:aboutme')

class IndexView(generic.TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

class AboutMeView(generic.TemplateView):
    template_name = 'aboutus.html'

    def get_context_data(self, **kwargs):
        context = super(AboutMeView,self).get_context_data(**kwargs)
        return context


def AboutForward(request):
    return redirect('blog:aboutme')

