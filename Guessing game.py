"""
Guessing Game
โปรแกรมทายตัวเลข แบ่งการทำงานออกเป็นฟังก์ชันย่อย
"""

import random


def generate_secret_number(low=1, high=100):
    """สุ่มตัวเลขลับที่ผู้เล่นต้องทาย"""
    return random.randint(low, high)


def get_user_guess():
    """รับค่าตัวเลขที่ผู้เล่นทายจากคีย์บอร์ด พร้อมตรวจสอบว่าเป็นตัวเลข"""
    while True:
        guess_input = input("ทายตัวเลข (1-100): ")
        if guess_input.isdigit():
            return int(guess_input)
        print("กรุณาป้อนตัวเลขเท่านั้น")


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
        guess = get_user_guess()
        attempts += 1
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"ถูกต้อง! คุณทายถูกภายใน {attempts} ครั้ง 🎉")
            return attempts
        else:
            show_hint(result)


def ask_play_again():
    """ถามผู้เล่นว่าต้องการเล่นอีกครั้งหรือไม่"""
    answer = input("ต้องการเล่นอีกครั้งหรือไม่ (y/n): ")
    return answer.strip().lower() == "y"


def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    print("=== เกมทายตัวเลข ===")
    while True:
        play_game()
        if not ask_play_again():
            print("ขอบคุณที่เล่นเกมนี้ครับ")
            break


if __name__ == "__main__":
    main()