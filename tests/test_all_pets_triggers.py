import unittest
import numpy as np
from torch import seed

from sapai import *
from sapai.compress import compress, decompress

class TestPetTriggers(unittest.TestCase):
    @staticmethod
    def print_pet_list(pet_list):
        n = []
        trigger_list = []
        triggerby_list = []
        effect_kind_list = []
        effect_target_kind_list = []
        for iter_idx, pet in enumerate(pet_list):
            n.append(iter_idx)
            trigger_list.append(pet.ability["trigger"])
            triggerby_list.append(pet.ability["triggeredBy"]["kind"])
            effect_kind_list.append(pet.ability["effect"]["kind"])
            if "target" in pet.ability["effect"]:
                effect_target_kind_list.append(pet.ability["effect"]["target"]["kind"])
            elif "to" in pet.ability["effect"]:
                effect_target_kind_list.append(pet.ability["effect"]["to"]["kind"])
            else:
                effect_target_kind_list.append("NONE")

        str_fmt = "{:3s}{:20s}{:15s}{:15s}{:20s}{:20s}\n"
        print_str = str_fmt.format(
            "N", "Pet", "Trigger", "TriggerBy", "EffectKind", "EffectTarget"
        )
        print_str += "-------------------------------------------------------------------------------\n"
        for iter_idx in range(len(pet_list)):
            print_str += str_fmt.format(
                str(n[iter_idx]),
                pet_list[iter_idx].name,
                trigger_list[iter_idx],
                triggerby_list[iter_idx],
                effect_kind_list[iter_idx],
                effect_target_kind_list[iter_idx],
            )

        print(print_str)

    def test_peacock(self):
        t = Team(["peacock"])
        enemy = Team(["fish"])
        t[0].obj.level = 1
        t[0].obj.hurt(1)
        t[0].obj.hurt_trigger(enemy)
        self.assertEqual(t[0].attack, 5)

        t = Team(["peacock"])
        enemy = Team(["fish"])
        t[0].obj.level = 2
        t[0].obj.hurt(1)
        t[0].obj.hurt_trigger(enemy)
        self.assertEqual(t[0].attack, 8)

        t = Team(["peacock"])
        enemy = Team(["fish"])
        t[0].obj.level = 3
        t[0].obj.hurt(1)
        t[0].obj.hurt_trigger(enemy)
        self.assertEqual(t[0].attack, 11)
    
    def test_turtle(self):
        # Test level 1 turtle
        t = Team(["turtle", "fish", "otter"])
        t[0].obj.level = 1
        t[0].obj.faint_trigger(t[0].obj, [0, 0])
        self.assertEqual(t[1].obj.status, "status-melon-armor")
        self.assertEqual(t[2].obj.status, "none")

        # Test level 1 turtle with melon already on first pet behind
        t = Team(["turtle", "fish", "fish"])
        t[0].obj.level = 1
        t[1].obj.status = "status-melon-armor"
        t[0].obj._health = 0  # Simulate fainting
        t[0].obj.faint_trigger(t[0].obj, [0, 0])
        self.assertEqual(t[1].obj.status, "status-melon-armor")
        self.assertEqual(t[2].obj.status, "status-melon-armor")

        # Test level 2 turtle
        t = Team(["turtle", "fish", "otter", "duck"])
        t[0].obj.level = 2
        t[0].obj.faint_trigger(t[0].obj, [0, 0])
        self.assertEqual(t[1].obj.status, "status-melon-armor")
        self.assertEqual(t[2].obj.status, "status-melon-armor")
        self.assertEqual(t[3].obj.status, "none")

        # Test level 2 turtle with melon already on first pet behind
        t = Team(["turtle", "fish", "otter", "duck", "beaver"])
        t[0].obj.level = 2
        t[1].obj.status = "status-melon-armor"
        t[2].obj.status = "status-melon-armor"
        t[0].obj.faint_trigger(t[0].obj, [0, 0])
        self.assertEqual(t[3].obj.status, "status-melon-armor")
        self.assertEqual(t[4].obj.status, "status-melon-armor")

        # Test level 3 turtle
        t = Team(["turtle", "fish", "otter", "duck", "beaver"])
        t[0].obj.level = 3
        t[0].obj.faint_trigger(t[0].obj, [0, 0])
        self.assertEqual(t[1].obj.status, "status-melon-armor")
        self.assertEqual(t[2].obj.status, "status-melon-armor")
        self.assertEqual(t[3].obj.status, "status-melon-armor")
        self.assertEqual(t[4].obj.status, "none")
    
    def test_flamingo(self):
        t = Team(["flamingo", "dragon", "dragon", "dragon"])
        t[0].obj.level = 1
        pet = t[0].obj
        te_idx = [0, 0]
        t[0].obj.faint_trigger(pet, te_idx)
        self.assertEqual(t[1].attack, 6 + 1)
        self.assertEqual(t[1].health, 8 + 1)
        self.assertEqual(t[2].attack, 6 + 1)
        self.assertEqual(t[2].health, 8 + 1)
        self.assertEqual(t[3].attack, 6)
        self.assertEqual(t[3].health, 8)

        t = Team(["flamingo", "dragon", "dragon", "dragon"])
        t[0].obj.level = 2
        pet = t[0].obj
        te_idx = [0, 0]
        t[0].obj.faint_trigger(pet, te_idx)
        self.assertEqual(t[1].attack, 6 + 2)
        self.assertEqual(t[1].health, 8 + 2)
        self.assertEqual(t[2].attack, 6 + 2)
        self.assertEqual(t[2].health, 8 + 2)
        self.assertEqual(t[3].attack, 6)
        self.assertEqual(t[3].health, 8)

        t = Team(["flamingo", "dragon", "dragon", "dragon"])
        t[0].obj.level = 3
        pet = t[0].obj
        te_idx = [0, 0]
        t[0].obj.faint_trigger(pet, te_idx)
        self.assertEqual(t[1].attack, 6 + 3)
        self.assertEqual(t[1].health, 8 + 3)
        self.assertEqual(t[2].attack, 6 + 3)
        self.assertEqual(t[2].health, 8 + 3)
        self.assertEqual(t[3].attack, 6)
        self.assertEqual(t[3].health, 8)

    def test_end_of_turn_triggers(self):
        test_team = Team([Pet("fish"), Pet("dragon"), Pet("cat")])
        test_team[0].pet.level = 3
        test_player = Player()

        test_pet_names = [
            "bluebird",
            "hatching-chick",
            "puppy",
            "tropical-fish",
            "bison",
            "llama",
            "penguin",
            "parrot",
            "monkey",
            "poodle",
            "tyrannosaurus",
        ]

        test_pet_list = [
            Pet(x, shop=Shop(), team=test_team.copy(), player=test_player)
            for x in test_pet_names
        ]
        self.print_pet_list(test_pet_list)

        for pet in test_pet_list:
            activated_bool, targets, possible = pet.eot_trigger(pet.team[0].pet)
            print("Name:", pet.name)
            print("activated: ", activated_bool)
            self.assertTrue(activated_bool)


if __name__ == '__main__':
    unittest.main()