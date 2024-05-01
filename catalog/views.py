import json
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'main/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('data/contacts.json', 'a', encoding='utf-8') as file:
            json.dump({'name': name, 'phone': phone, 'message': message}, file)
    return render(request, 'main/contacts.html')
