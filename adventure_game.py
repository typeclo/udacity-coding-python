import time
import math
import random

dangers = ["bear", "tiger", "snake", "fox",
           "boar", "lion", "Python", "Gruffalo"]

chap = {
    "home": ("Should I 'bring my bag' or 'leave it'? ",
             "bring my bag", "leave it"),
    "no_bag_fork": ("Yeah, I don't need a bag anyway."
                    " Which road should I take, the 'adventurous'"
                    " road or the 'easy' road?", "adventurous", "easy"),
    "fork_road": ("Better safe than sorry. Which road should I take,"
                  " the 'adventurous' road or the 'easy' road?",
                  "easy", "adventurous"),
    "dangerous_road": ("Oh no there's a " + random.choice(dangers) +
                       ", I won't make it today", None, None),
    "no_bag_bushes": ("I feel so adventurous! Wait."
                      " what's that? I hear a sound in the bushes, "
                      "I wonder if I should 'check' or 'keep walking'?",
                      "keep walking", "check"),
    "bushes": ("Grandpa always said this was the best way to go."
               " What's that? I hear a sound in the bushes,"
               " I wonder if I should 'check' or 'keep walking'?",
               "check", "keep walking"),
    "danger": ("Oh no, it's a " + random.choice(dangers) + "! " +
               "I better hurry back home! I'll try again tomorrow.",
               None, None),
    "no_bag_cave_ent": ("Looks like I found a big cave!"
                        " Too bad I didn't bring my flashlight."
                        " I left it in my bag! I guess I'll just go home.",
                        None, None),
    "cave_ent": ("Looks like I found a big cave!"
                 " Good thing I have a flashlight in my bag."
                 " Should I 'go in' or 'explore outside'?", "go in",
                 "explore outside"),
    "cave": ("This cave is so scary. Should I 'explore'"
             " or 'go back outside'?", 'explore', "go back outside"),
    "deep_cave": ("Wow, this cave is beautiful!"
                  " Too bad I couldn't find that treasure. "
                  "It's getting late, I'll just head back home.", None, None),
    "outside_cave": ("Wow, I'm exhausted."
                     " That tree by the cave entrance"
                     " looks like a good place to rest,"
                     " should I take a 'rest' or 'keep exploring'?",
                     "rest", "keep exploring"),
    "lonely_tree": ("I guess I'll just sit under this tree to rest. "
                    "Wait what's that sign on the ground. Should I 'dig' "
                    "or 'explore some more'?", "explore some more", "dig"),
    "getting_dark": ("Oh no, now it's dark."
                     " I'll have to look for that treasure again tomorrow.",
                     None, None),
    "treasure_pos": ("I can't believe it. I found the treasure!", None, None)
}

is_treasure_found = False

chap_n = [chap["home"],
          chap["fork_road"],
          chap["bushes"],
          chap["danger"],
          None,
          chap["no_bag_fork"],
          chap["dangerous_road"],
          chap["cave_ent"],
          chap["cave"],
          chap["deep_cave"],
          chap["no_bag_bushes"],
          chap["no_bag_cave_ent"],
          chap["outside_cave"],
          chap["lonely_tree"],
          chap["getting_dark"],
          chap["danger"],
          None,
          chap["getting_dark"],
          chap["treasure_pos"],
          None]

# Grid of positions, each position has a text and two options.
# Options can be text or None.
map = [[chap_n[0],  chap_n[1],  chap_n[2],  chap_n[3], chap_n[4]],
       [chap_n[5],  chap_n[6],  chap_n[7], chap_n[8],  chap_n[9]],
       [chap_n[10], chap_n[11], chap_n[12], chap_n[13], chap_n[14]],
       [chap_n[15], chap_n[16], chap_n[17], chap_n[18], chap_n[19]]]
current_position = (0, 0)
treasure_position = (3, 3)


# Prints, then waits 2 seconds.
def print_dialog(dialog):
    split_dialog = dialog.split(". ")
    for sentence in split_dialog:
        time.sleep(1.5)
        print(sentence + ("." if sentence != split_dialog[-1] else ""))
        time.sleep(1.5)


# Returns state tuple at current_position.
def get_current_state_from_position():
    coordinate_x = current_position[0]
    coordinate_y = current_position[1]
    return map[coordinate_x][coordinate_y]


# Prompts user with the state in map at current_position and
# returns the next position based on user's input.
def get_next_position(current_state):
    while True:
        print_dialog(current_state[0])
        action = input("(type either '" + current_state[1] +
                       "' or '" + current_state[2] + "')\n\n")
        if action == current_state[1]:
            print("\n")
            return (current_position[0], current_position[1] + 1)
        elif action == current_state[2]:
            print("\n")
            return (current_position[0] + 1, current_position[1])
        else:
            print_dialog("Huh. What was I doing again. Ah right.")


# Main game
def start_game():
    global is_treasure_found
    global current_position

    # Opening scene
    print_dialog("My grandpa told me that he hid some " +
                 "treasures in the forest nearby. " +
                 "Today, I'm going to look for that treasure.")

    # loops over map using get_next_position, until is_treasure_found is True.
    while not is_treasure_found:
        current_state = get_current_state_from_position()

        has_player_lost = current_state[1] is None and current_state[2] is None
        if has_player_lost:
            print_dialog(current_state[0])
            break

        current_position = get_next_position(current_state)

        # Check if current_position equals treasure_position.
        if current_position == treasure_position:
            current_state = get_current_state_from_position()
            is_treasure_found = True
            print_dialog(current_state[0])
            break

    # End scene: Player won.
    if is_treasure_found:
        print_dialog("YOU WIN!")
    # End scene: Player lost.
    else:
        print_dialog("YOU LOSE, GAME OVER!")


print("\n" +
      "             *###################################*\n" +
      "             |#              <=~=>              #|\n" +
      "             |#   THE GREAT FOREST ADVENTURE:   #|\n" +
      "             |#          SEARCHING FOR          #|\n" +
      "             |#   *~| THE HIDDEN TREASURE |~*   #|\n" +
      "             |#            <=~~@~~=>            #|\n" +
      "             *###################################*\n")

# Starts the initial game.
start_game()

while True:
    play_again = input("Would you like to play again? (type 'yes' or 'no')\n")
    if play_again == "yes":
        is_treasure_found = False
        current_position = (0, 0)
        print("\n\n")
        start_game()
        continue
    elif play_again == "no":
        print("Okay. See you next time!")
        break
    else:
        print("Sorry, I couldn't understand?")
