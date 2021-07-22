from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Flim , Commercial
from .forms import MovieSelectForm,FilmModelForm,CommercialModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MovieSelectFormView(LoginRequiredMixin,FormView):
	form_class = MovieSelectForm
	template_name = 'movies/main.html'
	success_url = reverse_lazy('movies:add-movie-view')

	def post(self,*args,**kwargs):
		self.request.session['movie'] = self.request.POST.get('movie').lower().capitalize()
		print(self.request.POST.get('movie'))
		return super().post(*args,**kwargs)



class AddMovieFormView(LoginRequiredMixin,FormView):
	template_name ='movies/add.html'
	success_url =reverse_lazy('homeView')

	def get_form_class(self,*args,**kwargs):
		movie = self.request.POST.get('movie')
		if movie =='Flim':
			return FilmModelForm
		else:
			return CommercialModelForm

	def form_valid(self,form):
		form.save()
		return super().form_valid(form )

