from django.http import HttpResponse

# Create your views here.
def vistaPaginaInicio(request):
	return HttpResponse('¡Hola Edmundo, Raymundo, Segismundo!')
