Hyperion LED Health Effects for PoE
=======================
This is a Hyperion Effect that I made for PoE. It allows you to keep track of your HP from your backlight. I have bundled part of the [Hyperion SDK](https://github.com/Fabi1080/hyperion_effects_dev_kit) to make this simpler to create / consume.

To run:
- Download theis repository
- Modify `main.py` to match your hyperion server config + led numbers + offsets
- Run `main.py`
- Enjoy backlighting for your health from your LEDS

=======================
hyperion_effects_dev_kit
=======================

Some python modules to simplify the hyperion effects development.  
Created with python 2.7  

Develop code for hyperion effects.  
See what your effect does in a gui.  
Send the colordata of your effect to hyperion's Json server.  


Modify the effects.py module to develop your effect.  
The hyperion.py module holds functions the fake the real hyperion functions.  
The gui.py module holds functions to open a window which displays the led colors.  
The json_client.py module contains functions to communicate with the json server.  
