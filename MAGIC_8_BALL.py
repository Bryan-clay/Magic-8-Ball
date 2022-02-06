#magic 8 ball

#global play_again
play_again = 'yes'
import letter_counter

#record possiblke answers
answers = ["It is certain", "It is decidedly so", "Without a doubt",
           "Yes definitely", "You may rely on it", "As i see it, yes",
           "Most likely", "Outlook good", "Yes", "Signs point to yes",
           "Reply hazy, try again", "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again", "Don't count on it",
           "My reply is 'no'", "My sources say 'no'", "Outlook not so good", "Very doubtful"]

#create a prompt to ask a question
question = input("What is your question? ")
def magic_8_ball(question):
    '''a function that asks the magic 8 ball question and provides an answer'''
    #question = input("What is your question? ")
    prediction = letter_counter.choice(answers)
    if question == '':
        print('Please ask a question.')
        magic_8_ball()
    else:
        print(f"\n{prediction}")

#make a way to either loop the program or quit
def keep_playing():
    '''a function to keep playing to game or quit'''
    global play_again
    next_question = input("\nWould you like to ask another question? ")
    if next_question == 'yes'.lower():
        magic_8_ball()
    if next_question == 'no'.lower():
        play_again = 'no'
        print("Thank you for playing.")
    else:
        print("Please answer 'yes' or 'no'.")


while play_again.lower() == 'yes':
    magic_8_ball(question)
    keep_playing()


