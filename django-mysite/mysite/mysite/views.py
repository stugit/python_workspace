from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'mysite/home.html')

class MysiteHomeView(generic.ListView):
    template_name = 'mysite/home.html'

    def get_queryset(self):
        return ()
