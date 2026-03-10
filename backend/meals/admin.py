from django.contrib import admin
from .models import Recipe, CookingLog, MealPlan, PlannedRecipe

admin.site.register(CookingLog)
admin.site.register(MealPlan)
admin.site.register(PlannedRecipe)
admin.site.register(Recipe)