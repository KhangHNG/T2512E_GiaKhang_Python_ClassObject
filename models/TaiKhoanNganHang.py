class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du=0):
        self.chu_tai_khoan = chu_tai_khoan
        self.so_du = so_du

    def nap_tien(self, so_tien):
        if so_tien <= 0:
            print("Khong du tien")
        self.so_du += so_tien

    def xem_so_du(self):
        print(f"So du tai khoan: {self.so_du}")