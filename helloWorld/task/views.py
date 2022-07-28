from django.shortcuts import render

# Create your views here.
tasks=['foo', 'bar', 'bazz']

def index(request):
	contex = {
		"tasks": tasks
	}
	return render(request, "task/index.html", contex)