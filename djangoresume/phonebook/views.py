from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from .models import Post 
from django.urls import reverse_lazy

#def home(request):
    #return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post 
    template_name = 'home.html'


class PhonebookDetailView(DetailView):
    model = Post 
    template_name = 'phonebook_detail.html'


class AddPostView(CreateView):
    model = Post 
    template_name = 'add_post.html'
    fields = ('name', 'phone_number', 'mobilephone_number', 'address')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post 
    template_name = 'update_post.html'
    fields = ('name', 'phone_number', 'mobilephone_number', 'address')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')