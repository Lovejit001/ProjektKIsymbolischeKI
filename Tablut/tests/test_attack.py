import unittest

import src.gamelogic.config
from src.gamelogic.attack import *
from tests.definitions import attackBoard1,attackBoard2,attackBoard3,attackBoard4,attackBoard5,attackBoard6,attackBoard7,attackBoard8,attackBoard9,attackBoard10,attackBoard11,attackBoard12,attackBoard13,attackBoard14,attackBoard15,attackBoard16,attackBoard17,attackBoard18,attackBoard19,attackBoard20,attackBoard21,attackBoard22,attackBoard23,attackBoard24,K,B,W,attackBoard202,attackBoard203,attackBoard204,attackBoard205,attackBoard206,attackBoard207,attackBoard208,attackBoard25,attackBoard26,attackBoard27,attackBoard28


class TestAttack(unittest.TestCase):

    def test_blackAttackWhite(self):
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, B, 0, B, 0, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        attack(attackBoard1,(1,3))
               
        self.assertEqual(attackBoard1, expected)
        print(f"✓ blackAttackWhite left and right: test passed")

        attack(attackBoard1,(4,4))
        self.assertEqual(attackBoard1, expected)
        print(f"✓ black attacks White King: test passed")

    def test_blackAttacks(self):

        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, W, B, 0, 0, 0],
            [0, 0, B, W, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, B, W, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected5 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, 0, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, W, B, 0, 0, 0],
            [0, 0, B, W, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected6 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, W, B, 0, 0, 0],
            [0, 0, B, 0, B, 0, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        attack(attackBoard2,(2,1))
        self.assertEqual(attackBoard2, expected)
        print(f"✓ blackAttackWhite vertical attack down: test passed")
        
        attack(attackBoard2,(4,1))
        self.assertEqual(attackBoard2, expected)
        print(f"✓ blackAttackWhite vertical attack up: test passed")

        attack(attackBoard3,(6,3))
        self.assertEqual(attackBoard3, expected2)
        print(f"✓ blackAttackWhite horizontal attack right: test passed")

        attack(attackBoard4,(6,5))
        self.assertEqual(attackBoard4, expected2)
        print(f"✓ blackAttackWhite horizontal attack left: test passed")
        
        attack(attackBoard5,(3,7))
        self.assertEqual(attackBoard5, expected5)
        print(f"✓ blackAttackWhite vertical double attack: test passed")

        attack(attackBoard6,(7,4))
        self.assertEqual(attackBoard6, expected6)
        print(f"✓ blackAttackWhite horizontal double attack: test passed")

    def test_King_Attack_NextToThron(self):
        expected1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, 0, 0, 0, 0, 0],
            [0, 0, B, K, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]   

        expected2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, 0, 0, 0, 0, 0],
            [0, 0, B, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]   

        expected3 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]   

        expected4 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ] 

        expected5 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, B, 0, 0, 0],
            [0, 0, 0, 0, 0, K, 0, 0, 0],
            [0, 0, 0, 0, 0, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ] 

        expected6 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, B, 0, 0],
            [0, 0, 0, 0, 0, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected7 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, K, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        expected8 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        attack(attackBoard7,(4,2))
        self.assertEqual(attackBoard7, expected1)
        print(f"✓ black dont kill King: test passed")

        attack(attackBoard8,(4,2))
        self.assertEqual(attackBoard8, expected2)
        print(f"✓ black kill King: test passed")

        attack(attackBoard8,(3,3))
        self.assertEqual(attackBoard8, expected2)
        print(f"✓ black kill King: test passed")
        
        attack(attackBoard8,(5,3))
        self.assertEqual(attackBoard8, expected2)
        print(f"✓ black kill King: test passed")
        
        attack(attackBoard9,(5,3))
        self.assertEqual(attackBoard9, expected3)
        print(f"✓ black dont kill King: test passed")

        attack(attackBoard9,(5,5))
        self.assertEqual(attackBoard9, expected3)
        print(f"✓ black dont kill King: test passed")

        attack(attackBoard10,(5,3))
        self.assertEqual(attackBoard10, expected4)
        print(f"✓ black kill King under Thron: test passed")

        attack(attackBoard10,(6,4))
        self.assertEqual(attackBoard10, expected4)
        print(f"✓ black kill King under Thron: test passed")
        
        attack(attackBoard10,(5,5))
        self.assertEqual(attackBoard10, expected4)
        print(f"✓ black kill King under Thron: test passed")

        attack(attackBoard11,(3,5))
        self.assertEqual(attackBoard11, expected5)
        print(f"✓ black dont kill King right Thron: test passed")
        
        attack(attackBoard11,(5,5))
        self.assertEqual(attackBoard11, expected5)
        print(f"✓ black dont kill King right Thron: test passed")

        attack(attackBoard12,(3,5))
        self.assertEqual(attackBoard12, expected6)
        print(f"✓ black kill King right Thron: test passed")
        
        attack(attackBoard12,(4,6))
        self.assertEqual(attackBoard12, expected6)
        print(f"✓ black kill King right Thron: test passed")
        
        attack(attackBoard12,(5,5))
        self.assertEqual(attackBoard12, expected6)
        print(f"✓ black kill King right Thron: test passed")
        
        attack(attackBoard13,(2,4))
        self.assertEqual(attackBoard13, expected7)
        print(f"✓ black dont kill King over Thron: test passed")

        attack(attackBoard13,(3,5))
        self.assertEqual(attackBoard13, expected7)
        print(f"✓ black dont kill King over Thron: test passed")

        attack(attackBoard14,(2,4))
        self.assertEqual(attackBoard14, expected8)
        print(f"✓ black kill King over Thron: test passed")

        attack(attackBoard14,(3,5))
        self.assertEqual(attackBoard14, expected8)
        print(f"✓ black kill King over Thron: test passed")
        
        attack(attackBoard14,(3,3))
        self.assertEqual(attackBoard14, expected8)
        print(f"✓ black kill King over Thron: test passed")

    def test_KingOnThrone(self):
        
        expected1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected3 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        expected4 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected5 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        attack(attackBoard15,(3,4))
        self.assertEqual(attackBoard15, expected1)

        attack(attackBoard15,(5,4))
        self.assertEqual(attackBoard15, expected1)

        attack(attackBoard15,(4,3))
        self.assertEqual(attackBoard15, expected1)

        attack(attackBoard15,(4,5))
        self.assertEqual(attackBoard15, expected1)
        
        #Testet attackBoard16 
        attack(attackBoard16,(3,4))
        self.assertEqual(attackBoard16, expected2)
        attack(attackBoard16,(5,4))
        self.assertEqual(attackBoard16, expected2)
        attack(attackBoard16,(4,5))
        self.assertEqual(attackBoard16, expected2)

        #Testet attackBoard17:
        attack(attackBoard17,(3,4))
        self.assertEqual(attackBoard17, expected3)
        attack(attackBoard17,(5,4))
        self.assertEqual(attackBoard17, expected3)
        attack(attackBoard17,(4,3))
        self.assertEqual(attackBoard17, expected3)

        #Testet attackBoard18:
        attack(attackBoard18,(3,4))
        self.assertEqual(attackBoard18, expected4)
        attack(attackBoard18,(4,3))
        self.assertEqual(attackBoard18, expected4)
        attack(attackBoard18,(4,5))
        self.assertEqual(attackBoard18, expected4)

        #Testet attackBoard19:
        attack(attackBoard19,(5,4))
        self.assertEqual(attackBoard19, expected5)
        attack(attackBoard19,(4,3))
        self.assertEqual(attackBoard19, expected5)
        attack(attackBoard19,(4,5))
        self.assertEqual(attackBoard19, expected5)


        print(f"✓ King is sourrended Thron: test passed")

    # TODO TEST fertig schreiben! 
    
    def test_attackKingAnyOtherPlace(self):

        
        expected1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected2 = [
            [0, 0, B, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected3 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected4 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, B, 0, 0, 0, 0, 0, 0] 
        ]

        expected5 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, B, 0, 0] 
        ]

        expected6 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected7 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected8 = [
            [0, 0, 0, 0, 0, 0, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        attack(attackBoard20,(2,0))
        self.assertEqual(attackBoard20,expected1)
        attack(attackBoard202,(0,2))
        self.assertEqual(attackBoard202,expected2)
        attack(attackBoard203,(6,0))
        self.assertEqual(attackBoard203,expected3)
        attack(attackBoard204,(8,2))
        self.assertEqual(attackBoard204,expected4)
        attack(attackBoard205,(8,6))
        self.assertEqual(attackBoard205,expected5)
        attack(attackBoard206,(6,8))
        self.assertEqual(attackBoard206,expected6)
        attack(attackBoard207,(2,8))
        self.assertEqual(attackBoard207,expected7)
        attack(attackBoard208,(0,6))
        self.assertEqual(attackBoard208,expected8)


 

    def test_whiteAttacks(self):
        expected1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, W, 0, W, 0, W, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        expected2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, W, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, W, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, W, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        expected3 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, K, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, W, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        attack(attackBoard21,(3,3))
        self.assertEqual(attackBoard21,expected1 ) 
        attack(attackBoard22,(4,2))
        self.assertEqual(attackBoard22,expected2 )      
        attack(attackBoard23,(2,2))
        self.assertEqual(attackBoard23,expected3 ) 
        attack(attackBoard23,(4,2))
        self.assertEqual(attackBoard23,expected3 )      

        print(f"✓ White greift an: test passed")
    
    def test_corner(self):
        expected1 = [
            [0, W, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [W, B, 0, 0, 0, 0, 0, W, B],
            [0, W, 0, 0, 0, 0, W, B, 0] 
        ]
        expected2 = [
            [0, W, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [W, B, 0, 0, 0, 0, 0, W, B],
            [0, W, 0, 0, 0, 0, W, B, 0] 
        ]

        expected4 = [
            [0, W, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [W, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, W, B, 0] 
        ]

        expected5 = [
            [0, W, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [W, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, W, 0, 0] 
        ]

        expected6 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, B],
                [0, 0, 0, B, 0, B, B, 0, 0],
                [B, 0, 0, 0, W, 0, 0, 0, 0],
                [B, B, 0, W, 0, 0, 0, 0, B],
                [B, 0, 0, 0, 0, W, 0, B, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [B, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, B, B, B, W, 0, 0]
            ]
        
        expected7 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, B],
                [0, 0, 0, B, 0, B, B, 0, 0],
                [B, 0, 0, 0, W, 0, 0, 0, 0],
                [B, B, 0, W, 0, 0, 0, 0, B],
                [0, 0, 0, 0, 0, W, 0, B, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [B, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, B, 0, B, W, 0, 0]
            ]
        
        expected8 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, B],
                [0, 0, 0, B, 0, B, B, 0, 0],
                [B, 0, 0, 0, W, 0, 0, 0, 0],
                [B, B, 0, W, 0, 0, 0, 0, B],
                [0, 0, 0, 0, 0, W, 0, B, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, B],
                [B, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, W, 0, 0]
            ]
        
        expected9 = [
                [0, 0, 0, W, 0, W, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, B],
                [0, 0, 0, B, 0, B, B, 0, 0],
                [B, 0, 0, 0, W, 0, 0, 0, 0],
                [B, B, 0, W, 0, 0, 0, 0, B],
                [0, 0, 0, 0, 0, W, 0, B, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, B],
                [B, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, W, 0, 0]
            ]
        
        
        
        attack(attackBoard24,(2,0))
        self.assertEqual(attackBoard24,expected1) 
        
        attack(attackBoard24,(1,1))
        self.assertEqual(attackBoard24,expected2)
        
        attack(attackBoard24,(7,1)),expected2
        self.assertEqual(attackBoard24,expected2)
        
        attack(attackBoard24,(6,8))
        self.assertEqual(attackBoard24,expected4)

        attack(attackBoard24,(8,6))
        self.assertEqual(attackBoard24,expected5)
        
        attack(attackBoard25,(7,0))
        self.assertEqual(attackBoard25,expected6)

        attack(attackBoard25,(5,0))
        self.assertEqual(attackBoard25,expected6)

        attack(attackBoard26,(8,5))
        self.assertEqual(attackBoard26,expected7)

        attack(attackBoard26,(8,3))
        self.assertEqual(attackBoard26,expected7)

        attack(attackBoard27,(4,8))
        self.assertEqual(attackBoard27,expected8)

        attack(attackBoard27,(6,8))
        self.assertEqual(attackBoard27,expected8)

        attack(attackBoard28,(0,3))
        self.assertEqual(attackBoard28,expected9)

        attack(attackBoard28,(0,5))
        self.assertEqual(attackBoard28,expected9)


        print(f"✓ Corner Attacks: test passed")

    def test_savedKilledPos(self):

        board1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, B, W, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        cordiantes1 = attack(board1,(2,1))
        expected1 = [((3,1),config.W)]
        self.assertEqual(set(cordiantes1), set(expected1))

        board2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, B, W, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        cordiantes2 = attack(board2,(4,1))
        self.assertEqual(set(cordiantes2), set(expected1))


        cordiantes3 = attack(board1,(7,4))
        expected3 = [((7,3),config.W),((7,5),config.W)]
        self.assertEqual(set(cordiantes3), set(expected3))


        board4 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, B, K, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        cordiantes4 = attack(board4,(7,4))
        expected4 = [((7,3),config.K),((7,5),config.W)]
        self.assertEqual(set(cordiantes4), set(expected4))

        cordiantes5 = attack(board1,(2,7))
        expected5 = [(3,7)]
        self.assertEqual(set(cordiantes5), set(expected5))

        board5 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, B, W, B, W, B, W, W, 0],
            [0, W, 0, 0, 0, 0, 0, B, 0],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, B, 0, B, 0, 0, 0],
            [0, 0, B, K, B, W, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]
        
        cordiantes6 = attack(board5,(2,4))
        expected6 = [(2,3),(2,5)]
        self.assertEqual(set(cordiantes6), set(expected6))

        board6 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, B, 0, 0, 0, 0, 0, 0],
            [0, 0, K, 0, 0, 0, 0, 0, 0],
            [0, 0, B, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, W, 0, 0],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        cordiantes7 = attack(board6,(3,2))
        expected7 = [((2,2),config.K)]
        self.assertEqual(set(cordiantes7), set(expected7))

        cordiantes8 = attack(board6,(6,4))
        expected8 = [((5,4),config.W)]
        self.assertEqual(set(cordiantes8), set(expected8))

        cordiantes9 = attack(board6,(4,6))
        expected9 = [(4,5)]
        self.assertEqual(set(cordiantes9), set(expected9))

        board7 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, B, W, 0, W, B, 0, 0],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        cordiantes9 = attack(board7,(2,4))
        cordiantes10 = attack(board7,(4,6))
        cordiantes11 = attack(board7,(6,4))
        cordiantes12 = attack(board7,(4,2))

        expected9 = [((3,4),config.W)]
        expected10 = [((4,5),config.W)]
        expected11 = [((5,4),config.W)]
        expected12 = [((4,3),config.W)]

        self.assertEqual(set(cordiantes9), set(expected9))
        self.assertEqual(set(cordiantes10), set(expected10))
        self.assertEqual(set(cordiantes11), set(expected11))
        self.assertEqual(set(cordiantes12), set(expected12))


        board8 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, W, B, 0, B, W, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        ]

        cordiantes9 = attack(board8,(2,4))
        cordiantes10 = attack(board8,(4,6))
        cordiantes11 = attack(board8,(6,4))
        cordiantes12 = attack(board8,(4,2))

        expected9 = [(3,4)]
        expected10 = [(4,5)]
        expected11 = [(5,4)]
        expected12 = [(4,3)]

        self.assertEqual(set(cordiantes9), set(expected9))
        self.assertEqual(set(cordiantes10), set(expected10))
        self.assertEqual(set(cordiantes11), set(expected11))
        self.assertEqual(set(cordiantes12), set(expected12))
        

        board9 = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]

        cordiantes13 = attack(board9,(5,4))
        expected13 = [((4,4),config.K)]
        self.assertEqual(set(cordiantes13), set(expected13))

        cordiantes14 = attack(board9,(2,0))
        expected14 = [((1,0),config.K)]
        self.assertEqual(set(cordiantes14), set(expected14))
        
        cordiantes15 = attack(board9,(2,8))
        expected15 = [((1,8),config.K)]
        self.assertEqual(set(cordiantes15), set(expected15))

        cordiantes16 = attack(board9,(0,2))
        expected16 = [((0,1),config.K)]
        self.assertEqual(set(cordiantes16), set(expected16))

        cordiantes17 = attack(board9,(0,6))
        expected17 = [((0,7),config.K)]
        self.assertEqual(set(cordiantes17), set(expected17))

        cordiantes18 = attack(board9,(6,0))
        expected18 = [((7,0),config.K)]
        self.assertEqual(set(cordiantes18), set(expected18))

        cordiantes19 = attack(board9,(6,8))
        expected19 = [((7,8),config.K)]
        self.assertEqual(set(cordiantes19), set(expected19))

        cordiantes20 = attack(board9,(8,2))
        expected20 = [((8,1),config.K)]
        self.assertEqual(set(cordiantes20), set(expected20))

        cordiantes21 = attack(board9,(8,6))
        expected21 = [((8,7),config.K)]
        self.assertEqual(set(cordiantes21), set(expected21))

        board10 = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]
        
        cordiantes22 = attack(board10,(4,5))
        
        self.assertEqual(set(cordiantes22), set(expected13))


        board = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]
        
        cordiantes = attack(board,(4,3))
        self.assertEqual(set(cordiantes), set(expected13))

        board = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]
        
        cordiantes = attack(board,(3,4))
        self.assertEqual(set(cordiantes), set(expected13))

        board = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, B, 0, 0, 0, B],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]

        cordiantes = attack(board,(2,4))
        expected =[((3,4),config.W)]
        self.assertEqual(set(cordiantes), set(expected))


        board = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, B, W, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]

        cordiantes = attack(board,(4,2))
        expected =[((4,3),config.W)]
        self.assertEqual(set(cordiantes), set(expected))

        board = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, W, B, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]

        cordiantes = attack(board,(4,6))
        expected =[((4,5),config.W)]
        self.assertEqual(set(cordiantes), set(expected))

        board = [
            [0, K, B, 0, 0, 0, B, K, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, K],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, W, B, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, B, W, B, 0, 0, 0, B],
            [K, 0, B, K, B, 0, 0, 0, K],
            [0, K, B, 0, 0, 0, B, K, 0] 
        ]
        
        cordiantes = attack(board,(6,2))
        expected =[((6,3),config.W)]
        self.assertEqual(set(cordiantes), set(expected))

        cordiantes = attack(board,(7,2))
        expected =[((7,3),config.K)]
        self.assertEqual(set(cordiantes), set(expected))


        board9 = [
            [0, B, W, 0, 0, 0, W, B, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [W, 0, 0, 0, 0, 0, 0, 0, W],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, W, B, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [W, 0, B, W, B, 0, 0, 0, W],
            [B, 0, B, K, B, 0, 0, 0, B],
            [0, B, W, 0, 0, 0, W, B, 0] 
        ]

        cordiantes14 = attack(board9,(2,0))
        expected14 = [(1,0)]
        self.assertEqual(set(cordiantes14), set(expected14))
        
        cordiantes15 = attack(board9,(2,8))
        expected15 = [(1,8)]
        self.assertEqual(set(cordiantes15), set(expected15))

        cordiantes16 = attack(board9,(0,2))
        expected16 = [(0,1)]
        self.assertEqual(set(cordiantes16), set(expected16))

        cordiantes17 = attack(board9,(0,6))
        expected17 = [(0,7)]
        self.assertEqual(set(cordiantes17), set(expected17))

        cordiantes18 = attack(board9,(6,0))
        expected18 = [(7,0)]
        self.assertEqual(set(cordiantes18), set(expected18))

        cordiantes19 = attack(board9,(6,8))
        expected19 = [(7,8)]
        self.assertEqual(set(cordiantes19), set(expected19))

        cordiantes20 = attack(board9,(8,2))
        expected20 = [(8,1)]
        self.assertEqual(set(cordiantes20), set(expected20))

        cordiantes21 = attack(board9,(8,6))
        expected21 = [(8,7)]
        self.assertEqual(set(cordiantes21), set(expected21))

        board = [
            [0, K, B, 0, 0, 0, B, W, 0],
            [K, 0, 0, 0, 0, 0, 0, 0, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, K, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [K, 0, 0, 0, 0, 0, 0, 0, W],
            [0, K, B, 0, 0, 0, B, W, 0] 
        ]

        cordiantes = attack(board,(0,6))
        expected = [((0,7),config.W)]
        self.assertEqual(set(cordiantes), set(expected))

        cordiantes = attack(board,(8,6))
        expected = [((8,7),config.W)]
        self.assertEqual(set(cordiantes), set(expected))

        print(f"✓ Attacks: killed figure and Positions correct saved")
    
    



if __name__ == '__main__':
    unittest.main()
