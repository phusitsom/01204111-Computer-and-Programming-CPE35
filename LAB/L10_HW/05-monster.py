import numpy as np
X = np.random.RandomState(1)

hp_monster = hp_hero = int(input('Blood Start: '))
damage = 10
streak = False

while True:
    move = input('Attack(a) or Heal(h): ')
    
    if move == 'a':
        if streak: damage += 2
        else: streak = True
        
        hp_monster = max(0, hp_monster-damage)
        print(f"Monster's HP left {hp_monster}")
        if not hp_monster: 
            print('You win.(^_^)')
            break
        
    elif move == 'h':
        hp_hero += 20
        damage, streak = 10, False
        print(f"Your HP left {hp_hero}")
            
    hp_hero = max(0, hp_hero-X.randint(1, 40)) 
    
    print(f"Monster's turn : Your HP left {hp_hero}")
    if not hp_hero:
        print('You lose and die.(T_T)')
        break