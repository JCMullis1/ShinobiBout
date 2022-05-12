# ShinobiBout
A project that I am working on, I don't think it'll be much but it's just to experiment and learn Python better, just looking for advice on how i could've done better..

The main objective is that in the game you input your player name your element and your health, and you also select your enemies stuff in the same way

then each turn it's similar to rock paper scissors with the elements and the objective is to get one player's health to hit 0

the program ends when that goal is reached and through the terminal the print statements will show you your and your enemy's health along with which element they picked

It's just poorly made so i wanted some advice
///

those previous notes were from a while back I've changed the game up a bunch
so some of the actions particularly all of the ones except the elemental attacks work
so ignore the others for now I'm still working on them,
however i have run into an issue where it says gives an error after i choose my element in the file that goes like this

File "C:\Users\Jonca\PycharmProjects\ShinobiBout\main.py", line 84, in rps
    if actionTuple[choiceList[0]] == 'water' and actionTuple[choiceList[1]] == 'fire':
IndexError: list index out of range

i chose the element water which was the index of '0' which is what I entered into the input
however it came back with this and I'm confused because this worked before my recent changes so I'm a little confused on what I did wrong 
if anyone could help me that would be much appreciated.
