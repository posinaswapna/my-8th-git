from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'swapna','batch':'django'}
    return render(request,'looping.html',d)