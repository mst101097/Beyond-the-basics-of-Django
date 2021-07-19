from django.contrib import admin
# Register your models here.
from .models import Movie,Flim,Commercial
from actors.models import Actor

# admin.site.register(Movie)
class FlimModelAdmin(admin.ModelAdmin):
	def render_change_form(self,request,context,*args,**kwargs):
		context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(is_star = True)
		return super().render_change_form(request,context,*args,**kwargs)



class CommercialModelAdmin(admin.ModelAdmin):
	def render_change_form(self,request,context,*args,**kwargs):
		context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(is_star = False)
		return super().render_change_form(request,context,*args,**kwargs)



admin.site.register(Flim,FlimModelAdmin)
admin.site.register(Commercial,CommercialModelAdmin)
