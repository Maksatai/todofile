from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, 'index.html')
    
def test(request):
    return render(request, 'test.html')

def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')
     