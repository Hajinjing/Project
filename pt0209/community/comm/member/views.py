from django.http import JsonResponse
from django.shortcuts import redirect, render
from member.models import Member

# 회원가입1
def join01(request):
    return render(request,'join01.html')

#아이디 중복 체크
def idcheck(request):
    # ajax에서 넘어온 user_id 값
    id = request.GET.get('user_id')
    print("views id: ", id)
    # id로 존재하는지 확인
    try:
        qs = Member.objects.get(m_id = id)
    except:
        qs = None
    if qs is None:
    # result 결과를 만들어서 보냄
        context=  {'result': 'true'}
    else:
        context=  {'result': 'false'}
    return JsonResponse(context)


# 회원가입2
def join02(request):
    return render(request,'join02_in.html')

# 로그인
def login(request):
    if request.method == 'GET':
        print("view get : login")
        return render(request,'login.html')
    elif request.method =='POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("view id : ",id)
        #예외처리
        try:
            qs = Member.objects.get(m_id=id,m_pw=pw)
        except Member.DoesNotExist:
            qs = None    
        
        if qs:
            request.session['session_id'] = qs.m_id
            msg = "로그인 성공!"
            return render(request,'index.html',{'msg':msg})
        else:
            msg = "아이디와 패스워드가 일치하지 않습니다. "    
            return render(request,'login.html',{'msg':msg})
        
def logout(request):
    if request.session.get('session_id'):
        request.session.clear()
    
    return redirect('/')        
        
