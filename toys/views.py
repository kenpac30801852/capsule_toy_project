from django.shortcuts import render, get_object_or_404
from .models import CapsuleToy

def toy_list(request):
    toys = CapsuleToy.objects.all()
    return render(request, 'toys/toy_list.html', {'toys': toys})

def toy_detail(request, toy_id):
    toy = get_object_or_404(CapsuleToy, id=toy_id)
    return render(request, 'toys/toy_detail.html', {'toy': toy})

def no_official_info(request):
    return render(request, 'toys/no_official_info.html')  # 公式情報なしページ
