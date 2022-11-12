from django.shortcuts import render

# Create your views here.
def notes(request):
    return render(request, 'notes/notes.html')
