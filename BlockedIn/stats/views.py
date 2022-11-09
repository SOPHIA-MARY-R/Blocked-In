from django.shortcuts import render

def chart(request):
    return render(request, 'stats/chart.html')
