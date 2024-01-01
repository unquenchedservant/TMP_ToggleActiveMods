# TMP_ToggleActiveMods
A small interface to quickly activate mods for TruckersMP. 

Simply grab the executable from the Releases tab and place it in to your mod folder for either ATSMP or ETS2MP.

Run it whenever you want to enable or disable certain mods (this mainly applies for Frosty's Winter Mod). 

Because this script dynamically checks the files at launch, it's compatible with any mod. 

Includes buttons for quickly disabling/enabling all mods. 

I made this for myself, mainly because there's sometimes I want to play with physics on, and sometimes I don't, 
and with the new map DLCs I hadn't explored, I wanted winter off while I played for a bit. 

## What this does
It simply scans the folder it's in for any .scs file and puts it in to a nice little UI with checkboxes. 
Because the way TMP typically works with the mods is based on file name, all you need to do to deactivate a mod is 
change the file name. I've chosen "INACTIVE_" as a prefix for file names, but I believe just about anything would do. 

You check the checkbox, it marks the file as active or inactive, by simply changing the file name. 

## WARNING
Only works for TruckersMP. The base game doesn't care about the name of a mod. Doesn't work for ProMods, but to be fair, 
you can just go to another map for ETS2. And let's be honest, this tool is only for the laziest of us, and we can afford to expend
a little bit of energy moving the mod file for promods. 

## Mac & Linux
Currently this version only works on Windows. Once I get off my lazy butt and compile this on my Mac, a Mac/Linux version will exist. 
 