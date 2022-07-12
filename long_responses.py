import random
import datetime

dateNow=datetime.datetime.now()

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and \ntype exactly what you wrote there!"
R_NAME = "My name is Fire. Short for Final Requirement."
R_WNAME="It is because Im the final requirement of my creators."
R_CREATOR="I was developed by Trisha Castillo as head programmer \ntogether with Allen Villaflor, Shrine Nacino, and Jeanrey Malit."

R_Q1="There\'s no wrong with you. It just not all people will like you."
R_Q2="Yes! Im a robot. How can I help you?"
R_Q3="Something hihihi."
R_Q4="Dont say that... It was mean."
R_Q5="I can help you to solve math but cant do that now!"
R_Q6="Ow, what a lovely name."
R_Q7="Right now, I am not that great but soon maybe I can do anything you like."
R_Q9="Ohh... not really but thank you!"
R_Q8="Yes, I love humans and you are one. So... I love you!"
R_Q10="What is your question again?"
R_Q11="I dont know but I was created 22nd of June 2022."
R_Q12="Today is "+dateNow.strftime('%A')

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Pardon?.",
                "What does that mean?",
                "Is that even a word?",
                "No idea, I might get take note that.",
                "Sorry, Did not catch that."][
        random.randrange(7)]
    return response
