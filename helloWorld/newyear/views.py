from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
	now = datetime.datetime.now()
	context = {"newyear": now.month==1 and now.date==1}
	return render(request, "newyear/index.html", context)
