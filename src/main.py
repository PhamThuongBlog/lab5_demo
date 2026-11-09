"""
Student Manager — DevOps Lab 5
Module: Main Application
"""
from student import Student


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]
    # Thêm sinh viên mới
    students = add_student(students, "SV004", "Pham Thi D", 22, "K19")

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")

    # Tìm kiếm sinh viên
    print("\n--- Tìm kiếm ---")
    search_student(students, "Van")

    # Sửa tên, tuổi và lớp của SV002
    students = update_student(
        students,
        "SV002",
        name="Tran Thi Bich",
        age=22,
        grade="K21",
    )

    # Chỉ sửa tuổi của SV001
    students = update_student(students, "SV001", age=21)

    
def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã.

    Args:
        students: Danh sách sinh viên
        keyword: Từ khóa tìm kiếm

    Returns:
        Danh sách sinh viên khớp với từ khóa
    """
    results = []
    keyword_lower = keyword.lower()

    for s in students:
        if keyword_lower in s.name.lower() or keyword_lower in s.student_id.lower():
            results.append(s)

    if results:
        print(f"🔍 Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for s in results:
            print(f"  {s}")
    else:
        print(f"❌ Không tìm thấy sinh viên nào với từ khóa '{keyword}'")

    return results

def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách.

    Args:
        students: Danh sách sinh viên hiện tại
        student_id: Mã sinh viên
        name: Họ tên
        age: Tuổi
        grade: Khóa

    Returns:
        Danh sách sinh viên đã được cập nhật
    """
    # Kiểm tra trùng mã sinh viên
    for s in students:
        if s.student_id == student_id:
            print(f"❌ Mã sinh viên {student_id} đã tồn tại!")
            return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Đã thêm sinh viên: {new_student}")
    return students

def update_student(
    students,
    student_id: str,
    name: str = None,
    age: int = None,
    grade: str = None,
):
    """Sửa sinh viên theo mã, chỉ cập nhật thông tin được truyền vào."""
    for student in students:
        if student.student_id == student_id:
            if name is not None:
                student.name = name

            if age is not None:
                student.age = age

            if grade is not None:
                student.grade = grade

            return students

    raise ValueError(f"Không tìm thấy sinh viên: {student_id}")



if __name__ == "__main__":
    main()