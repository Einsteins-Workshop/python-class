from flask import Flask, render_template, request, jsonify, session

# Adapted from https://github.com/VRohit1901/ChatBot-Flask/
#
# This project gives the chassis for a chat bot experience.  It firsts asks for a name to
# and assumes that each name represents a distinct user.
#
# One suggestion is to create a chatbot that, when it sees a new message from the user, asks
# for a response, and otherwise repeats the user. Here are the possible steps:
#
# 1. For each user, create a file that represents the JSON string of a dictionary, where the
# key is the user message and the value is the desired response.  The dictionary will start
# empty, and the file name should be based on the user.
#
# 2. With each message, load the file into a dictionary and check to see if the message is a key
# in it.
#
#    2a. If so, respond with the message
#
#    2b. If not, ask the user for the desired response. Save the response to the dictionary and
#        save it to the file.
#
# As a further elaboration, if the message is not defined by the user but is defined by the majority
# of other users, use that response instead.
#
# As a further bonus, there can be a small percentage for messages with a response where the
# chatbot asks for confirmation that the response is correct.
#
# To run this webserver, you can run the following command line:
# python -m flask —app chat run.

app = Flask(__name__)

app.secret_key = "xyzzy"
ASKING = 1
GET_ANSWER = 2
# A way of getting local files
# for file in os.listdir('C:/Users/Anonymous/Desktop/ChatBot-Flask/data/'):
#    chats = open('C:/Users/Anonymous/Desktop/ChatBot-Flask/data/' + file, 'r').readlines()


@app.route("/")
def hello():
    return render_template('chat.html')


@app.route("/clear", methods=['POST'])
def clear():
    session.clear()
    print("Clearing session cookies")
    return jsonify({'status': 'OK'})


@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    if "name" in session:
        if session["state"] == ASKING:
            if message == 'Hi':
                bot_response = "Welcome to my lair"
            else:
                bot_response = "I haven't heard that before, how should I respond to that?"
                session["state"] = GET_ANSWER
        elif session["state"] == GET_ANSWER:
            bot_response = "I will totally not remember that."
            session["state"] = ASKING
        else:
            bot_response = f"MAJOR MALFUNCTION, UNKNOWN STATE {session['state']}"
    else:
        session["name"] = message
        bot_response = f"Hi {session['name']}, I am listening"
        session["state"] = ASKING
    print(bot_response)
    return jsonify({'status': 'OK', 'answer': bot_response})


if __name__ == "__main__":
    app.run()