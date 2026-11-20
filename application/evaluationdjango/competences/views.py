from django.shortcuts import render

from django.views import generic

from .models import Skill, User, Activity, Slot

from itertools import chain

# Create your views here.


class IndexView(generic.ListView):
#    model = Skill
    template_name = "competences/index.html"
    context_object_name = "item_list"

    def get_queryset(self):
        skills = Skill.objects.all()
        slots = Slot.objects.all()
        test = chain(skills, slots)
        return list(test)
        #return list(chain(skills, slots))