from modules.functions import StudentManager
def main_menu():
    manager = StudentManager()

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
        print("1. Xem danh sach sinh vien")
        print("2. Them sinh vien")
        print("3. Tim kiem sinh vien")
        print("4. Xoa sinh vien")
        print("5. Thoat chuong trinh\n")
        choice = input("Lua chon cua ban (1-5): ")

        if choice == '1':
            manager.show_all_students()
        elif choice == '2':
            manager.add_student()
        elif choice == '3':
            manager.find_student_by_id()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            print("Dang thoat chuong trinh")
            break
        else:
            print("Khong hop le")

if __name__ == "__main__":
    main_menu()