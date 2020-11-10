import sys
sys.path.append(r'A:\Documents\GitHub\steamid-converter\steamid_converter') # TODO make this relative

import unittest
import Converter # Code being tested

class TestConversions(unittest.TestCase):
    '''
    Test that the id conversion functions are giving the correct results
    The accounts being tested represent both account types (0 and 1)
    '''

    def test_steamID(self): 
        '''Test conversion to steamID'''

        self.assertEqual(Converter.to_steamID("76561197972191978"), "STEAM_0:0:5963125") # Test a known conversion
        self.assertEqual(Converter.to_steamID("76561198054518843"), "STEAM_0:1:47126557")

        self.assertEqual(Converter.to_steamID("76561197972191978"), Converter.to_steamID("[U:1:11926250]"))   # Corresponding steamID3 and SteamID
        self.assertEqual(Converter.to_steamID("76561198054518843"), Converter.to_steamID("[U:1:94253115]")) 
    

    def test_steamID3(self):
        '''Test conversion to steamID3'''

        self.assertEqual(Converter.to_steamID3("76561197972191978"), "[U:1:11926250]") # Test a known conversion
        self.assertEqual(Converter.to_steamID3("76561198054518843"), "[U:1:94253115]")

        self.assertEqual(Converter.to_steamID3("76561197972191978"), Converter.to_steamID3("STEAM_0:0:5963125")) # Corresponding steamID3 and SteamID
        self.assertEqual(Converter.to_steamID3("76561198054518843"), Converter.to_steamID3("STEAM_0:1:47126557")) 
        

    def test_steamID64(self):
        '''Test conversion to steamID64'''

        self.assertEqual(Converter.to_steamID64("[U:1:94253115]"), "76561198054518843") # Test a known conversion
        self.assertEqual(Converter.to_steamID64("[U:1:11926250]"), "76561197972191978")

        self.assertEqual(Converter.to_steamID64("[U:1:94253115]"), Converter.to_steamID64("STEAM_0:1:47126557")) # Corresponding steamID3 and SteamID
        self.assertEqual(Converter.to_steamID64("[U:1:11926250]"), Converter.to_steamID64("STEAM_0:0:5963125"))   

class TestHelpers(unittest.TestCase):
    '''Check other functions in Converter.py are working'''
    
    def test_steamID64_length(self):
        
        self.assertRaises(ValueError, Converter.check_steamID64_length, "1"*15) # Raises error if steamID64 is not 17 digits, does nothing otherwise
        self.assertIsNone(Converter.check_steamID64_length("1"*17))

if __name__ == '__main__':
    unittest.main()
