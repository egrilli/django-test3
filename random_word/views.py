from django.shortcuts import render, HttpResponse,redirect
from django.utils.crypto import get_random_string


def index(request):

    if 'busquedas' not in request.session:
        request.session['busquedas'] = 0

    request.session['busquedas'] += 1
    letras_random= get_random_string(length=14)
    context={
        'letras_random':letras_random
    }
    return render(request,"index.html",context)
    
def random(request):
    return redirect("/app")
        
    
def delete(request):
    del request.session['busquedas']
    return redirect("/app")
