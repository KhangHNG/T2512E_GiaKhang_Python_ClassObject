
from models.HinhChuNhat import HinhChuNhat
from models.NhanVien import NhanVien
from models.Oto import Oto
from models.TaiKhoanNganHang import TaiKhoanNganHang

def main_menu():
    # Bai 1

    hcn1 = HinhChuNhat(5, 3)
    hcn2 = HinhChuNhat(10, 4)
    print(f"{hcn1.tinh_dien_tich()}")
    print(f"{hcn2.tinh_dien_tich()}")

    # Bai 3

    nv1 = NhanVien("Khang", "10000000")
    nv2= NhanVien("Duong", "8000000")
    print(f"{nv1.cong_ty}_{nv1.ten}_{nv1.luong}")
    print(f"{nv2.cong_ty}_{nv2.ten}_{nv2.luong}")

    # Bai 4

    p = TaiKhoanNganHang("Khang", 5000)
    p.nap_tien(1000000)
    p.xem_so_du()

    # Bai 5

    xeVinfast = Oto()
    print(f"{xeVinfast.so_banh_xe}")

    xeVinfast.so_banh_xe = 3
    print(f"{xeVinfast.so_banh_xe}")
    
if __name__ == "__main__":
    main_menu()