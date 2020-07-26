from django.shortcuts import render, redirect

def signup(request):
    return render(request, 'signup.html')

def check(request):
    return render(request, 'check.html')

def assign(request):
    if not request.POST.get('agree_a', None) == None:
        if not request.POST.get('agree_b', None) == None:
            return redirect('signup')
        else:
            return render(request, 'check.html')
    else:
        return render(request, 'check.html')


