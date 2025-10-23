from django.shortcuts import render,redirect
from .models import Test
from .forms import TestForm

# Create your views here.
def index(request):
    return render(request, 'test_app/index.html')

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