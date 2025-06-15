from django.shortcuts import render, redirect, get_object_or_404
from .models import NV, TS, BG
from .forms import NVForm, TSForm, BGForm

# ====== NV views ======
def nv_list(request):
    ds = NV.objects.all()
    return render(request, 'inventory/nv_list.html', {'nv_list': ds})

def nv_create(request):
    form = NVForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('nv_list')
    return render(request, 'inventory/nv_form.html', {'form': form})

def nv_update(request, pk):
    nv = get_object_or_404(NV, ma_nv=pk)
    form = NVForm(request.POST or None, instance=nv)
    if form.is_valid():
        form.save()
        return redirect('nv_list')
    return render(request, 'inventory/nv_form.html', {'form': form})

def nv_delete(request, pk):
    nv = get_object_or_404(NV, ma_nv=pk)
    if request.method == "POST":
        nv.delete()
        return redirect('nv_list')
    return render(request, 'inventory/nv_confirm_delete.html', {'object': nv})
# ====== TS views ======

def ts_list(request):
    """Danh sách tài sản"""
    ds_ts = TS.objects.all().order_by('ma_ts')
    return render(request, 'inventory/ts_list.html', {
        'ts_list': ds_ts
    })

def ts_create(request):
    """Thêm mới tài sản"""
    form = TSForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ts_list')
    return render(request, 'inventory/ts_form.html', {
        'form': form,
        'title': 'Thêm tài sản'
    })

def ts_update(request, pk):
    """Sửa thông tin tài sản"""
    ts = get_object_or_404(TS, ma_ts=pk)
    form = TSForm(request.POST or None, instance=ts)
    if form.is_valid():
        form.save()
        return redirect('ts_list')
    return render(request, 'inventory/ts_form.html', {
        'form': form,
        'title': f'Sửa tài sản {ts.ma_ts}'
    })

def ts_delete(request, pk):
    """Xóa tài sản"""
    ts = get_object_or_404(TS, ma_ts=pk)
    if request.method == 'POST':
        ts.delete()
        return redirect('ts_list')
    return render(request, 'inventory/ts_confirm_delete.html', {
        'object': ts,
        'title': f'Xác nhận xóa {ts.ten_ts}'
    })


# ====== BG views ======

def bg_list(request):
    """Danh sách bàn giao"""
    ds_bg = BG.objects.select_related('nguoi_giao', 'nguoi_nhan', 'ts')\
                     .all().order_by('-ngay_giao')
    return render(request, 'inventory/bg_list.html', {
        'bg_list': ds_bg
    })

def bg_create(request):
    """Tạo phiếu bàn giao"""
    form = BGForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bg_list')
    return render(request, 'inventory/bg_form.html', {
        'form': form,
        'title': 'Tạo phiếu bàn giao'
    })

def bg_update(request, pk):
    """Sửa phiếu bàn giao"""
    bg = get_object_or_404(BG, ma_bg=pk)
    form = BGForm(request.POST or None, instance=bg)
    if form.is_valid():
        form.save()
        return redirect('bg_list')
    return render(request, 'inventory/bg_form.html', {
        'form': form,
        'title': f'Sửa phiếu {bg.ma_bg}'
    })

def bg_delete(request, pk):
    """Xóa phiếu bàn giao"""
    bg = get_object_or_404(BG, ma_bg=pk)
    if request.method == 'POST':
        bg.delete()
        return redirect('bg_list')
    return render(request, 'inventory/bg_confirm_delete.html', {
        'object': bg,
        'title': f'Xác nhận xóa phiếu {bg.ma_bg}'
    })

def ts_detail(request, pk):
    ts = get_object_or_404(TS, ma_ts=pk)
    # Lấy phiếu bàn giao cuối cùng (theo ngày)
    last_bg = (
        BG.objects
          .filter(ts=ts)
          .select_related('nguoi_nhan', 'nguoi_giao')
          .order_by('-ngay_giao')
          .first()
    )
    return render(request, 'inventory/ts_detail.html', {
        'ts': ts,
        'last_bg': last_bg
    })
