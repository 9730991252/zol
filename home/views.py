from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'enter'in request.POST:
        room_code = request.POST.get('room_code')
        user_name = request.POST.get('user_name')
        return redirect(f'/chat/{room_code}/?user={user_name}')
    return render(request, 'home/index.html')

def chat(request , room_code):
    context = {
        'room_code' : room_code,
        'user' : request.GET.get('user')
    }
    return render(request, 'home/chat.html', context)