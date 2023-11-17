import re
import random
import streamlit as st
from phrases import responses

# match user input with fitting response pattern from responses list
def check(user_input, previous_response):
    for rule, response in responses:
        match = re.match(rule.lower(), user_input.rstrip(".!").lower())
        if match:
            # Choose a new response different from the previous one
            new_response = random.choice(response).format(*match.groups())
            while new_response == previous_response:
                new_response = random.choice(response).format(*match.groups())

            return new_response

    return "Es tut mir leid, ich verstehe dich nicht."

# main function to ask for user input and give converted answers
def psychotherapy():
    # streamlit title
    st.title("ANJA: Deine persönliche Therapeutin")

    # initial greeting from ANJA
    initial_greeting = st.chat_message("assistant")
    initial_greeting.write("Guten Tag! Ich bin ANJA, deine persönliche Therapeutin. Wie kann ich dir heute helfen?")

    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    goodbyes = ['tschüss', 'auf wiedersehen', 'bis später', 'ade', 'bis zum nächsten Mal', 'tschau']

    user_input = st.chat_input("Erzähle ANJA wie es dir geht!")
    if user_input is not None:
        with st.chat_message("user"):
            st.markdown(user_input)

        # add message to history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Check if user input matches any goodbye phrase
        if user_input.lower() in goodbyes:
            st.session_state.messages.append(
                {"role": "assistant", "content": "Auf Wiedersehen! Hab einen schönen Tag :)"})
            with st.chat_message("assistant"):
                st.markdown("Auf Wiedersehen! Hab einen schönen Tag :)")
                st.stop()
        else:
            # make sure one response is not used twice in a row
            previous_response = st.session_state.messages[-1]["content"] if st.session_state.messages else None
            # create ANJAs response from check function
            response = check(user_input, previous_response)

        if response is not None:
            with st.chat_message("assistant"):
                st.markdown(response)

            # add ANJAs messages to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    psychotherapy()