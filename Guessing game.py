"""
Guessing Game (v2)
โปรแกรมทายตัวเลข แบ่งการทำงานเป็นฟังก์ชันย่อย
และเพิ่มการจัดการข้อผิดพลาด (Exception Handling)
"""

import random


def generate_secret_number(low=1, high=100):
    """สุ่มตัวเลขลับที่ผู้เล่นต้องทาย"""
    try:
        return random.randint(low, high)
    except ValueError:
        # กรณีค่า low, high ผิดช่วง (low > high)
        print("ช่วงตัวเลขไม่ถูกต้อง จะใช้ค่าเริ่มต้น 1-100 แทน")
        return random.randint(1, 100)


def get_user_guess():
    """
    รับค่าตัวเลขที่ผู้เล่นทายจากคีย์บอร์ด
    ใช้ try-except จัดการกรณีป้อนข้อมูลที่ไม่ใช่ตัวเลข
    """
    while True:
        try:
            guess = int(input("ทายตัวเลข (1-100): "))
            return guess
        except ValueError:
            print("ข้อผิดพลาด: กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
        except KeyboardInterrupt:
            # ผู้ใช้กด Ctrl+C ระหว่างป้อนข้อมูล
            print("\nยกเลิกการป้อนข้อมูล")
            raise


def check_guess(guess, secret_number):
    """
    เปรียบเทียบค่าที่ทายกับเลขลับ
    คืนค่า: 'correct', 'too_high', 'too_low'
    """
    if guess == secret_number:
        return "correct"
    elif guess > secret_number:
        return "too_high"
    else:
        return "too_low"


def show_hint(result):
    """แสดงคำใบ้ตามผลการเปรียบเทียบ"""
    if result == "too_high":
        print("ทายสูงไปครับ ลองใหม่อีกครั้ง")
    elif result == "too_low":
        print("ทายต่ำไปครับ ลองใหม่อีกครั้ง")


def play_game(low=1, high=100):
    """ควบคุมการเล่นเกมทั้งหมด 1 รอบ คืนค่าจำนวนครั้งที่ทาย"""
    secret_number = generate_secret_number(low, high)
    attempts = 0

    print(f"ผมกำลังคิดตัวเลขระหว่าง {low}-{high} อยู่ในใจ ลองทายดูสิ!")

    while True:
        try:
            guess = get_user_guess()
            attempts += 1
            result = check_guess(guess, secret_number)

            if result == "correct":
                print(f"ถูกต้อง! คุณทายถูกภายใน {attempts} ครั้ง 🎉")
                return attempts
            else:
                show_hint(result)

        except KeyboardInterrupt:
            print("\nยกเลิกเกมรอบนี้")
            return attempts
        except Exception as e:
            # ดักจับข้อผิดพลาดที่ไม่คาดคิดอื่น ๆ เพื่อไม่ให้โปรแกรมพัง
            print(f"เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")


def ask_play_again():
    """ถามผู้เล่นว่าต้องการเล่นอีกครั้งหรือไม่ พร้อมตรวจสอบค่าที่ป้อน"""
    while True:
        try:
            answer = input("ต้องการเล่นอีกครั้งหรือไม่ (y/n): ").strip().lower()
            if answer in ("y", "n"):
                return answer == "y"
            raise ValueError("ต้องป้อน y หรือ n เท่านั้น")
        except ValueError as e:
            print(f"ข้อผิดพลาด: {e}")


def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    print("=== เกมทายตัวเลข ===")
    try:
        while True:
            play_game()
            if not ask_play_again():
                print("ขอบคุณที่เล่นเกมนี้ครับ")
                break
    except KeyboardInterrupt:
        print("\nออกจากโปรแกรมเรียบร้อยแล้ว")
    finally:
        print("จบการทำงานของโปรแกรม")


if __name__ == "__main__":
    main()
