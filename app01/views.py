from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the app01 index.")

def transfer(request):
    if request.method == 'POST':
        from_ = request.POST.get('from_')
        to_ = request.POST.get('to_')
        money = request.POST.get('money')
        print('{}转给{}了{}元钱'.format(from_, to_, money))
        return HttpResponse('转账成功')
    return render(request,'zhuanzhang.html')

def test_template(request):
    name_list = ['peter','joy','','derek']
    name_list_empty = []
    from datetime import datetime
    date = datetime.now()
    script = '<a href="javascript:void(0);" onclick="alert(\'hello\')">点我</a>'
    return render(
        request,
        'test_template.html',
        {
            'name_list':name_list,
            'name_list_empty':name_list_empty,
            'file_size':123456789,
            'date':date,
            'script':script


        }
    )