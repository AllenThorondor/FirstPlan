from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'moments/index.html',{'title':'人物专题'})
