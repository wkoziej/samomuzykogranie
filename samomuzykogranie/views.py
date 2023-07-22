from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic


# def index(request):
#     return render(request, "index.html", )

from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


