#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีการส่ง Argument เข้ามาเกินหรือไม่ (เช่น ./advanced_mult.py "yolo")
if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    # ลูปนอก: ควบคุมแม่สูตรคูณ (0 ถึง 10)
    while i <= 10:
        print(f"Table de {i}:", end="")
        
        j = 0
        # ลูปใน: ควบคุมตัวคูณในแต่ละแม่ (0 ถึง 10)
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
            
      
      
        # ขึ้นบรรทัดใหม่เมื่อพิมพ์ครบแต่ละแม่
        print()
        i += 1
