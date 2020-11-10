import re
import math

def to_steamID(steamID):
    """Convert to steamID from steamID3 or steamID64

    Parameters:
    int/str : steamID - Steam id to convert
    """

    id_str = str(steamID)

    if re.search("^\[.*\]$", id_str): # If passed steamID3

        id_split = id_str.split(":") # Split string into 'Universe', Account type, and Account number
        account_id3 = int(id_split[2][:-1]) # Remove ] from end of steamID3

        if account_id3 % 2 == 0:
            account_type = 0
        else:
            account_type = 1

        account_id = (account_id3 - account_type) // 2

    elif id_str.isnumeric(): # Passed steamID64

        check_steamID64_length(id_str) # Validate id passed in

        id64_base = 76561197960265728 # steamID64 are all offset from this value
        offset_id = int(id_str) - id64_base

        # Get the account type and id
        if offset_id % 2 == 0:
            account_type = 0
        else:
            account_type = 1

        account_id = ((offset_id - account_type) // 2)

    return "STEAM_0:" + str(account_type) + ":" + str(account_id)

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

        # Join together in steamID3 format
        return "[U:1:" + str(((account_id + account_type) * 2) - account_type) + "]"

    elif id_str.isnumeric(): # Passed steamID64
        
        check_steamID64_length(id_str) # Validate id passed in

        id64_base = 76561197960265728 # steamID64 are all offset from this value
        offset_id = int(id_str) - id64_base

        # Get the account type and id
        if offset_id % 2 == 0:
            account_type = 0
        else:
            account_type = 1

        account_id = ((offset_id - account_type) // 2) + account_type

        # Join together in steamID3 format
        return "[U:1:" + str((account_id * 2) - account_type) + "]"
        
    else:
        raise ValueError(f"Unable to decode steamID: {steamID}")


def to_steamID64(steamID, as_int = False):
    """Convert to steamID64 from steamID or steamID3

    Parameters:
    int/str : steamID - Steam id to convert
    Bool  : as_int - If the steamID64 is returned in integer format, Default = False
    """

    id_str = str(steamID)
    id_split = id_str.split(":") # Split string into 'Universe', Account type, and Account number
    id64_base = 76561197960265728 # steamID64 are all offset from this value

    if re.search("^STEAM_", id_str): # If passed steamID
        
        account_type = int(id_split[1]) # Check for account type
        account_id = int(id_split[2]) # Account number, needs to be doubled when added to id64

    elif re.search("^\[.*\]$", id_str): # If passed steamID3

        account_id3 = int(id_split[2][:-1]) # Remove ] from end of steamID3

        if account_id3 % 2 == 0:
            account_type = 0
        else:
            account_type = 1

        account_id = (account_id3 - account_type) // 2

    else:
        raise ValueError(f"Unable to decode steamID: {steamID}")


    id64 = id64_base + (account_id * 2) + account_type

    # Check if returning as string or integer
    if as_int:
        return id64
    else:
        return str(id64)


def check_steamID64_length(id_str :str):
    # All steamId64 should be 17 digits in length

    if len(id_str) != 17:
        raise ValueError(f"Incorrect length for steamID64: {id_str}")






    