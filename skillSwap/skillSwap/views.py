from django. shortcuts import render

def index(request):
    return render(request, 'index.html')

def matchPage(request):
    return render(request, 'matchPage.html')

def feed(request):
    user = request.user
    context={
        'user':user
    }
    return render(request, 'feed.html', context)