## XBE Save Patcher for XBMC
A utility that modifies the hex of .XBE files to read/write save files from "F:\TDATA\" instead of "E:\TDATA\", or from the first partition of your secondary HDD (Cerbios users only).

## Installation:
- Install script to "Q:\scripts\XBESavePatcher" (must be installed there as script paths are hardcoded!)

## How to use:
- Run the script
- Select "Patch .XBE Save Folder (E:\ to F:\)"
- Select the game .xbe you'd like to modify (make sure you're using an extracted copy of the game you're patching, attach.xbe files will not work!)
- Select the folder you'd like to save the modified .xbe in and what name you'd like to save it under.
- ???
- Profit.

## Bugs:
- You tell me.

## Why?
To offer an easy way to run multiple save games from one game. You may want to use this if you're using modded saves, or share your Xbox with someone who want to have their own saves, or to avoid the dreaded 240 save game bug. 

## TODO:
- Implement basic error checking to make sure non-TDATA/UDATA strings don't get replaced.
- Test Dual-HDD support (you can test this yourself from the patch menu, this is currently fully untested by me as I don't have the right setup! Saves will default to the first partition on your secondary HDD.)
