from django.shortcuts import render, get_object_or_404
from .models import CapsuleToy

def toy_list(request):
    toys = CapsuleToy.objects.all()
    use_official_images = False  # 公式画像の使用を一時的に無効化
    return render(request, 'toys/toy_list.html', {'toys': toys, 'use_official_images': use_official_images})

def toy_detail(request, toy_id):
    toy = get_object_or_404(CapsuleToy, id=toy_id)
    use_official_images = False  # 公式画像の使用を一時的に無効化
    return render(request, 'toys/toy_detail.html', {'toy': toy, 'use_official_images': use_official_images})
