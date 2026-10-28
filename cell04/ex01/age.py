#!/usr/bin/env python3

# รับค่าอายุเริ่มต้นจากผู้ใช้
current_age = int(input(""))

# วนลูป 3 รอบ โดยให้จำนวนปีเพิ่มขึ้นทีละ 10 (คือ 10, 20, 30)
for i in range(10, 31, 10):
    future_age = current_age + i
    print(f"In {i} years, you'll be {future_age} years old.")
