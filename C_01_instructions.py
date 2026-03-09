

        # print error if user does not enter something that is not valid
        print(error)
        print()


# Displays instructions

def instructions():
    print("""
    

**** Instructions ****

To begin, choose the number of rounds (or play infinite mode).


Then play against the computer. you need to P (paper) or S (scissors).

The rules are as follows: 
0 Paper beats rock 
0 Rock beat scissors 
0 Scissors beat paper

Good luck!
    """)


# Main routine
print()
print("🪨📄✂️ Rock / Paper / Scissors Game 🪨📄✂️")
print()


# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")

