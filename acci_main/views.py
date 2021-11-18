from django.shortcuts import render
from . models import Branches, Home, Devotion
from django.views.generic import ListView, DetailView


# def home(request):
#     obj = Home.objects.all()
#     content = {
#         "obj": obj
#     }
#     return render(request, "acci_main/home.html", content)


class Home(ListView):
    template_name = "acci_main/home.html"
    context_object_name = 'home'
    paginate_by = 3
    model = Home


class DevotionList(ListView):
    template_name = "acci_main/devotionlist.html"
    context_object_name = 'devotions'
    paginate_by = 2

    def get_queryset(self):
        return Devotion.objects.order_by('-date')


class DevotionView(DetailView):
    model = Devotion
    template_name="acci_main/devotiondetail.html"
    context_object_name = 'devotiondetail'


class Branch(ListView):
    template_name = "acci_main/branches.html"
    context_object_name = 'branches'
    paginate_by = 3
    model = Branches

    def get_queryset(self):
        return self.model.objects.order_by('-branch_name')

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(
                branch_name__contains=query)
        else:
            object_list = self.model.objects.order_by('branch_name')
        return object_list


# def branches(request):
#     return render(request, 'acci_main/branches.html')

def contact(request):
    return render(request, 'acci_main/contact.html')
