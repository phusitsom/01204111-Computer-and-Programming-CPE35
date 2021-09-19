import numpy as np
X = np.random.RandomState(1)

class Monster(object):

    def __init__(self, monster_ind: int, speed: int) -> None:
        self.name = f'Monster {monster_ind}'
        self.health = BLOOD_START//N
        self.speed = speed
        self.alive = True

    def __repr__(self):
        return repr(f"NAME: {self.name}, HP: {self.health}, SPEED: {self.speed}")
    
    def show_health(self):
        print(f'{self.name} HP left {self.health}')
        
    def show_turn(self):
        print(f'- {self.name} Turn -')

    def attack(self, player):
        player.__attacked__(X.randint(1, 40))
        player.show_health()

        return player

    def __attacked__(self, __damage: int):
        self.health = max(0, self.health-__damage)
        if self.health == 0:
            self.alive = False

class Player(object):

    def __init__(self) -> None:
        self.name = 'Your'
        self.health = BLOOD_START
        self.speed = SPEED
        self.damage = 10
        self.on_streak = False
        self.alive = True

    def __repr__(self):
        return repr(f"NAME: Player, HP: {self.health}, SPEED: {self.speed}")

    def show_health(self):
        print(f'Your HP left {self.health}')
        
    def show_turn(self):
        print('- Your Turn -')

    def attack(self, monster: Monster):

        if self.on_streak:
            self.damage += 2
        else:
            self.on_streak = True

        monster.__attacked__(self.damage)
        monster.show_health()
        
    def reset_streak(self):
        self.damage = 10
        self.on_streak = False

    def heal(self):
        self.health += 20*N
        self.reset_streak()
        self.show_health()

    def __attacked__(self, __damage: int):
        self.health = max(0, self.health-__damage)
        if self.health == 0:
            self.alive = False
            
BLOOD_START, SPEED, N = [int(input(_)) for _ in (
    'Blood Start: ', 'Your speed: ', 'Number of monsters: ')]

player = [Player()]
all_monsters = [Monster(i, int(input(f'Monster {i} speed: '))) for i in range(1, N+1)]

turn = 1
while True:
    remaining_monster = [m for m in all_monsters if m.alive]
    if remaining_monster == []: 
        print('You win.(^_^)')
        break
    queues = sorted(remaining_monster + player, key= lambda ins: ins.speed, reverse= True)
    monster = max(remaining_monster, key= lambda m: m.speed)
    
    print(f"=========================\nTurn {turn}\n-------------------------")
    
    queue_count, queue_end = 0, len(queues)
    while queue_count != queue_end:
        
        instance = queues[queue_count]
        instance.show_turn()
        
        if isinstance(instance, Player):
            if input('Attack(a) or Heal(h): ') == 'a':
                instance.attack(monster)
                
                if not monster.alive:
                    if queues.index(monster) < queues.index(player[0]):
                        queue_count-=1
                    del queues[queues.index(monster)]
                    queue_end = len(queues)
                    
            else:
                instance.heal()
                
        if isinstance(instance, Monster):
            instance.attack(player[0])
            if not player[0].alive:
                break
        queue_count+=1
        
    if not player[0].alive:
        print("You lose and die.(T_T)")
        break

    turn+=1