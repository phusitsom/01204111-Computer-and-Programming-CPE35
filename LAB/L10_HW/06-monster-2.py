from typing import List

import numpy as np
X = np.random.RandomState(1)

BLOOD_START, SPEED, N = [int(input(_)) for _ in (
    'Blood Start: ', 'Your speed: ', 'Number of monsters: ')]


class Monster(object):

    def __init__(self, monster_ind: int, speed: int) -> None:
        self.health = BLOOD_START//N
        self.speed = speed
        self.name = f'Monster {monster_ind}'
        self.alive = True

    def show_health(self):
        print(f'{self.name} HP left {self.health}')

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

    def show_health(self):
        print(f'Your HP left {self.health}')

    def attack(self, monster: Monster):

        if self.on_streak:
            self.damage += 2
        else:
            self.on_streak = True

        monster.__attacked__(self.damage)
        monster.show_health()

    def heal(self):
        self.health += 20*N
        self.damage = 10
        self.show_health()

    def __attacked__(self, __damage: int):
        self.health = max(0, self.health-__damage)
        self.alive = False


def sort_by_speed(lst: List[Monster or Player]):
    return sorted(lst, key=lambda _m: _m.speed, reverse=True)


player = [Player()]
monsters = [Monster(i, int(input(f'Monster {i} speed: '))) for i in range(1, N+1)]

turns = sort_by_speed(player + monsters)

turn_count = 1
while True:
    print(f'=========================\nTurn {turn_count}\n-------------------------')

    for instance in turns:
        print(f"- {instance.name} Turn -") if instance.alive else None

        if isinstance(instance, Player):

            move = input('Attack(a) or Heal(h): ')

            if move == 'a':
                instance.attack(
                    sort_by_speed([monster for monster in monsters if monster.alive])[0])

            elif move == 'h':
                instance.heal()

        elif isinstance(instance, Monster):
            if instance.health == 0:
                continue
            else:
                instance.attack(player[0])

        if not player.alive:
            break

    if not player.alive:
        print('You lose and die.(T_T)')
        break

    if all(map(lambda _m: not _m.alive, monsters)):
        print('You win.(^_^)')
        break
    turn_count += 1
