"""Create your own adventure: Buzzfeed quiz."""
__author__ = "730550997"


# import
import random

# global variables:
points: int = 0
player: str = ""
# Use randint
stairs: int = random.randint(2, 20)

# named constants
HAPPY_EMOJI = "\U0001F60A"
SAD_EMOJI = "\U0001F622"


def greet() -> None:
    """Function that gives a welcome message plus takes name."""
    # Introduce game
    print("Welcome to my adventure game. \nThis adventure scenario will help you find out if you can survive a power outage in your sketchy apartment complex. All you need to do is follow the story line and choose the number based on the choice you wish to make. Enjoy...\t")

    # Get player name
    global player
    name = input("What is your name: ")
    player = name.capitalize()
    print("")


def endgame(ending_type: int) -> None:
    """Function that ends the game."""
    if ending_type == 1:
        print(f"\nThe game has finished {HAPPY_EMOJI} . \nYou were able to stay safe until the lights turned back on. You did well by earning {points} adventure points, but can you do better next time?")
    else:
        print(f"\nGame over {SAD_EMOJI} . \nYou were not able to survive the terrors of your apartment complex, and only earned {points} adventure points. Can you do better next time?")
    
    return ending_type


def path1() -> None:
    """Function that contains path if you try to fix the light."""
    # access global 
    global points
    points += 5
    choice = int(input("\nNone of the switches are working. Do you: 1-Go outside to get into the apartment building so you can turn on the generator?\n"\
        "2-Grab a flashlight and use that to finish up your work for the night.\t"))
    
    if choice == 1:
        points += 10
        print(f"\nYou run down {stairs} flights of stairs. As you make your way to the shady part of the building's parking lot, you see a shadowy figure whisper, {player}. What do you do?")
        choice2 = int(input("1-Walk towards them and ask if they need help.\n2-Run away and call the police. \n3-Freeze and drop your house keys in the grass.\t"))

        if choice2 == 1:
            points -= 10
            print(f"\nUh oh {player}. Looks like this shadowy figure was a criminal on the loose...You got caught witnessing something highly illegal, and the criminal couldn't "\
                "leave any loose ends.")
            endgame(2)

        elif choice2 == 2:
            points += 5
            print("\nAs you run away and almost face plant due to the slippery grass, you realize that your phone battery is dead. What do you do?")
            choice3 = int(input("1-Bang on the nearest door. \n2-Sit there and cry. \n3-Find the nearest branch to defend yourself.\t"))
            
            if choice3 == 1:
                points += 5
                print(f"\nThe neighbor opens the door and says in surprise, {player}? Turns out, you knocked on your ex-best friend's door. You try explaining "\
                    "what's happening but she doens't believe you because of your past as a pathalogical liar. She slams the door on your face. What do you do now?")
                choice4 = int(input("1-Stand there in confusion. \n2-Run back to your room as fast as you can.\t"))

                if choice4 == 1:
                    points -= 5
                    print(f"\nUh oh {player}. Looks like the shadowy figure caught up to you after you accidently caught him doing something highly illegal, and he couldn't leave any loose ends...")
                    endgame(2)
                else:
                    points += 5
                    print(f"\nYou are able to get into your room succesfully, and by the time your un up the {stairs} flights of stairs, the lights have come back on.")
                    endgame(1)

            elif choice3 == 2:
                points -= 5
                print(f"\nAs you sit there crying in the rain, the shadowy figure comes up behind you with an umbrella. You are about to scream when you hear him whisper, {player} are you ok? Turns out, the shadowy figure was a childhood best friend that had come to your apartment building to visit but didn't know what room you lived in so he got lost outside. What do you do next?")
                choice4 = int(input("1-Ask for help in turning on your generator. \n2-Take him back up to your apartment to get some dry clothes on. \n3-Tell him to call an uber because you are creeped out at his sudden appearence.\t"))
                
                if choice4 == 1:
                    points += 5
                    print("\nAs you guys make you way down to the basement, the lights magically turn on. Turns out, the breaker switched off and the landlord had come before you to fix it!")
                    endgame(1)
                elif choice4 == 2:
                    points -= 5
                    print("\nYou two carefully reach your apartment, where you immediately run to grab towels for the both of you. Suddenly you hear the door lock, and your 'friend' walks towards you with an object in your hand. What do you do?")
                    choice5 = int(input("1-Freeze out of fear. \n2-Scream as loudly as possible. \n3-Grab your nearest object (a physics textbook) and hope for the best.\t"))

                    if choice5 == 1:
                        points -= 5
                        print("\nUh oh. Your supposed best friend turned out to be a criminal on the loose and did not want to leave any loose ends...")
                        endgame(2)
                    elif choice5 == 2:
                        points += 5
                        print("\nYour next door neighbor, hearing the screams, tries to get into the apartment. Alas, the locked door gives your supposed best friend enough time to take you out, leaving your neighbor to be the next victim.")
                        endgame(2)
                    else:
                        points += 10
                        print("\nYour high school PE skills come in a clutch as you use enough strength to knock out the man. As you do this, the lights turn back on, and you quickly call the police using your landline.")
                        endgame(1)

                else:
                    points += 10
                    print("\nWhile you were saying this, your landlord, who just came out of the basement to fix the breaker that had turned off, comes up behind you. The 'best friend' turned out to be a criminal and you made the right call to send him away. Since your landlord is also there, the criminal can't hurt you, so he slowly runs away.")
                    endgame(1)
            
            else:
                points += 10
                print("\nYou do your best to fend off the attacker. However, once he comes near the dim streetlight you fell under, you see that it's your landlord. Turns out he had come down to fix the lights as well, but lost his keys somewhere in the grass because a loud sound jumpscared him. What do you do?")
                choice4 = int(input("1-Help him look for his keys. \n2-Say OK and then go back to your apartment because you barely know the guy.")) 

                if choice4 == 1:
                    points -= 5
                    print("\nAs the two of you search the wet grass for the keys to the basement, another shadowy figure emmerges from behind the bushes. This is the criminal that's been making national news because he ran away from a high security prison. You and your landlord are witnesses and now cannot escape...")
                    endgame(2)
                else:
                    points += 5
                    print(f"\nYou make it back to your apartment, wet, tired, and extremely confused. By the time you grab a piece of chocolate as a reward for running up and down {stairs} flights of stairs the lights turn back on. Guess he found the keys afterall.")
                    endgame(1)

        else:
            points -= 5
            print("\nAs you go onto your knees and dig through the muddy grass, the thundering turns into lighting. Bright flashes strike around you, and almost near you. What do you do?")
            choice3 = int(input("1-Run back to your apartment entrance. \n2-Keep looking for your keys.\n"))

            if choice3 == 1:
                points += 10
                print("\nYou make it inside just before the lighting strikes near the area you were just sitting in. But now you can't even get into your apartment. What do you do?")
                choice4 = int(input("1-Knock on the first door you see. \n2-Wait till the lightning stops to go for your keys again. \n"))

                if choice4 == 1:
                    points += 10
                    print("\nYou knocked on the door of an old friend whom you didn't know was living there. She lets you inside to wait out the storm, and a few minutes later, the lights are back on as well.")
                    endgame(1)
                else:
                    points += 5
                    print("\nAs you wait in the staircase area, the lights turn back on. However, you still can't get to your room. So, you try to find your friend's apartment to ask for help, and, a few hours later, the two of you finally find your key.")
                    endgame(1)
            
            else:
                points -= 10
                print("\nYou find out the hard way that lightning can strike the same spot twice. While it wasn't a direct hit, the lightning strike knocks you out, so your landlord, who was busy fixing the light, finds you laying outside an hour after the tragedy.")
                endgame(2)
    
    else: 
        points += 5
        print("\nYou find out that tragically, your flashlight is dead. And of course, you only have dead batteries in your junk drawer. What do you do?")
        choice2 = int(input("1-Attempt to drive to the nearest store to buy batteries...and ice cream. \n2-Ask your next door neighbor (also your ex) for some. \n3-Go to sleep. \t"))
        
        if choice2 == 1:
            points += 5
            print("\nYou find out your car has a flat tire because somehow, a branch got stuck in the back. What do you do?")
            choice3 = int(input("1-Sit there and cry because your tire is flat. \n2-Walk to the store because you have nothing else to do."))

            if choice3 == 1:
                points -= 10
                print("\nUh oh. A shadowy figure emergers near the driver's window. Turns out, this criminal that was actually on the run was trying to steal your car but the branch foiled his plans. He wanted to tie up all loose ends including you...")
                endgame(2)
            else:
                points -= 5
                print("\nAs you walk and get soaked, you realize that you left your keys in your car. What do you do?")
                choice4 = int(input("1-Try and shout for help. \n2-Break the car window cuz your tire is already flat. \t"))

                if choice4 == 1:
                    points -= 5
                    print("\nUh oh...your shouting attracted the attention of a criminal on the loose...")
                    endgame(2)
                else:
                    points += 10
                    print("\nUnfortunately, your insurance is going to spike due to your actions. However, you were able to get your keys back before the lights got back on.")
                    endgame(1)
       
        elif choice2 == 2:
            points += 5
            print("\nNo one answers the door. What do you do?")
            choice3 = int(input("1-Leave and go to sleep. \n2-Go to the next door.\t"))

            if choice3 == 1:
                points += 5
                print("\nLooks like you weren't able to fix the problem, but you also didn't get hurt.")
                endgame(1)
            else:
                points -= 10
                print("\nUh oh. Since you were banging on all the doors, someone called the police. Coincidentally, there have been reports of ding-dong-ditches turning violent, and now the police suspect you...")
                endgame(2)

        else:
            points += 5
            print("\nLooks like you weren't able to fix the problem, but you also didn't get hurt.")
            endgame(1)
        

def path2() -> None:
    """Function that contains path if you try to ignore the issue."""
    # access global 
    global points
    points += 5
    print("\nAs you sit down to meditate, you hear some weird noises on top of the rain outside. What do you do?")
    choice = int(input("1-Continue meditating. \n2-Go outside with a bat and your almost dead phone to investigate.\t"))
    
    if choice == 1:
        points += 5
        print("\nLooks like you weren't able to fix the problem, but you also didn't get hurt.")
        endgame(1)

    elif choice == 2:
        points += 10
        print("\nYou are now outside and, because you forgot an umbrella, are also soaked in the rain. As you try to find the source of the weird noise, a shadowy figure approaches you asking for help. What do you do?")
        choice2 = int(input("1-Go towards them to help. \n2-Slowly run away because that was insanely creepy. \n3-Throw the bat at them to scare them away.\t"))

        if choice2 == 1:
            points -= 10
            print("\nUh oh. This shadowy figure that was acting turned out to be a criminal on the loose, and was out for any victim he could find...")
            endgame(2)
        elif choice2 == 2:
            points += 5
            print("\nAs you run away, you slip on the grass and hurt your ankle. What do you do?")
            choice3 = int(input("1-Sit there and cry. \n2-Get up and try to run back to your apartment. \n3-Stay there but keep your bat on standby.\t"))
            
            if choice3 == 1:
                points -= 10
                print("\nUh oh. This shadowy figure that was acting turned out to be a criminal on the loose, and was out for any victim he could find. He finally caught up to you...")
                endgame(2)

            elif choice3 == 2: 
                points += 10
                print("\n Even though your ankle is completely destroyed, you made it back to your apartment safely. In that time, the landlord got the lights back on.")
                endgame(1)
            
            else:
                points += 15
                print("\nThe shadowy figure approaches you and tries to get to you, but you are able to defend yourself just enough to run away.")
                endgame(1)
        else:
            points -= 5
            print("\nThe shadowy figure doesn't appreciate this. He starts approaching you. What do you do?")
            choice3 = int(input(f"1-Bang on all the closest doors to ask for help. \n2-Freeze out of fear. \n3-Somehow sprint up the {stairs} flights of stairs due to your incredible cross country abilities.\t"))

            if choice3 == 1:
                points -= 5
                print("\nUh oh. Since you were banging on all the doors, someone called the police. Coincidentally, there have been reports of ding-dong-ditches turning violent, and now the police suspect you...")
                endgame(2)
            elif choice3 == 2:
                points -= 10
                print("\nUh oh. This shadowy figure that was acting turned out to be a criminal on the loose, and was out for any victim he could find. He finally caught up to you...")
                endgame(2)
            else:
                points += 10
                print("\nWhile your lungs are burning, yuou made it back to your apartment safely. In that time the landlord got the lights back on.")
                endgame(1)


def extra_points(current: int) -> int:
    """Bonus point function that is only added when the high score is increasde."""
    bonus = random.randint(1, 50)
    answer = random.randint(1, 10)

    print(f"{player}, since your current score exceeds the previous highest score, you can earn {bonus} bonus points if you can answer this question correctly.")
    guess = int(input("Choose a number from 1 to 10: "))
    if guess == answer:
        print("Correct!")
        global points
        points += bonus
    else:
        print(f"Incorrect...the answer was {answer}. Better luck next time!")

    return points


def main() -> None:
    """Main function that runs the loop."""
    user_choice = "Y"
    high_score = 0
    greet()
    while user_choice.upper() == "Y":
        # Enter experience with 3 choices:
        print("You are resting in your tiny yet pricey student apartment in the midst of a late-night thunderstorm. Suddenly, all the lights go out.")

        enter = int(input(f"{player}. How do you want to proceed: 1-Check all the switches and power outlets.\n2-Take this oppurtunity to meditate in the dark.\n3-Go to sleep because it's already 10 PM.\n"))  
        
        if enter == 1:
            path1()
        elif enter == 2:
            path2()
        else:
            print("Looks like you weren't able to fix the problem, but you also didn't get hurt.")
            endgame(1)
        
        if points > high_score:
            extra_points(points)
            high_score = points

        print(f"Your high score: {high_score}. \nYour current score: {points}.")
        user_choice = input("Would you like to play again? Y/N")


if __name__ == "__main__":
    main()