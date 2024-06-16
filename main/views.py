from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'main/homepage.html')

def other_page(request):
    return render(request, 'main/other_page.html')