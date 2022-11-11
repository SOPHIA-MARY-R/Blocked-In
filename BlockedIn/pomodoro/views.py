from django.shortcuts import render

def pomodoro(request):
    return render(request, 'pomodoro/pomodoro.html')
