from django import forms
from .models import Meal

class MealForm(forms.ModelForm): #sublass ng forms:ModelFrom
	class Meta: #properties ng form
		model = Meal
		fields = "__all__" #lahat ng fields lagyan, food, serving size, meal time