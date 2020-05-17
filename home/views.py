from django.shortcuts import render

# Create your views here.
def redirect_to_homepage(request):
    return render(request,'index.html')