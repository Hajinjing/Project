from django.shortcuts import render
from board.models import Fboard

# Create your views here.

#db의 글 html에 뿌려주기
def blist(request):
    qs = Fboard.objects.all()
    context = {'blist':qs}
    return render(request, "blist.html", context)