from django.http import HttpResponse
# from .settings import MEDIA_URL

def index(request):
    html = "<html><body><h1 style='text-align:center'>Coming Soon!<h1></body></html>"

    return HttpResponse(html)