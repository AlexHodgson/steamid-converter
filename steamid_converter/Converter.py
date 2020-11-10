import re

def to_steamID(steamID):
    pass

def to_steamID3(steamID):
    """Convert to steamID3 from steamID or steamID64

    Parameters:
    int/str : steamID - Steam id to convert
    """

    id_str = str(steamID)

    if re.search("^STEAM_", id_str): # If passed steamID

        id_split = id_str.split(":") # Split string into 'Universe', Account type, and Account number

        account_type = int(id_split[1]) # Check for account type
        account_id = int(id_split[2]) # Account number, needs to be doubled when added to id3

        return "[U:1:" + str((account_id * 2) - account_type) + "]"




    elif id_str.isnumeric(): # Passed steamID64

        id64_base = 76561197960265728 # steamID64 are all offset from this value

        offset_id = int(id_str) - id64_base

        if offset_id % 2 == 0:
            account_type = 0
            account_id = offset_id // 2
        else:
            account_type = 1
            account_id = ((offset_id - 1) // 2) + 1

        return "[U:1:" + str((account_id * 2) - account_type) + "]"


def to_steamID64(steamID):
    """Convert to steamID64 from steamID or steamID3

    Parameters:
    int/str : steamID - Steam id to convert
    """

    id_str = str(steamID)
    id_split = id_str.split(":") # Split string into 'Universe', Account type, and Account number
    id64_base = 76561197960265728 # steamID64 are all offset from this value

    if re.search("^STEAM_", id_str): # If passed steamID
        
        account_type = int(id_split[1]) # Check for account type
        account_id = int(id_split[2]) # Account number, needs to be doubled when added to id64

        return id64_base + (account_id * 2) + account_type

    elif re.search("^\[.*\]$", id_str): # If passed steamID3

        account_id3 = int(id_split[2][:-1]) # Remove ] from end of steamID3

        if account_id3 % 2 == 0:
            account_type = 0
            account_id = account_id3 // 2
        else:
            account_type = 1
            account_id = (account_id3 - 1) // 2

        return id64_base + (account_id * 2) + account_type

    else:
        raise ValueError(f"Unable to decode steamID: {steamID}")







    