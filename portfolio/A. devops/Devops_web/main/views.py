from django.shortcuts import render

# Create your views here.
def home(request):
    
    context = {'user': request.user}  # user 객체를 context에 추가
    print(context)
    return render(request, 'home.html', context)