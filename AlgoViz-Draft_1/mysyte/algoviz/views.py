from django.shortcuts import render
from .models import Algorithm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Algorithm, AlgorithmCategory

def home(request):
    return render(request, 'algoviz/home.html')

def about(request):
    return render(request, 'algoviz/about.html')

# def terminal(request):
#     return render(request, 'algoviz/terminal.html')

def docs(request):
    context = {
        'algorithms': Algorithm.objects.all(),
        'algorithmscategory' : AlgorithmCategory.objects.all(),
    }
    a=  AlgorithmCategory.objects.all()
    print("asd")
    return render(request, 'algoviz/docs.html', context)

class AlgoListView(ListView):
    model = Algorithm
    template_name = 'algoviz/docs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'algorithms'
    ordering = ['-date_posted']


class AlgoDetailView(DetailView):
    model = Algorithm


class AlgoCreateView(LoginRequiredMixin, CreateView):
    model = Algorithm
    fields = ['name', 'description', 'code', 'category']

    def form_valid(self, form):
        form.instance.contributor = self.request.user
        return super().form_valid(form)


class AlgoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Algorithm
    fields = ['name', 'description', 'code', 'category']

    def form_valid(self, form):
        form.instance.contributor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.contributor:
            return True
        return False
    
class AlgoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Algorithm
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.contributor:
            return True
        return False


def about(request):
    return render(request, 'algoviz/about.html', {'title': 'About'})
