from django. shortcuts import render

def index(request):
    return render(request, 'index.html')

def matchPage(request):
    return render(request, 'matchPage.html')

def feed(request):
    return render(request, 'feed.html')