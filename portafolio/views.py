from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView

from .forms import UserSignUpForm, UserSignInForm
from .models import User, Blog, Portfolio, Curso


class HomeTemplateView(TemplateView):
  template_name = 'home.html'


class SignUpView(CreateView):
  model = User
  form_class = UserSignUpForm
  template_name = 'signup.html'
  success_url = reverse_lazy('portafolio:signin')

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return redirect(self.success_url)


class SignInView(LoginView):
  form_class = UserSignInForm
  template_name = 'signin.html'
  success_url = reverse_lazy('portafolio:home')

  @method_decorator(never_cache)
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect(self.success_url)
    return super().dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    return super().form_valid(form)


class SignOutView(LoginRequiredMixin, LogoutView):
  next_page = reverse_lazy('portafolio:home')

  @method_decorator(never_cache)
  def dispatch(self, request, *args, **kwargs):
    response = super().dispatch(request, *args, **kwargs)
    logout(request)
    return response


class BlogListView(LoginRequiredMixin, ListView):
  model = Blog
  template_name = 'my_blogs_Julissa.html'
  context_object_name = 'blogs'
  login_url = reverse_lazy('portafolio:signin')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['total_blogs'] = self.get_queryset().count()
    context['title'] = 'Ing. Julissa'
    return context


class BlogsDetailView(LoginRequiredMixin, DetailView):
  model = Blog
  template_name = "blog_details_Julissa.html"
  context_object_name = "blog"
  login_url = reverse_lazy('portafolio:signin')

  def get_object(self, **kwargs):
    blog_id = self.kwargs.get('blog_id')
    return get_object_or_404(Blog, pk=blog_id)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = self.object.title
    return context


class PortfolioAndCursoListView(LoginRequiredMixin, TemplateView):
  template_name = 'portafolio.html'
  login_url = reverse_lazy('portafolio:signin')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Ing. Julissa'
    context['projects'] = Portfolio.objects.all()
    context['cursos'] = Curso.objects.all()
    return context
