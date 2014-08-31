from django.shortcuts import render_to_response

def index(request):
    return render_to_response('home.html')
    
def shred(request):
    return render_to_response('shred.html')