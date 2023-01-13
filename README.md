# SteamID Converter

Provides easy conversions between different SteamID formats in native Python 

[![Downloads](https://pepy.tech/badge/steamid-converter)](https://pepy.tech/project/steamid-converter) 
[![GitHub license](https://img.shields.io/github/license/AlexHodgson/steamid-converter)](https://github.com/AlexHodgson/steamid-converter/blob/main/LICENSE)


## Overview

Steam provides 3 types of ID for each unique account on the platform: SteamID, SteamID3 and SteamID64

ID | SteamID | SteamID3 | SteamID64
---|---------|----------|----------   
Format| STEAM_0:<zero-width space>X:XXXXXXXX | \[U:1:XXXXXXXX\] | 17 digit int


This package provides conversions between these formats.\
For more in-depth information on steamIDs see the [Valve Software Wiki Page](https://developer.valvesoftware.com/wiki/SteamID)

## Functionality

All functions currently avaliable are located in ```steamid_converter.Converter```\
Each function can take any of the steamID formats (Including the function's target format) as a string or integer. Then will return that ID converted to the function's target format.

### Avaliable Functions

```python
Converter.to_steamID(steamID)
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

Converter.to_steamID3(steamID)
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

Converter.to_steamID64(steamID, as_int=False)
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
```

## Other Info

This package was created by [Alex Hodgson](https://github.com/AlexHodgson)

Steam is a copyright of Valve Corporation, Valve Corporation is in no way affiliated with this package or it's author.
