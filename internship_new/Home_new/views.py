from django.shortcuts import render

# Create your views here.
def home_new(request):
    return render(request,'index.html')



