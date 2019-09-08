from django.shortcuts import render
from django.http import HttpResponse
from .models import Food, Meal
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import MealForm

# Create your views here.

def index(request): #request ay contant
    template = 'list.html' #name of template
    meals = Meal.objects.all() #variable would contain all your meal objects
    context = {
         'meals': meals, #variables : variable na may object
    }
    return render(request, template, context)

def add_meal(request):
	template = "add_meal.html" #anong ggmitin na html file

	if request.method == "POST": #mas clear kasya get
		form = MealForm(request.POST) #tawagin ung forms
		if form.is_valid(): #check if character/integer ung variable
			form.save()
		return HttpResponseRedirect(reverse_lazy('food:index')) #redirect user to index page , namespace:name of url
	else:
		context = {
			'meal_form': MealForm(), #blankong meal form, prompt si user
		}
	return render(request, template, context) #balik si user sa index page

def delete_meal(request, meal_id):
	meal = Meal.objects.get(id=int(meal_id))
	meal.delete()
	return HttpResponseRedirect(reverse_lazy('food:index'))

def update_meal(request, meal_id):
	template = "update_meal.html"
	meal = Meal.objects.get(id=int(meal_id))

	if request.method == "POST":
		form = MealForm(request.POST, instance=meal)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
		context = {
			'meal_form': MealForm(instance=meal),
		}
	return render(request, template, context)

def view_meal(request, meal_id):
	template = "view_meal.html"
	meal = Meal.objects.get(id=int(meal_id))
	context = {
			'meal':meal,
	}
	return render(request, template, context)

def login(request):
	if request.user.is_authenticated:
	    return HttpResponseRedirect(reverse_lazy('food:index')) #dest page, kpag tama ung username and pass
	else:
	    return HttpResponseRedirect(reverse_lazy('auth_login')) #login parin