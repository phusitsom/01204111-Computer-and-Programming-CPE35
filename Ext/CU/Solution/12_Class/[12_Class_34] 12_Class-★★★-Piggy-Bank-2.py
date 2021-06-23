class piggybank:
    def __init__(self):
        # มีตัวแปร self.coins เก็บ dict เริ่มต้นให้ว่าง ๆ
        # มี key เป็นมูลค่าเหรียญ และ value เป็นจ านวนเหรียญ
        self.coins = {}
        self.number = 0

    def add(self, v, n):
        # ถ้าเพิ่มจ านวนเหรียญในกระปุกอีก n เหรียญแล้วเกิน 100
        # จะไม่ให้เพิ่ม ให้คืน False แทนว่า เพิ่มไม่ส าเร็จ
        # แปลง v เป็น float ก่อน (เพิ่ม 5 กับ 5.0 จะได้เหมือนกัน)
        # ถ้ากระปุกไม่เคยมีเหรียญ v ท า self.coins[v]= 0
        # ท าค าสั่ง self.coins[v] += n
        # คืน True แทนว่าเพิ่มส าเร็จ
        v = float(v)
        if self.number + n <= 100:
            if v in self.coins:
                self.coins[v] += n
            else:
                self.coins[v] = n
            self.number += n
        else:
            return False
        return True

    def __float__(self):
        # น าค่าของเหรียญคูณกับจ านวนเหรียญ ของเหรียญทุกแบบ
        # ต้องคืนจ านวนแบบ float เท่านั้น อยากคืนศูนย์ ก็ต้อง 0.0
        sum_all = 0.0
        for i in self.coins:
            sum_all += self.coins[i] * i
        return sum_all

    def __str__(self):
        # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
        # โดยให้เรียงเหรียญตามมูลค่าจากน้อยไปมาก
        s = ', '.join([str(i) + ':' + str(self.coins[i]) for i in sorted(self.coins)])
        return '{' + s + '}'


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank();
p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)