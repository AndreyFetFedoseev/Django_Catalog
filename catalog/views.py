from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')
