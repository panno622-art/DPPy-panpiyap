import random
 
# ข้อมูลหลัก
players = {}  # {"ชื่อ": {"balance": 1000, "wins": 0, "losses": 0}}
history = []  # [{"player": "ชื่อ", "game": "Dice", "bet": 100, "result": "win"}]
 
 
# --- ตรวจสอบผู้เล่นและเงินเดิมพัน (ใช้ร่วมกันทั้ง 2 เกม) ---
def check_bet(player_name, bet):
    if player_name not in players:
        print("❌ ไม่พบผู้เล่นนี้!")
        return False
    if bet <= 0:
        print("❌ เงินเดิมพันต้องมากกว่า 0!")
        return False
    if bet > players[player_name]["balance"]:
        print(f"❌ เงินไม่พอ! มีแค่ {players[player_name]['balance']} บาท")
        return False
    return True
 
 
# --- อัปเดตผลการเล่น ---
def update_result(player_name, game, bet, result):
    p = players[player_name]
    if result == "win":
        p["balance"] += bet
        p["wins"] += 1
        print(f"🎉 ชนะ! +{bet} บาท | คงเหลือ: {p['balance']} บาท")
    elif result == "loss":
        p["balance"] -= bet
        p["losses"] += 1
        print(f"😢 แพ้! -{bet} บาท | คงเหลือ: {p['balance']} บาท")
    else:
        print(f"🤝 เสมอ! คงเหลือ: {p['balance']} บาท")
    history.append({"player": player_name, "game": game, "bet": bet, "result": result})
 
 
# --- สร้างผู้เล่นใหม่ ---
def create_player(name, money):
    if name in players:
        print("❌ ชื่อนี้มีอยู่แล้ว!")
        return
    if money <= 0:
        print("❌ เงินเริ่มต้นต้องมากกว่า 0!")
        return
    players[name] = {"balance": money, "wins": 0, "losses": 0}
    print(f"✅ สร้างผู้เล่น '{name}' สำเร็จ! เงิน: {money} บาท")
 
 
# --- เกม Dice ---
def play_dice(player_name, bet):
    if not check_bet(player_name, bet):
        return
 
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    total = dice1 + dice2
    print(f"\n🎲 ลูกที่ 1: {dice1} | ลูกที่ 2: {dice2} | รวม: {total}")
 
    guess = input("ทาย HIGH (8-12) หรือ LOW (2-7): ").strip().upper()
    if guess not in ["HIGH", "LOW"]:
        print("❌ พิมพ์ผิด! ต้องพิมพ์ HIGH หรือ LOW")
        return
 
    actual = "HIGH" if total >= 8 else "LOW"
    print(f"ผลจริง: {actual}")
    update_result(player_name, "Dice", bet, "win" if guess == actual else "loss")
 
 
# --- เกม Blackjack ---
def play_blackjack(player_name, bet):
    if not check_bet(player_name, bet):
        return
 
    my_cards = [random.randint(1, 11), random.randint(1, 11)]
    dealer_cards = [random.randint(1, 11), random.randint(1, 11)]
    print(f"\n🃏 ไพ่ของคุณ: {my_cards} รวม = {sum(my_cards)}")
    print(f"🃏 Dealer: [{dealer_cards[0]}, ?]")
 
    # ผู้เล่นจั่วไพ่
    while sum(my_cards) < 21:
        choice = input("HIT (จั่ว) หรือ STAND (หยุด): ").strip().upper()
        if choice == "HIT":
            my_cards.append(random.randint(1, 11))
            print(f"🃏 ไพ่คุณ: {my_cards} รวม = {sum(my_cards)}")
            if sum(my_cards) > 21:
                print("💥 BUST! แต้มเกิน 21!")
                update_result(player_name, "Blackjack", bet, "loss")
                return
        elif choice == "STAND":
            break
        else:
            print("❌ พิมพ์ HIT หรือ STAND เท่านั้น!")
 
    # Dealer จั่วไพ่ (กฎ: ต้องจั่วถ้าน้อยกว่า 17)
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.randint(1, 11))
    print(f"🃏 ไพ่ Dealer: {dealer_cards} รวม = {sum(dealer_cards)}")
 
    # ตัดสินผล
    p, d = sum(my_cards), sum(dealer_cards)
    if d > 21 or p > d:
        result = "win"
    elif p == d:
        result = "draw"
    else:
        result = "loss"
    update_result(player_name, "Blackjack", bet, result)
 
 
# --- ดูประวัติ ---
def show_history(player_name):
    if player_name not in players:
        print("❌ ไม่พบผู้เล่นนี้!")
        return
    records = [r for r in history if r["player"] == player_name]
    if not records:
        print("ยังไม่มีประวัติการเล่น")
        return
    print(f"\n📜 ประวัติของ '{player_name}':")
    for i, r in enumerate(records, 1):
        print(f"  {i}. {r['game']} | เดิมพัน: {r['bet']} | ผล: {r['result']}")
 
 
# --- ดู Leaderboard ---
def show_leaderboard():
    if not players:
        print("❌ ยังไม่มีผู้เล่น!")
        return
    print("\n🏆 LEADERBOARD:")
    sorted_p = sorted(players.items(), key=lambda x: x[1]["balance"], reverse=True)
    for i, (name, d) in enumerate(sorted_p, 1):
        total = d["wins"] + d["losses"]
        rate = round(d["wins"] / total * 100) if total > 0 else 0
        print(f"  {i}. {name} | เงิน: {d['balance']} บาท | W:{d['wins']} L:{d['losses']} | Win Rate: {rate}%")
 
 
# --- เมนูหลัก ---
def main():
    print("=" * 40)
    print("🎰   ยินดีต้อนรับสู่ BANGKOK CASINO   🎰")
    print("=" * 40)
 
    while True:
        print("\n1. สร้างผู้เล่นใหม่")
        print("2. เล่น Dice")
        print("3. เล่น Blackjack")
        print("4. ดูประวัติ")
        print("5. ดู Leaderboard")
        print("6. ออก")
        choice = input("\nเลือก (1-6): ").strip()
 
        if choice == "1":
            name = input("ชื่อผู้เล่น: ").strip()
            if not name:
                print("❌ ชื่อห้ามว่าง!")
                continue
            try:
                money = int(input("เงินเริ่มต้น (บาท): "))
            except ValueError:
                print("❌ ใส่เป็นตัวเลขเท่านั้น!")
                continue
            create_player(name, money)
 
        elif choice in ["2", "3"]:
            # แสดงรายชื่อผู้เล่นก่อน
            if not players:
                print("❌ ยังไม่มีผู้เล่น! สร้างผู้เล่นก่อน")
                continue
            print("\n👥 ผู้เล่น:", ", ".join(players.keys()))
            name = input("ชื่อผู้เล่น: ").strip()
            try:
                bet = int(input("เงินเดิมพัน: "))
            except ValueError:
                print("❌ ใส่เป็นตัวเลขเท่านั้น!")
                continue
            if choice == "2":
                play_dice(name, bet)
            else:
                play_blackjack(name, bet)
 
        elif choice == "4":
            name = input("ชื่อผู้เล่น: ").strip()
            show_history(name)
 
        elif choice == "5":
            show_leaderboard()
 
        elif choice == "6":
            print("\n👋 ขอบคุณที่มาเล่น! แล้วพบกันใหม่ 🎰")
            break
 
        else:
            print("❌ ไม่มีเมนูนี้! เลือก 1-6")
 
 
if __name__ == "__main__":
    main()
 