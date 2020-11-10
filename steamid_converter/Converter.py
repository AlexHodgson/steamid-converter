import re

def to_steamID(steamID):
    pass

def to_steamID3(steamID):
    pass

def to_steamID64(steamID):
    """Convert steamID or steamID3 to steamID64

    Parameters:
    int/str : steamID - Steam id to convert
    """

    id_str = str(steamID)

    if re.search("^STEAM_", id_str): # If passed steamID

        id64_base = 76561197960265728 # steamID64 are all offset from this value

        id_split = id_str.split(":") # Split string into 'Universe', Account type, and Account number
        
        account_type = int(id_split[1]) # Check for account type
        account_id = int(id_split[2]) # Account number, needs to be doubled when added to id64

        return id64_base + (account_id * 2) + account_type

    elif re.search("^\[.*\]$", id_str): # If passed steamID3
        
        id_split = id_str.split(":") # Split steamID3

        account_id3 = int(id_split[2][:-1]) # Remove ] from end of id3

        if account_id3 % 2 == 0:
            account_type = 0
            account_id = account_id3 // 2
        else:
            account_type = 1
            account_id = (account_id3 - 1) // 2

        id64_str = "7656119" + str((account_id * 2) + (7960265728 + account_type))

        return int(id64_str)
    else:
        raise ValueError(f"Unable to decode steamID: {steamID}")







    