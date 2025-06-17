from django.db import models
from datetime import date


class NV(models.Model):
    ma_nv = models.CharField(max_length=10, primary_key=True)
    ho_ten = models.CharField(max_length=100)
    cong_ty = models.CharField(max_length=100)
    phong_ban = models.CharField(max_length=100)
    chuc_vu = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ma_nv} - {self.ho_ten}"

class TS(models.Model):
    ma_ts = models.CharField(max_length=10, primary_key=True)
    ten_ts = models.CharField(max_length=200)
    loai_ts = models.CharField(max_length=100)
    don_vi = models.CharField(max_length=50)
    tinh_trang = models.CharField(max_length=100)

    # Thêm mới:
    ngay_mua = models.DateField(default=date.today)
    khau_hao_nam = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"{self.ma_ts} - {self.ten_ts}"


class BG(models.Model):
    ma_bg = models.CharField(max_length=10, primary_key=True)
    nguoi_giao = models.ForeignKey(NV, related_name="bg_giao", on_delete=models.CASCADE)
    nguoi_nhan = models.ForeignKey(NV, related_name="bg_nhan", on_delete=models.CASCADE)
    ngay_giao = models.DateField()
    ts = models.ForeignKey(TS, on_delete=models.CASCADE)
    ghi_chu = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ma_bg} | {self.ts.ten_ts}"