import unittest

import numpy as np

from sapai import *
from sapai.battle import Battle
from sapai.graph import graph_battle
from sapai.compress import *


class TestBattles(unittest.TestCase):
    # def test_whale_summon_stats(self):
    #     fish = Pet("fish")
    #     fish._attack = 10
    #     fish._health = 31
    #     team1 = Team([fish])
    #     whale = Pet("whale")
    #     whale.level = 2
    #     badger = Pet("badger")
    #     badger._attack = 7
    #     badger._health = 4
    #     team2 = Team([Pet("badger"), whale])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()

    #     self.assertEqual(result, 2)
    # def test_dolphin_snipes(self):
    #     dolphin = Pet("dolphin")
    #     dolphin.level = 2
    #     team1 = Team([dolphin])
    #     duck = Pet("duck")
    #     duck._attack = 3
    #     duck._health = 5
    #     duck.status = "status-garlic-armor"
    #     team2 = Team([duck])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()

    #     self.assertEqual(result, 2)
    
    # def test_shark(self):
    #     shark = Pet("shark")
    #     team1 = Team([shark])
    #     duck = Pet("duck")
    #     duck._attack = 3
    #     duck._health = 2
    #     team2 = Team([duck])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()

    #     self.assertEqual(result, 2)
    
    # def test_fly(self):
    #     mammoth = Pet("mammoth")
    #     mammoth.status = "status-splash-attack"
    #     bison = Pet("bison")
    #     bison._attack = 7
    #     bison._health = 7
    #     leopard = Pet("leopard")
    #     hedgehog = Pet("hedgehog")
    #     team1 = Team([mammoth, bison, leopard, hedgehog])

    #     fly = Pet("fly")
    #     fly._attack = 50
    #     fly._health = 50
    #     snake = Pet("snake")
    #     m = Pet("mammoth")
    #     mosquito = Pet("mosquito")
    #     team2 = Team([fly, snake, m, mosquito])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()

    #     self.assertEqual(result, 1)

    # def test_chilli(self):
    #     # this causes an error because chilli makes ant faint, but then dirty rat changes index of ant
    #     # sheep and mushroom also may cause similar erros ex. 4th position pet faints but then sheep faints too which makes 5th position pet treated as fainted
    #     ant = Pet("ant")
    #     ant.status = "status-garlic-armor"
    #     worm = Pet("worm")
    #     worm._attack = 6
    #     worm._health = 8
    #     beaver = Pet("beaver")
    #     horse = Pet("horse")
    #     team1 = Team([worm, ant, horse])

    #     b = Pet("beaver")
    #     b._attack = 3
    #     b._health = 4
    #     rat = Pet("rat")
    #     rat.status = "status-splash-attack"
    #     rat._attack = 3
    #     rat._health = 6
    #     spider = Pet("spider")
    #     shrimp = Pet("shrimp") 
    #     cricket = Pet("cricket")
    #     team2 = Team([rat, spider, shrimp, cricket])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()
    
    # def test_tiger(self):
    #     mammoth = Pet("mammoth")
    #     mammoth.status = "status-splash-attack"
    #     bison = Pet("bison")
    #     bison._attack = 7
    #     bison._health = 7
    #     tiger = Pet("tiger")
    #     spider = Pet("spider")
    #     hedgehog = Pet("hedgehog")
    #     team1 = Team([spider, tiger, mammoth, bison, hedgehog])

    #     fly = Pet("fly")
    #     fly._attack = 50
    #     fly._health = 50
    #     snake = Pet("snake")
    #     m = Pet("mammoth")
    #     mosquito = Pet("mosquito")
    #     team2 = Team([fly, m, m, mosquito])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()

    # def test_sheep_and_fly(self):
    #     dolphin = Pet("dolphin")
    #     # deer.status = "status-extra-life"
    #     team1 = Team([dolphin])


    #     sheep = Pet("sheep")
    #     sheep._attack = 6
    #     # sheep.status = "status-extra-life"
    #     fly = Pet("fly")
    #     team2 = Team([sheep, fly])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()
    
    # def test_sheep_and_fly(self):
    #     dolphin = Pet("dolphin")
    #     rooster = Pet("rooster")
    #     rooster.level = 2
    #     # deer.status = "status-extra-life"
    #     team1 = Team([dolphin, Pet("peacock"), Pet("peacock"), Pet("peacock"), Pet("peacock")])


    #     sheep = Pet("sheep")
    #     sheep._attack = 6
    #     sheep._health = 1
    #     # sheep.status = "status-extra-life"
    #     fly = Pet("fly")
    #     team2 = Team([sheep, Pet("peacock"), Pet("peacock"), Pet("beaver"), fly])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()
    # def test_honey_status(self):
    #     fish = Pet("fish")
    #     fish.status = "status-bone-attack"
    #     fish._attack = 5
    #     pig = Pet("pig")
    #     pig.status = "status-honey-bee"
    #     ant = Pet("ant")
    #     duck = Pet("duck")
    #     duck._attack = 3
    #     duck._health = 4
    #     # deer.status = "status-extra-life"
    #     team1 = Team([pig, ant, duck])


    #     otter = Pet("otter")
    #     otter._attack = 3
    #     otter._health = 4
    #     # sheep.status = "status-extra-life"
    #     mosquito = Pet("mosquito")
    #     team2 = Team([otter])

    #     test_battle = Battle(team1, team2)
    #     result = test_battle.battle()
    #     self.assertEqual(result, 0)
    # def test_rhino(self):
    #    # Create Team 0
    #     badger1 = Pet("badger")
    #     badger1._attack = 7
    #     badger1._health = 4

    #     rhino = Pet("rhino")
    #     rhino._attack = 7
    #     rhino._health = 8

    #     cow = Pet("cow")
    #     cow._attack = 4
    #     cow._health = 6

    #     skunk = Pet("skunk")
    #     skunk._attack = 3
    #     skunk._health = 5

    #     team0 = Team([badger1, rhino, cow, skunk])

    #     # Create Team 1
    #     badger2 = Pet("badger")
    #     badger2._attack = 9
    #     badger2._health = 4
    #     badger2.status = "status-bone-attack"

    #     whale = Pet("whale")
    #     whale._attack = 4
    #     whale._health = 10

    #     dolphin = Pet("dolphin")
    #     dolphin._attack = 4
    #     dolphin._health = 3

    #     badger3 = Pet("badger")
    #     badger3._attack = 6
    #     badger3._health = 3

    #     team1 = Team([badger2, whale, dolphin, badger3])

    #     # Create the battle
    #     from sapai import Battle

    #     battle = Battle(team0, team1)

    #     # Run the battle
    #     result = battle.battle()
    # def test_rhino_turtle(self):
    #     turtle = Pet("turtle")
    #     cow = Pet("cow")
    #     team0 = Team([turtle, cow])
    #     rhino = Pet("rhino")
    #     team1 = Team([rhino])
    #     battle = Battle(team0, team1)

    #     result = battle.battle()
    #     self.assertEqual(result, 1)
    # def test_camel_faint(self):
    #     camel = Pet("camel")
    #     camel._health = 5
    #     snail = Pet("snail")
    #     snail._attack = 4
    #     snail._health = 4
    #     team1 = Team([camel, snail])
    #     hippo = Pet("hippo")
    #     hippo._health = 7
    #     team2 = Team([hippo])

    #     battle = Battle(team1, team2)

    #     result = battle.battle()
    #     self.assertEqual(result, 0)
    def test_blowfish_hurt(self):
        # Create Team 0
        hedgehog = Pet("hedgehog")
        hedgehog._attack = 3
        hedgehog._health = 6

        horse = Pet("horse")
        horse._attack = 3
        horse._health = 3
        horse.status = "status-honey-bee"

        rooster = Pet("rooster")
        rooster._attack = 6
        rooster._health = 4

        parrot = Pet("parrot")
        parrot._attack = 5
        parrot._health = 2

        team0 = Team([hedgehog])

        # Create Team 1
        beaver = Pet("beaver")
        beaver._attack = 4
        beaver._health = 3
        beaver.status = "status-splash-attack"

        swan = Pet("swan")
        swan._attack = 2
        swan._health = 4
        swan.status = "status-splash-attack"

        peacock = Pet("peacock")
        peacock._attack = 2
        peacock._health = 5

        duck = Pet("duck")
        duck._attack = 5
        duck._health = 4
        duck.status = "status-bone-attack"

        blowfish = Pet("blowfish")
        blowfish._attack = 3
        blowfish._health = 6

        team1 = Team([blowfish])

        battle = Battle(team0, team1)
        result = battle.battle()
        self.assertEqual(result, 1)

    def test_extra_life_status(self):
        pass


if __name__ == '__main__':
    unittest.main()