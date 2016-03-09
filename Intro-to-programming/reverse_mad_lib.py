#Reverse Mad_Lib generator made of Ender's Game Theme.


easy = """ "In the moment when I truly understand my enemy,
understand him well enough to defeat him,
then in that very moment I also love him.
I think it's impossible to really understand somebody,
what they want, what they believe,
and not love them the way they love themselves.
And then, in that very moment when I love them.... I destroy them."""

medium = """ "I am your enemy, the first one you've ever had who was smarter than you.
There is no teacher but the enemy.
No one but the enemy will tell you what the enemy is going to do.
Only the enemy shows you where you are weak.
Only the enemy tells you where he is strong.
And the rules of the game are what you can do to him
and what you can stop him from doing to you.
I am your enemy from now on. From now on I am your teacher." """


hard = """ "Let me tell you about gods," said Wiggin. "
No matter how smart or strong you are,
there's always somebody smarter or stronger,
and when you run into somebody who's stronger
and smarter than anybody, you think,
This is a god. This is perfection.
But I can promise you that there's somebody else somewhere else
who'll make your god look like a maggot by comparison.
And somebody smarter or stronger or better in some way.
So let me tell you what I think about gods.
A real god already has control of everything that needs controlling.
Real gods would want to teach you how to be just like them." """

blanks = [['moment', 'love', 'destroy'], ['enemy', 'teacher', 'smarter'], ['god', 'smarter', 'somebody']]

# Asks the user to choose what level of difficulty he/she wants to play in.    
def choose_level():
    print "The reverse_mad_lib game invites you to play a round.\n"
    level = raw_input("Please choose a level. Type easy/medium/hard to select a level.\n")
    intro_game(level)

# This function converts easy,medium or hard strings to an appropriate blank filled string.

def create_blank(paragraph):
    if(paragraph == easy):
        index_of_blank =0
    elif(paragraph == medium):
        index_of_blank = 1
    else:
        index_of_blank = 2
    for word in blanks[index_of_blank]:
        if word in paragraph:
           paragraph = paragraph.replace(word, str(blanks[index_of_blank].index(word)+1))
    return paragraph,index_of_blank
# This function calls the main_game function with the appropriate paragraph and difficulty level.

def intro_game(level):
    if(level == "easy"):
        paragraph, index_of_blank = create_blank(easy)
    elif(level == "medium"):
        paragraph , index_of_blank = create_blank(medium)
    elif(level == "hard"):
        paragraph, index_of_blank  = create_blank(hard)
    else:
        print "Please choose a level"
    print paragraph
    main_game(paragraph,index_of_blank)

# This function is the main_game.

def main_game(paragraph,index_of_blank):
    count = 0
    print "The round begins!"
    while(count<3):
        input = raw_input("Please enter a guess for blank " + str(count+1)+"\n")
        if(input == blanks[index_of_blank][count]):
                          paragraph = paragraph.replace(str(count+1),input)
                          count = count + 1
                          print "Your guess was correct!"
                          print paragraph
        else:
            print "Please guess again"
    print "The level is over!You won!"
    progress_game(index_of_blank)


# This function asks if the user wants to go to the next level or quit.

def progress_game(index_of_blank):
    if(index_of_blank == 2):
        print "The game is over!You have finished"
    else:
        option = raw_input("Do you want to progress to the next level? Y/N\n")
        if(option == "N"):
            print "You've quit at level " + str(index_of_blank+1)
        else:
            go_to_next_level(index_of_blank)

# If the user wants to go to the next level this function handles the progress.

def go_to_next_level(index_of_blank):
    if(index_of_blank == 0):
        paragraph, index_of_blank = create_blank(medium)
    elif (index_of_blank == 1):
        paragraph,index_of_blank = create_blank(hard)
    print paragraph
    main_game(paragraph,index_of_blank)

   
def main():
    choose_level()

main()
