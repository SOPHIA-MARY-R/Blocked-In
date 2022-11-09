from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import Site
from urllib.parse import urlparse
from json import dumps
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def sites(request):
    Sites = Site.objects.all()
    return render(request, 'block/index.html', {'Sites':Sites})

def create(request):
    if request.method=='POST':
        if request.POST.get('url'):
            Sites = Site.objects.all()
            #Getting Domain name
            Link=request.POST.get('url')
            Domain_name = urlparse(Link).netloc
            isAlreadyExists=False
            for site in Sites:
                if site.domain==Domain_name:
                    isAlreadyExists=True
                    break
            if not isAlreadyExists:
                Obj=Site()
                Obj.link=Link
                Obj.domain=Domain_name
                Obj.save()
            else:
                print('Domain already blocked!')
                messages.info(request, 'Domain already blocked!')
            return render(request, 'block/create.html')
    else:
        return render(request, 'block/create.html')

'''
def update(request, id):
    site=Site.objects.get(id=id)
    Sites=Site.objects.all()
    return render(request, 'index.html', {'site': site, 'Sites':Sites})
'''

def edit(request, id):
    s = Site.objects.get(id=id)
    if request.method=='POST':
        if request.POST.get('url'):            
            Sites = Site.objects.all()
            #Getting Domain name
            Link=request.POST.get('url')
            Domain_name = urlparse(Link).netloc
            isAlreadyExists=False
            for site in Sites:
                if site.domain==Domain_name:
                    isAlreadyExists=True
                    break
            if not isAlreadyExists:
                s.link=Link
                s.domain=Domain_name
                s.save()
            else:
                print('Domain already blocked!')
                messages.info(request, 'Domain already blocked!')
            return redirect('/extension')
    return render(request, 'block/edit.html', {'site':s})

def delete(request, id):
    site = Site.objects.get(id= id)
    site.delete()
    return redirect('/extension')

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    Link = request.POST.get('url')
    Domain=urlparse(Link).netloc
    Sites = Site.objects.all()
    Obj=Site()
    list = []
    for link in Sites:
        list.append(link.domain)

    # New URL
    if Domain not in list:
        Obj.link=Link
        Obj.domain=Domain
        Obj.save()
        #_ = Site.objects.create(link=request.POST['url'], )
    
    return render(request, 'index.html', {'Sites':Sites})

def get(request):
    if request.method == 'GET':
        sites=Site.objects.all()
        List=[]
        for site in sites:
            List.append(site.domain)
        return HttpResponse(' '.join(List))
    return HttpResponse('Invalid')

