import re
import math

def to_steamID(steamID):
    """
    Convert to steamID

    A steamID is unique to each steam account, 
    Formatted with digits as x "STEAM_0:x:xxxxxxxx"

    Parameters
    ----------
    steamID : int or str
        steamID3 or steamID64 to convert to steamID

    Returns
    -------
    str
        steamID value

    """

    id_str = str(steamID)

    if re.search("^STEAM_", id_str): # Already a steamID
        return id_str

    elif re.search("^\[.*\]$", id_str): # If passed steamID3

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
    """
    Convert to steamID3

    A steamID3 is unique to each steam account, 
    Formatted with digits as x "[U:1:xxxxxxxx]"

    Parameters
    ----------
    steamID : int or str
        steamID or steamID64 to convert to steamID3

    Returns
    -------
    str
        steamID3 value

    """

    id_str = str(steamID)

    if re.search("^\[.*\]$", id_str): # Already a steamID3
        return id_str

    elif re.search("^STEAM_", id_str): # If passed steamID

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
    """
    Convert to steamID64

    A steamID64 is a 17 digit number, unique to each steam account

    Parameters
    ----------
    steamID : int or str
        steamID or steamID3 to convert to steamID64
    as_int : bool
        If the steamID64 is returned as an integer rather than string, Default = False

    Returns
    -------
    int or str
        steamID64 value

    """

    id_str = str(steamID)
    id_split = id_str.split(":") # Split string into 'Universe', Account type, and Account number
    id64_base = 76561197960265728 # steamID64 are all offset from this value

    if id_str.isnumeric(): # Already a steamID64

        check_steamID64_length(id_str) # Validate id passed in
        if as_int:
            return id64
        else:
            return str(id64)

    elif re.search("^STEAM_", id_str): # If passed steamID
        
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
    """
    Check if a steamID64 is of the correct length, raises ValueError if not.

    Not really for you to use

    Parameters
    ----------
    id_str : str
        steamID64 to check length of

    """

    if len(id_str) != 17:
        raise ValueError(f"Incorrect length for steamID64: {id_str}")






    