from django.shortcuts import render,redirect
from .models import Test
from .forms import TestForm

# Create your views here.
def index(request):
    tests = Test.objects.all()
    context = {
        'tests' : tests
    }
    return render(request, 'test_app/index.html', context)

def create(request):
    if request.method =='POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save()
            return redirect('test_app:detail', test.pk)
    else:
        form = TestForm()
    context = {
        'form' : form
    }
    return render(request, 'test_app/create.html', context)

def detail(request, test_pk):
    test = Test.objects.get(pk=test_pk)
    context = {
        'test' : test
    }
    return render(request, 'test_app/detail.html', context)

def delete(request, test_pk):
    test = Test.objects.get(pk=test_pk)
    if request.method == "POST":
        test.delete()
        return redirect('test_app:index')
    else:
        return redirect('test_app:detail', test_pk)

def update(request, test_pk):
    test = Test.objects.get(pk=test_pk)
    if request.method == "POST":
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save()
            return redirect('test_app:detail', test_pk)
    else:
        form = TestForm(instance=test)
    context = {
        'tests' : test,
        'form' : form
    }
    return render(request, 'test_app/update.html', context)