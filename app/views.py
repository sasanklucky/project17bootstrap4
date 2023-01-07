from django.shortcuts import render

# Create your views here.
def mdbdown(request):
    return render(request,'mdbdown.html')