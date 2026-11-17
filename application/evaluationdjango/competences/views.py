from django.shortcuts import render

from django.views import generic

from .models import Skill


# Create your views here.


class IndexView(generic.ListView):
#    model = Skill
    template_name = "competences/index.html"
    context_object_name = "latest_skill_list"

    def get_queryset(self):
        return Skill.objects.all()