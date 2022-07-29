from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

class CreateNewFom(forms.Form):
	task= forms.CharField(label = "New Task")

def index(request):
	
	if "tasks" not in request.session:
		request.session["tasks"]=[]

	
	context = {
		"tasks": request.session["tasks"]
	}
	return render(request, "task/index.html", context)

def add(request):
	if request.method=="POST":
		form = CreateNewFom(request.POST)
		if form.is_valid():
			task = form.cleaned_data["task"]
			request.session["tasks"] +=[task]
			return HttpResponseRedirect(reverse("task:index"))
		else:
			return render(request, "task/add.html", {"form": form})
	context={
		"form": CreateNewFom()
	}
	return render(request, "task/add.html", context)