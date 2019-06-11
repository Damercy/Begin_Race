# Introduction  

Hello! This is a beginner project game made using _Python_ and _pygame_ library. It was heavily inspired by Sentdex. I hope you like what you see here and enjoy **_THE GAME!_**  

**Warning**: The following is a work in progress and a beginner trying to understand stuff.  

Here you go!  

>![THE GAME][Gameplay Picture here]

## Features  

**THE GAME** features the following functionalities (_and with many more to come, of course!_):
> * A counter to count no. of objects dodged
> * An incrementally increasing level as you progress through the game
> * Background sounds including crash sound & gameplay music
> * Button functions
> * Pause menu to resume or quit the game (PRESS **'p'** to _PAUSE_ THE GAME) 
> * Most importantly, this game features my dog **_POLO_** starring as the _icon_! (Seriously, what more do you want now?)

The **MENU SCREEN** & **PAUSE SCREEN** was also made later so that the game doesn't just simply.._Begin_. They serve as a UI for the user.

>![MENU SCREEN][Menu_screen Picture here]  
>
>![PAUSE SCREEN][Pause_screen Picture here] 

The **CRASHED SCREEN** was also developed with text being displayed as "_You Crashed_" when the car object hits the blue block(s) or even the side of the 800 x 600 screen.  
A sound is also generated during the crash which can be heard when playing the game.  

>![CRASH SCREEN][Crash_screen Picture here]  

# HOW TO PLAY

> The objective of the game is simple ---- To AVOID getting crashed!  
>
> The Car only moves sideways, so to move left , press the **left arrow** (![Left arrow][L_Icon]) on your keyboard and similarly, press  >   **right arrow** (![Right arrow][R_Icon]) to move right.  
>
> Also avoid hitting the edges of the screen (window) to avoid crashing.  
>
> Keep on playing and dodging objects. For every _10_ objects you surpass , the speed of the car automatically increases thereby >  increasing the difficulty. 
>
> Press 'p' to pause the game.

## HOW TO CLONE AND START PLAYING  

Simply clone this repository and in the local copy in your machine , open the folder that corresponds to the directory '**THE GAME**'. 
Or in other words, move to this location : '[Your download path here]\Begin_Race\The GAME  
>
Then click the **game.exe** file to start the game.  
>
For modifications to the game files including changing FPS from the current 60FPS,or to add your own sound files/icons/image sprites or any change whatsoever, open the file **Game.py** in the downloaded repo and modify this **.py** file as required.
>
Hope you like it!

>The project is incomplete in the sense that I plan on to make the following modifications in the near future:-
>  * Add background
>  * Add complex crash functionality like fires & smoke
>  * Add better sounds


[Gameplay Picture here]:https://github.com/Damercy/Begin_Race/blob/master/Screenshots/Gameplay.png
[Menu_screen Picture here]:https://github.com/Damercy/Begin_Race/blob/master/Screenshots/Menu.png
[Pause_screen Picture here]:https://github.com/Damercy/Begin_Race/blob/master/Screenshots/Pause.png  
[Crash_screen Picture here]:https://github.com/Damercy/Begin_Race/blob/master/Screenshots/Crashed.png
[L_Icon]:data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAaVBMVEX///8AAADv7+/h4eHl5eX29vaPj48kJCSVlZX5+fnt7e2SkpKWlpbg4OAoKCjV1dV4eHhgYGBVVVXIyMiGhoYWFhbAwMB/f3+np6c6OjrT09NHR0caGho/Pz8PDw8uLi63t7dxcXGenp7TFKP5AAADdklEQVR4nO2da3OiQBBFZ0yy7JIVjYqPqODu//+RC1bWGAGZnjjV0z33fE5R99aB5hVGYwAAAAAAAAAAAADSZrk5Fod6v3rnDhKIrb1QrLnDBCDf2WveuPM8nCd7Q/3CHemxdApam6mq+NwtqKtij0FdFXsNnkfqL+5oj2HAoB6LgwbPFRVYvGPwvKOKtzhSsDkvcif8JqMFpV/dOBS0VvI16t0hcyHjjumPk8GGJXdQX9wMNmy4k3riatDaI3dUP5wNNnBn9cLdoNCGpIISG9IKVtxx6dAK2gV3XjKUIdOy5Q5MhWjQ2gl3YiJUg/YPd2IiZINW2B0i2aC0q1K6wb/ckWmgYIef3JFp0Av+5o5Mgz5kYDAuYDA9g8IK4jSRnsFX7sg01BukDxkYjAsY7CDsNAGD6RUUtovCoHSDGDLpGfzBHZmG+iGDYxAFI4deEEMmLnCagMHIUT9kYBAFIwcFpRfEkJFeEAalF4RBFIwcesG5mURIPvSv1vSC8bLY9rSkD5m46RxAmgx+MFNt8MxSt8GWmW6DLcoNNqy0F/z4hEXtLtpyagpOuEMEZd40PHKHCMruy6pcGqmM4Y4QGrPmThAas+JOEBrlc6bBVNwJQqN+0FhTcicIjdlzJwhNArN0yZ0gNAlc02i/Li2be4uaO0RQFurvD1/V3+PPdD9p+1ypUW/FyyqGWiterdmk84Fieb0mrEaLVa783dP+dkEjZRbL0+37Q1UVy3n/ek3kitX0hfudfS/Di06Tj8VK2vJrKVSkH4viKsJiD/n4RuMCFpO0iIoRgooaKmLcaKhIt/jMHZkKLKZpERXjAxU1VMS40VARFjVUpFt84o5MJQGL9IoJWEyg4pQ7MhX6uBFXERY1VITFHmbjG42LBCzSK8JifCRgEeNGQ0VY1FARFlFRBKiooSIeFXfJuBOTIVsUtvpZw5RaUdgPApsEfpebfCy+cef1gFbxwB3XB1pF7rRekCpyh/WDMm64s3ribnHHHdUXZ4tz7qTeuJ76+7+4EoGbRZEni/84HYsn7pTfwqHiYnwrUTNasR7+MFAIIxULeTcWHe6Om0y8wZY7FjMFBlsGLRYqDLYMWNRisKXXooYh80mPRU0GWzoVa2UFjcl3XwpKfDYzytUKYtl6/M9Fst4ci0O9X71zBwEAAAAAAAAAAAAQwT8350l0+kRC+wAAAABJRU5ErkJggg==
[R_Icon]:data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAaVBMVEX///8eIB0ACACdnZwAAAAbHRrY2NgaHRnU1dTZ2tnJycnHyMfLzMvU1NTExcTBwcGwsbAXGRW4uLgwMi8MEAvv7+8+Pz2UlJSpqaloaWjh4eBgYWDz9POtra0ABACLjItwcXA2NzUjJSI95uYCAAAClklEQVR4nO3d4XKaQBTF8QUupTYaJYIxxiTa93/IQmoyVJZvZZg99/97gj1zdveq0RACAAAAAAAAAAAAAGAZq+NzsWuXXsV81lezPDd7Vc1YWJ19avLV0muZxZtlXyr7sfRqZtBa+Z0wK02wxY88y4YR9VrcV8OEghu1tSy7iyi2UUcJ5c7iOb9PKHcWD/UoothZLEbbVO4sNuU4otZG3Vg0olKL63hEpRa9RtS6UYmowGtEhkZiaFGBg4i/nN6oWhFpUUG0RYZGYmhRgYOIDA0FtKiAoaGAFhU4iDixUX8uva7/aKJFpYi0qGCiRa6bpNCiAiIqcBDxQT+i3xYZGklh9CsgogIHERn9Chj9Chj9ChzcqOtmnPAuYrs9Fgk7vo5/FNZH3HzlO72YvecpiwUcRNxarGQFt40a/WOAiNJOXcJKN2CW1dcQdpHfNQqxxxC9hnQ0l/B76TXMq7yGpZcwu3BVvmi6Dvfhon0O60s375dexKy6uzTslUusD93EXwm/pqms/fuyTfd16e2ld3sRf2/ROT9ovz9M3sR7fJ2A8p/TeA2o83mp/Kelj+oNyp/BiQZ1AtJg6giYOvkxId/gVr/BcT4PDSoFlG+wImDSHJxB8THh4JKJBqTBZPgMWBEwHV4vGZ2AT/GAOv/bhAZTN3GLijdIwIT4DOjgFpUPqDMmaDB18rdo9GcSBEyIz4BKt6jXgDpjQr7Bt/glI96g0i0abZAzmJCJMygfUGeLTpxBnQYnvumk02DI1R8QoP88YPlnOus/lzv2bHWpgOH8Ln0Ge/tSPGD4yP8NqLVFe+3wa5VSg/7b0QYB9RrsFXYbiY1kg73NwSzPzV7apVcyn9PxudgJ5wMAAAAAAAAAAACAOf0BIho4QWE7sgwAAAAASUVORK5CYII=

