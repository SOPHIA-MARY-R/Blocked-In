from django.http import HttpResponse
from django.shortcuts import render
from . models import Site
from urllib.parse import urlparse
from json import dumps
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def sites(request):
    Sites = Site.objects.all()
    '''
    if request.method=='POST':
        if request.POST.get('url'):
                #Getting the domain name
                X=Link.strip().split('/')
                #if protocol is http or https, then X[1] will be the www. or subdomain
                if(X[0] == "https:" or X[0] == "http:"):
                        X = X[2].split(".")
                else:
                    X=X[0].split(".")
                
                if len(X)==2:
                    Domain_name=X[0]
                else:
                    Domain_name=X[1]
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

            Dict={}
            for site in Sites:
                if site.domain not in Dict: Dict[site.domain]=''
                Dict[site.domain]=site.link
            dataJSON = dumps(Dict) 
            ''' 
    return render(request, 'index.html', {'Sites':Sites})

def edit(request):
    pass

def delete(request):
    pass

@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    Link = request.POST.get('url')
    #print('------\n'+Link+'----------')
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


@require_http_methods(['POST'])
@csrf_exempt
def load(request):
    # Get comparison rating
    Link = request.POST['url']
    # Return it as plaintext
    response = HttpResponse(content_type='text/plain')
    response.write('Saved')
    return response


def get(request):
    if request.method == 'GET':
        sites=Site.objects.all()
        List=[]
        for site in sites:
            List.append(site.domain)
        return HttpResponse(' '.join(List))
    return HttpResponse('Invalid')

