from django.contrib import admin
from .models import NV, TS, BG

@admin.register(NV)
class NVAdmin(admin.ModelAdmin):
    list_display = ('ma_nv','ho_ten','cong_ty','phong_ban','chuc_vu')

@admin.register(TS)
class TSAdmin(admin.ModelAdmin):
    list_display = ('ma_ts','ten_ts','loai_ts','don_vi','tinh_trang')

@admin.register(BG)
class BGAdmin(admin.ModelAdmin):
    list_display = ('ma_bg','nguoi_giao','nguoi_nhan','ngay_giao','ts')
    list_filter = ('ngay_giao',)