from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def process(request):
    request.session['name']= request.POST['name']
    request.session['location']= request.POST['location']
    request.session['fav_language']= request.POST['fav_language']
    request.session['comment']= request.POST['comment']
    return redirect('/info')    

def info(request):
    print('got here from redirect!')
    return render(request, 'info.html')
