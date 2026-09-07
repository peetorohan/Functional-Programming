"""
Calculator (v2)
โปรแกรมเครื่องคิดเลข แบ่งการทำงานเป็นฟังก์ชันย่อย
และเพิ่มการจัดการข้อผิดพลาด (Exception Handling)
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
    """หาร (จะยิง ZeroDivisionError ถ้า b เป็น 0)"""
    if b == 0:
        raise ZeroDivisionError("ไม่สามารถหารด้วยศูนย์ได้")
    return a / b


def get_number(prompt):
    """
    รับค่าตัวเลข (float) จากผู้ใช้
    ใช้ try-except จัดการกรณีป้อนข้อมูลที่ไม่ใช่ตัวเลข
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ข้อผิดพลาด: กรุณาป้อนตัวเลขเท่านั้น (เช่น 3 หรือ 3.5)")
        except KeyboardInterrupt:
            print("\nยกเลิกการป้อนข้อมูล")
            raise


def show_menu():
    """แสดงเมนูตัวเลือกการคำนวณ"""
    print("\n=== เครื่องคิดเลข ===")
    print("1. บวก (+)")
    print("2. ลบ (-)")
    print("3. คูณ (*)")
    print("4. หาร (/)")
    print("5. ออกจากโปรแกรม")


def get_menu_choice():
    """รับตัวเลือกเมนูจากผู้ใช้ พร้อมตรวจสอบความถูกต้อง"""
    while True:
        try:
            choice = input("เลือกเมนู (1-5): ").strip()
            if choice not in ("1", "2", "3", "4", "5"):
                raise ValueError("ตัวเลือกต้องอยู่ระหว่าง 1-5 เท่านั้น")
            return choice
        except ValueError as e:
            print(f"ข้อผิดพลาด: {e}")


def calculate(choice, num1, num2):
    """
    เรียกฟังก์ชันคำนวณตามตัวเลือกที่ผู้ใช้เลือก
    ดักจับข้อผิดพลาดที่อาจเกิดขึ้น (เช่น หารด้วยศูนย์)
    คืนค่า (result, error_message)
    """
    try:
        if choice == "1":
            return add(num1, num2), None
        elif choice == "2":
            return subtract(num1, num2), None
        elif choice == "3":
            return multiply(num1, num2), None
        elif choice == "4":
            return divide(num1, num2), None
    except ZeroDivisionError as e:
        return None, str(e)
    except OverflowError:
        return None, "ตัวเลขมีค่ามากเกินไปที่จะคำนวณได้"
    except Exception as e:
        # ดักจับข้อผิดพลาดอื่น ๆ ที่ไม่คาดคิด เพื่อไม่ให้โปรแกรมหยุดทำงาน
        return None, f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}"


def show_result(result, error_message):
    """แสดงผลลัพธ์ หรือข้อความข้อผิดพลาดถ้ามี"""
    if error_message:
        print(f"ข้อผิดพลาด: {error_message}")
    else:
        print(f"ผลลัพธ์ = {result}")


def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == "5":
                print("ขอบคุณที่ใช้บริการครับ")
                break

            num1 = get_number("ป้อนตัวเลขที่ 1: ")
            num2 = get_number("ป้อนตัวเลขที่ 2: ")

            result, error_message = calculate(choice, num1, num2)
            show_result(result, error_message)

    except KeyboardInterrupt:
        print("\nออกจากโปรแกรมเรียบร้อยแล้ว")
    finally:
        print("จบการทำงานของโปรแกรม")


if __name__ == "__main__":
    main()
