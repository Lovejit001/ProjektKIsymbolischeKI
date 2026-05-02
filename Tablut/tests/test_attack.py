import unittest

import scr.config
from scr.attack import *
from tests.definitions import attackBoard1,attackBoard2,attackBoard3,attackBoard4,attackBoard5,attackBoard6,attackBoard7,attackBoard8,attackBoard9,attackBoard10,attackBoard11,attackBoard12,attackBoard13,attackBoard14,attackBoard15,attackBoard16,attackBoard17,attackBoard18,attackBoard19,attackBoard20,attackBoard21,attackBoard22,attackBoard23,attackBoard24,K,B,W


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

        self.assertEqual(attack(attackBoard1,(1,3)), expected)
        print(f"✓ blackAttackWhite left and right: test passed")
        self.assertEqual(attack(attackBoard1,(4,4)), expected)
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
        

        self.assertEqual(attack(attackBoard2,(2,1)), expected)
        print(f"✓ blackAttackWhite vertical attack down: test passed")
        self.assertEqual(attack(attackBoard2,(4,1)), expected)
        print(f"✓ blackAttackWhite vertical attack up: test passed")

        self.assertEqual(attack(attackBoard3,(6,3)), expected2)
        print(f"✓ blackAttackWhite horizontal attack right: test passed")
        self.assertEqual(attack(attackBoard4,(6,5)), expected2)
        print(f"✓ blackAttackWhite horizontal attack left: test passed")

        self.assertEqual(attack(attackBoard5,(3,7)), expected5)
        print(f"✓ blackAttackWhite vertical double attack: test passed")

        self.assertEqual(attack(attackBoard6,(7,4)), expected6)
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
        
        self.assertEqual(attack(attackBoard7,(4,2)), expected1)
        print(f"✓ black dont kill King: test passed")

        self.assertEqual(attack(attackBoard8,(4,2)), expected2)
        print(f"✓ black kill King: test passed")

        self.assertEqual(attack(attackBoard8,(3,3)), expected2)
        print(f"✓ black kill King: test passed")
        
        self.assertEqual(attack(attackBoard8,(5,3)), expected2)
        print(f"✓ black kill King: test passed")
        

        self.assertEqual(attack(attackBoard9,(5,3)), expected3)
        print(f"✓ black dont kill King: test passed")

        self.assertEqual(attack(attackBoard9,(5,5)), expected3)
        print(f"✓ black dont kill King: test passed")


        self.assertEqual(attack(attackBoard10,(5,3)), expected4)
        print(f"✓ black kill King under Thron: test passed")

        self.assertEqual(attack(attackBoard10,(6,4)), expected4)
        print(f"✓ black kill King under Thron: test passed")
        
        self.assertEqual(attack(attackBoard10,(5,5)), expected4)
        print(f"✓ black kill King under Thron: test passed")

        self.assertEqual(attack(attackBoard11,(3,5)), expected5)
        print(f"✓ black dont kill King right Thron: test passed")
        
        self.assertEqual(attack(attackBoard11,(5,5)), expected5)
        print(f"✓ black dont kill King right Thron: test passed")

        self.assertEqual(attack(attackBoard12,(3,5)), expected6)
        print(f"✓ black kill King right Thron: test passed")
        
        self.assertEqual(attack(attackBoard12,(4,6)), expected6)
        print(f"✓ black kill King right Thron: test passed")
        
        self.assertEqual(attack(attackBoard12,(5,5)), expected6)
        print(f"✓ black kill King right Thron: test passed")
        
        self.assertEqual(attack(attackBoard13,(2,4)), expected7)
        print(f"✓ black dont kill King over Thron: test passed")

        self.assertEqual(attack(attackBoard13,(3,5)), expected7)
        print(f"✓ black dont kill King over Thron: test passed")

        self.assertEqual(attack(attackBoard14,(2,4)), expected8)
        print(f"✓ black kill King over Thron: test passed")

        self.assertEqual(attack(attackBoard14,(3,5)), expected8)
        print(f"✓ black kill King over Thron: test passed")
        
        self.assertEqual(attack(attackBoard14,(3,3)), expected8)
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

        self.assertEqual(attack(attackBoard15,(3,4)), expected1)
        self.assertEqual(attack(attackBoard15,(5,4)), expected1)
        self.assertEqual(attack(attackBoard15,(4,3)), expected1)
        self.assertEqual(attack(attackBoard15,(4,5)), expected1)
        
        #Testet attackBoard16 
        self.assertEqual(attack(attackBoard16,(3,4)), expected2)
        self.assertEqual(attack(attackBoard16,(5,4)), expected2)
        self.assertEqual(attack(attackBoard16,(4,5)), expected2)

        #Testet attackBoard17:
        self.assertEqual(attack(attackBoard17,(3,4)), expected3)
        self.assertEqual(attack(attackBoard17,(5,4)), expected3)
        self.assertEqual(attack(attackBoard17,(4,3)), expected3)

        #Testet attackBoard18:
        self.assertEqual(attack(attackBoard18,(3,4)), expected4)
        self.assertEqual(attack(attackBoard18,(4,3)), expected4)
        self.assertEqual(attack(attackBoard18,(4,5)), expected4)

        #Testet attackBoard19:
        self.assertEqual(attack(attackBoard19,(5,4)), expected5)
        self.assertEqual(attack(attackBoard19,(4,3)), expected5)
        self.assertEqual(attack(attackBoard19,(4,5)), expected5)


        print(f"✓ King is sourrended Thron: test passed")

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

        self.assertEqual(attack(attackBoard20,(2,0)),expected1 )        

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
        

        self.assertEqual(attack(attackBoard21,(3,3)),expected1 ) 
        self.assertEqual(attack(attackBoard22,(4,2)),expected2 )      
        self.assertEqual(attack(attackBoard23,(2,2)),expected3 ) 
        self.assertEqual(attack(attackBoard23,(4,2)),expected3 )      

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
            [0, 0, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [W, B, 0, 0, 0, 0, 0, W, B],
            [0, W, 0, 0, 0, 0, W, B, 0] 
        ]

        expected3 = [
            [0, 0, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [0, B, 0, 0, 0, 0, 0, W, B],
            [0, 0, 0, 0, 0, 0, W, B, 0] 
        ]

        expected4 = [
            [0, 0, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, W, B, 0] 
        ]
        expected5 = [
            [0, 0, 0, 0, 0, 0, 0, W, 0],
            [0, B, 0, 0, 0, 0, 0, B, W],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, W, 0, 0] 
        ]
        
        expected6 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, B, 0, 0, 0, 0, 0, B, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, B],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, 0, W],
            [0, B, 0, 0, 0, 0, 0, W, 0],
            [0, 0, 0, 0, 0, 0, W, 0, 0] 
        ]

        self.assertEqual(attack(attackBoard24,(2,0)),expected1) 
        self.assertEqual(attack(attackBoard24,(1,1)),expected2)
        self.assertEqual(attack(attackBoard24,(7,1)),expected3)
        self.assertEqual(attack(attackBoard24,(6,8)),expected4)
        self.assertEqual(attack(attackBoard24,(8,6)),expected5)
        self.assertEqual(attack(attackBoard24,(1,7)),expected6)

        print(f"✓ Corner Attacks: test passed")







if __name__ == '__main__':
    unittest.main()
