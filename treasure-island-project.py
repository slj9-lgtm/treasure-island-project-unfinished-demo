print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("\nYou're at a crossroad."
                "\nLeft takes you east down a stone path and right takes you west into the woods."
                "\nType \"left\" or \"right\" ").lower()

if choice1 == "left":
    choice2 = input("\nYou walk along the stone path and arrive at a rushing river."
                    "\nThe bridge to get across is broken."
                    "\nYou can choose to risk it and swim to the other side, or walk upstream to find another way across."
                    "\nType \"swim\" or \"walk\" ").lower()
    if choice2 == "walk":
        choice3 = input("\nYou start marching upstream, looking for something - anything - that might lead you to the other side."
                        "\nAs you march on farther and farther, the rushing river widens and the current appears to weaken."
                        "\nA little further and you spot some long, dark shapes in the muddy water."
                        "\nYou gulp."
                        "\nYou'd heard rumours about alligators residing around these parts. You just hope they'll pay you no mind."
                        "\n \nAfter some time, you come across a very old fallen log lodged into the banks on either side of the river."
                        "\nYou gaze further up ahead and in an old oak tree is a man-made wooden platform with a zipline leading to another platform across the water."
                        "\nType \"log\" or \"zipline\" ").lower()
        if choice3 == "zipline":
            choice4 = input("\nYou walk over to the base of the tree and find steps nailed into the trunk spiralling upwards around it to the platform."
                            "\nYou start climbing up."
                            "\nOnce on the platform, you test your weight against the zipline contraption."
                            "\nIt holds you easily."
                            "\nYou grip onto the handholds provided, take a steadying breath, and push off the edge of the platform."
                            "\nThe wind rushes by your ears and you close your eyes, whispering a silent prayer."
                            "\n \nYou've all too soon come to a stop."
                            "\nYou blink your eyes open again and look down, finding yourself just above the other platform."
                            "\nYou've made it to safety!"
                            "\n \nAfter climbing down the other tree and continuing on your way, you spot the tall spires of a fortress in the distance."
                            "\nThe treasure you seek lies within its walls."
                            "\n \nAs you get closer, you must decide your next course of action."
                            "\nTrying to enter via the front gate is more straightforward, but heavily armed and guarded."
                            "\nYou cannot predict how the guards will receive you."
                            "\nOr you could search for the secret tunnel leading directly to the castle's catacombs."
                            "\nYou were tipped off as to its location."
                            "\nBut you've no idea what perils may await you below ground..."
                            "\nType \"gate\" or \"tunnel\" ").lower()
            if choice4 == "tunnel":
                choice5 = input("\nYou veer off the road leading to the gate and take the long way round."
                                "\nRecalling the coordinates you were given, you begin your search for the subterranean tunnels."
                                "\nFinally, on the edge of a small woodland area, you find a tree with a hidden enchantment on it."
                                "\nReciting the incantation provided with the coordinates, the magical illusion dissipates revealing a trap door embedded in the trunk."
                                "\nYou swing open the door only to be faced with a pitch black abyss."
                                "\nYou close it again and wander a little deeper between the trees, looking for materials."
                                "\n \nAfter acquiring a suitable branch, you tear the bottom of your shirt and soak it in sap leaking our of a nearby pine tree,"
                                "\nbefore wrapping the rag around the stick."
                                "\nTaking your flint out of one of your many inventory pockets, you set alight your homemade torch and make your way into the tunnel."
                                "\n \nA little while later, you're heading deeper and deeper underground and will soon reach the castle's catacombs."
                                "\nTaking another turn, you find two doors."
                                "\nOne is large, mahogany, almost reaching the ceiling of the tunnel, with ornate gold plated carvings spiralling beautifully upwards."
                                "\nThe other is much smaller, old, worn, and covered in moss, looking more like a broom closet."
                                "\n \nType \"big door\" or \"small door\" ").lower()
                if choice5 == "small door":
                    choice6 = input("").lower()

                elif choice5 == "big door":
                    print("")

                else:
                    print("\nError! You can't do that here.\n \nYou spontaneously combust and die.\n \nGame Over.")

            elif choice4 == "gate":
                print("\nYou continue down the road towards the gate, deciding for the more straightforward approach."
                      "\nA few hundred metres from the gate, you see that the guards have noticed you coming and are rushing to their stations."
                      "\nNow in front of the gate, two guards have come down to greet you - or so you thought."
                      "\nGlancing skywards at the top of the fortress walls, you can make out a dozen arrows pointed at you."
                      "\nYou freeze and stare back down at the two guards approaching you, but by now they've already got you surrounded."
                      "\n")

            else:
                print("\nError! You can't do that here.\n \nYou spontaneously combust and die.\n \nGame Over.")

        elif choice3 == "log":
            print("\nTurning back to the log, you step towards it."
                  "\nAs you get closer, though, you notice the distinct smell of decay."
                  "\nCautiously, you touch the waterlogged wood, praying that it won't crumble instantly."
                  "\nIt holds, barely. But you decide to risk it anyway."
                  "\nOnce you manage to fully climb onto the log, you begin to edge across, being careful not to slip on the moss."
                  "\n \nYou're almost at the halfway point, but halt abruptly after hearing a loud, heart wrenching \"CRACK\" beneath your feet."
                  "\nYou glance down and see pieces of rotten bark fall, disturbing the waters below."
                  "\nThe dark shapes in the water begin to stir, revealing themselves to indeed be alligators."
                  "\nAnd you've just woken them from their slumber."
                  "\nSoon, nearly a dozen of them congregate underneath the creaking log you're standing on."
                  "\n \nThrough gritted teeth, you let out a sharp breath and keep shuffling towards the other side."
                  "\nHowever, as you keep moving, you feel the log begin to bend under your weight."
                  "\nMore debris falls into the water, further agitating the hungry beasts."
                  "\nA couple of them leap up to angrily snap their maws at the air just inches from your feet."
                  "\nBut you keep going, determined to get to safety through any means necessary."
                  "\n \nIn your desperation, you start taking bolder strides."
                  "\nYou leap forward and land heavily onto the log."
                  "\nIt somehow still holds."
                  "\nYou stand but trip over a broken branch, your body hitting the log hard."
                  "\n \nYou hear a final creak travel throughout the decaying old tree trunk, before feeling completely weightless."
                  "\nPlummeting straight down into the many snapping jaws of your doom."
                  "\n \nAs you hit the water, every single alligator charges towards your sinking form."
                  "\nYet you resurface and still try to swim to safety."
                  "\nTo no avail."
                  "\nA set of razor sharp teeth sink into your right arm, then another into one of your legs."
                  "\nYour agonised screams are muffled by the rolling scaled bodies and the murky water."
                  "\n \nYou Died.\n \nGame Over.")

        else:
            print("\nError! You can't do that here.\n \nYou spontaneously combust and die. \nGame Over.")

    elif choice2 == "swim":
        print("\nYou shed your outer layers of clothing and footwear and approach the shore."
              "\nKneeling down, you test the water temperature with your hand."
              "\nIt is fresh but surprisingly pleasant."
              "\nYou ease yourself into the water, searching for the bottom with your feet so as not to get swept away by the currents."
              "\nThe water reaches your neck before your foot finds a slippery rock below you to stand on."
              "\nSo, you edge away from the shore and begin to make your way across."
              "\nBut as you go to take another step, something latches onto your ankle, causing you to miss the next rock and slip."
              "\n \nNow fully submerged in the merky water, the currents take you faster and faster away from your goal."
              "\nYou finally manage to breach the surface and take a gasping breath."
              "\nFrantically flailing your arms about to grab onto anything, you look in the direction the river is heading."
              "\nBut you don't see the horizon."
              "\nYour stomach drops."
              "\nUp ahead, a seemingly endless fall awaits you, and there is nothing you can do to escape."
              "\nYour fate is sealed."
              "\n \nYou can hear the ever approaching sound of crashing water onto jagged rocks, and let yourself slip below the surface once more."
              "\nWhen you reach the drop, you don't squirm or scream or struggle.\nYou simply close your eyes, awaiting your end."
              "\n \nYou Died.\n \nGame Over.")

    else:
        print("\nError! You can't do that here.\n \nYou spontaneously combust and die.\n \nGame Over.")

elif choice1 == "right":
    print("\nYou start strolling down the woodland path."
          "\nThe woods grow thicker the deeper you go."
          "\nThe foliage overhead grows so thick that daylight no longer shines through to the earth below."
          "\nThe trees and other plant life begin to reach various stages of decay as you continue on the increasingly treacherous path."
          "\n \nA strong sense of foreboding overcomes you. But despite everything, you force yourself onwards."
          "\n \nThe acrid smell of decaying plants is steadily overtaken by the nauseating stench of rotting flesh."
          "\nThis smell mixed with the taste of the stale air burns your throat."
          "\n \nYou cough."
          "\nYou keep coughing."
          "\nYou can't stop."
          "\nYour eyes begin to water, your breath comes out in shallow wheezes between coughing fits, and your whole body starts to tremble with a dull aching pain."
          "\nThrough a blurry, tear-filled gaze, you look back the way you came searching for a way out."
          "\nBut it's too late now. You've come too far to turn back."
          "\n \nThe hot and humid air suddenly turns icy."
          "\nYou stop walking."
          "\nYou feel a cool breeze on the back of your neck making you shiver."
          "\n \nSilence."
          "\n \nYour coughing stops, and now all you can hear are your own ragged breaths and the beat of your heart thundering in your chest."
          "\n \nYou turn, slowly."
          "\nNothing."
          "\nAnd then, you feel it again. The cool breeze on your neck."
          "\nYour hands shake and your teeth chatter."
          "\nYou turn back around to find nothing."
          "\nThe breeze is by you ear this time but before you can react there is a sudden striking pain in your stomach."
          "\nLooking down you see a giant claw-like object the size of your arm protruding from your abdomen. Your ripped clothes stained by your own hot blood."
          "\nYou open your mouth to scream, but the claw moves upwards too fast, slicing you clean in half."
          "\n \nYou Died.\n \nGame Over.")

else:
    print("\nError! You can't do that here.\n \nYou spontaneously combust and die.\n \nGame Over.")

