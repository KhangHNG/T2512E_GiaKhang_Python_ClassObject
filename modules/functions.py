from models.student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\nThem sinh vien")
        sid = input("Nhap ma sv: ")
        name = input("Nhap ten sv: ")
        age = input("Nhap tuoi sv: ")
        major = input("Nhap chuyen nganh: ")
        new_student = Student(sid, name, age, major)
        self.students.append(new_student)
        print("Them moi thanh cong\n")

    def show_all_students(self):
        print("\nDanh sach sinh vien\n")
        if not self.students:
            print("Danh sach trong")
        else:
            for st in self.students:
                print(st)

    def find_student_by_id(self):
        sid = input("\nNhap ma sinh vien can tim: ")
        for st in self.students:
            if st.student_id == sid:
                print(st)
                return
        print("Khong tim thay sinh vien voi ma nay\n")

    def delete_student(self):
        sid = input("\nNhap ma sinh vien can xoa: ")
        for st in self.students:
            if st.student_id == sid:
                self.students.remove(st)
                print("Xoa thanh cong\n")
                return
        print("Khong tim thay sinh vien voi ma nay\n")