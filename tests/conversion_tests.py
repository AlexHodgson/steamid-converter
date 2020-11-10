import sys
sys.path.append(r'A:\Documents\GitHub\steamid-converter\steamid_converter')

import unittest
import Converter # Code being tested

class TestConversions(unittest.TestCase):

    def test_steamID64(self): # Test conversion to steamID64

        self.assertEqual(Converter.to_steamID64("[U:1:94253115]"), Converter.to_steamID64("STEAM_0:1:47126557")) # Corresponding steamID3 and SteamID
        self.assertEqual(Converter.to_steamID64("[U:1:11926250]"), Converter.to_steamID64("STEAM_0:0:5963125"))


if __name__ == '__main__':
    unittest.main()
