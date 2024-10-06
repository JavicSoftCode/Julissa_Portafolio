from django.urls import path

from .views import SignInView, SignUpView, SignOutView, HomeTemplateView, BlogListView, BlogsDetailView, PortfolioAndCursoListView

app_name = 'portafolio'

urlpatterns = [
  # Home
  path('', HomeTemplateView.as_view(), name='home'),

  # Accounts
  path('signup/', SignUpView.as_view(), name='signup'),
  path('signin/', SignInView.as_view(), name='signin'),
  path('signout/', SignOutView.as_view(), name='signout'),

  # Blogs
  path('blog/', BlogListView.as_view(), name='blog_list'),
  path('blog/<int:blog_id>/', BlogsDetailView.as_view(), name='blog_details'),

  # Portfolio y Curso
  path('portfolio/', PortfolioAndCursoListView.as_view(), name='portfolio_and_projects'),
]
