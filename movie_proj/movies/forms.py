from django import forms
from .models import Flim, Commercial
from actors.models import Actor


MOVIE_CHOICE = (
	('FILM','Flim'),
	('COMMERCIAL','Commercial'),

	)


class MovieSelectForm(forms.Form):
	movie = forms.ChoiceField(choices =MOVIE_CHOICE ,widget =forms.RadioSelect(attrs = {'class':'radio_1'}))


class FilmModelForm(forms.ModelForm):
	actors = forms.ModelMultipleChoiceField(label ='Select all Actors ',widget = forms.SelectMultiple,queryset = Actor.objects.filter(is_star = True))

	class Meta:
		model = Flim
		fields = '__all__'


class CommercialModelForm(forms.ModelForm):
	actors = forms.ModelMultipleChoiceField(label ='Select all Actors ',widget = forms.SelectMultiple,queryset = Actor.objects.filter(is_star = False))
	class Meta:
		model = Commercial
		fields = '__all__'



