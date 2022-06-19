This is ShinobiBout, a text terminal fighting game,
the objective is to get the enemy's health to hit 0 

current version, alpha version 0.7.1 

//
READERS GUIDE:
 
    not started: self explanatory
    
    started: just started working on it and no estimate on finish
    
    near completion: started with estimate on finished update
    
    complete: finished product with insights

//
BUGS:

    none currently known as of version alpha 0.7.1

//
TODO:

    make Orochimaru vs 3rd Hokage battle in it's entirety possible(started)

    add transformation(not started)

    add weapon system(not started)

//
SYSTEMS

    this tab will explain how the program works and some of it's funcionality for confused readers
    
    //FLOWCHART
        Battlefield creation(math expression at the top of the main file)

                        |
                        v

        Character creation(automatic/dynamic class generation via setplayers method)

                        |
                        v

        Game loop starts(while running)

                        |
                        v

        Game over/Character death(checks if player health <= 0 via class attribute)

                        |
                        v

        Turn system(for loop iterating through a list with all of the class instances of Shinobi/Summon in it)

                        |
                        v

        Series of checks(checks if player chose a special action, checks how much chakra to remove from player, etc)

                        |
                        v

        Turn execution(loops through playerList again and checks the battlefield for their target and figuring out who won the round)

                        |
                        v        
        
        Top of the game loop(resets loop)
        
    //AUTO DYNAMIC CLASS GENERATION
        using input statements I can assign values to a globals() string variable and then append it to a list
        and in doing so I can loop through said list to go through the class instances made in the program without having
        to find a special name or anything similar.

    //WORKSHOP FILE
        This file is just for me to mess around with ideas for the game without messing stuff up permanently but I leave it in the
        repo so others can see the changes I'm working on.