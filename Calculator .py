"""
Calculator
โปรแกรมเครื่องคิดเลข แบ่งการทำงานออกเป็นฟังก์ชันย่อย
"""


def add(a, b):
    """บวก"""
    return a + b


def subtract(a, b):
    """ลบ"""
    return a - b


def multiply(a, b):
    """คูณ"""
    return a * b


def divide(a, b):
    """หาร (ตรวจสอบการหารด้วยศูนย์)"""
    if b == 0:
        raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
    return a / b


def get_number(prompt):
    """รับค่าตัวเลข (float) จากผู้ใช้ พร้อมตรวจสอบความถูกต้อง"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")


def show_menu():
    """แสดงเมนูตัวเลือกการคำนวณ"""
    print("\n=== เครื่องคิดเลข ===")
    print("1. บวก (+)")
    print("2. ลบ (-)")
    print("3. คูณ (*)")
    print("4. หาร (/)")
    print("5. ออกจากโปรแกรม")


def get_menu_choice():
    """รับตัวเลือกเมนูจากผู้ใช้ และตรวจสอบว่าอยู่ในช่วง 1-5"""
    while True:
        choice = input("เลือกเมนู (1-5): ")
        if choice in ("1", "2", "3", "4", "5"):
            return choice
        print("กรุณาเลือกตัวเลข 1-5 เท่านั้น")


def calculate(choice, num1, num2):
    """
    เรียกฟังก์ชันคำนวณตามตัวเลือกที่ผู้ใช้เลือก
    คืนค่าผลลัพธ์ หรือ None ถ้ามีข้อผิดพลาด
    """
    try:
        if choice == "1":
            return add(num1, num2)
        elif choice == "2":
            return subtract(num1, num2)
        elif choice == "3":
            return multiply(num1, num2)
        elif choice == "4":
            return divide(num1, num2)
    except ZeroDivisionError as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None


def show_result(result):
    """แสดงผลลัพธ์การคำนวณ"""
    if result is not None:
        print(f"ผลลัพธ์ = {result}")


def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "5":
            print("ขอบคุณที่ใช้บริการครับ")
            break

        num1 = get_number("ป้อนตัวเลขที่ 1: ")
        num2 = get_number("ป้อนตัวเลขที่ 2: ")

        result = calculate(choice, num1, num2)
        show_result(result)


if __name__ == "__main__":
    main()