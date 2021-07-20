from django.http import HttpResponse

def homeView(request):
	return HttpResponse('Welcome to The HomePaege!! ')
