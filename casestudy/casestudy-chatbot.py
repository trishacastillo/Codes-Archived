from tkinter import *
import re 
import long_responses as long #here store the other responses of bot


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Good Day!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('Okay.', ['nothing', 'business', 'not', 'dont', 'care'], single_response=True)
    response('Nice chatting with you. Goodbye!', ['stop','bye', 'goodbye'], single_response=True)
    response('Good for you', ['not bad','fine','great', 'nice', 'good', 'im', 'better'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks', 'you'], single_response=True)
    response('Thank you!', ['you', 'are', 'nice'], required_words=['nice'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_NAME, ['do','you', 'have', 'name','what'], required_words=['name'])
    response(long.R_WNAME, ['why','you', 'called', 'name','fire'], required_words=['why'])
    response(long.R_CREATOR, ['who','is', 'your', 'creator','developer','boss'], required_words=['who'])
    
    response(long.R_Q1, ['me','with', 'wrong', 'is','what'], required_words=['what'])
    response(long.R_Q2, ['are','you', 'a', 'robot'], required_words=['robot'])
    response(long.R_Q3, ['tell','me', 'something', 'said','say'], required_words=['something'])
    response(long.R_Q4, ['sucks','stupid', 'you', 'idiot'],  single_response=True)
    response(long.R_Q5, ['can','you', 'help', 'me','what'], required_words=['help'])
    response(long.R_Q6, ['my','name', 'is', 'im','call','me'], required_words=['name' or 'call'])
    response(long.R_Q7, ['can','you', 'do', 'capabilities','have','limitation'], required_words=['what'])
    response(long.R_Q8, ['do','you', 'love', 'me','humans','people'], single_response=True)
    response(long.R_Q9, ['you','smart', 'are', 'intelligent','helpful'], single_response=True)
    response(long.R_Q10, ['i','want', 'answer', 'now','me'], single_response=True)
    response(long.R_Q11, ['how','old', 'are', 'you'], required_words=['old'])
    response(long.R_Q12, ['day','today','what'], required_words=['what'])
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# GUI-----------------------------------------------------------------------
root = Tk()
root.title("Chatbot")

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function---------------------------------------------------------------
def send():
	user = "You: " + e.get()
	txt.insert(END, "\n" + user)
	txt.insert(END, "\n" + 'Bot: ' + get_response(user))
	e.delete(0, END)


lable1 = Label(root, bg="#3a7599", fg="#EAECEE", text="Simple Chatbot", font=FONT_BOLD, width=40, height=2).grid(
	row=0)

txt = Text(root, bg="#4f899b", fg="#EAECEE", font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg="#EAECEE", font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg="#ABB2B9",
			command=send).grid(row=2, column=1)

root.mainloop()
