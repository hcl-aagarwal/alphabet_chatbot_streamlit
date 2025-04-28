import streamlit as st

# Define the dictionary mapping alphabet letters to objects
alphabet_dict = {
    'A': 'Apple',
    'B': 'Ball',
    'C': 'Cat',
    'D': 'Dog',
    'E': 'Elephant',
    'F': 'Fish',
    'G': 'Giraffe',
    'H': 'Hat',
    'I': 'Ice Cream',
    'J': 'Jellyfish',
    'K': 'Kite',
    'L': 'Lion',
    'M': 'Monkey',
    'N': 'Nest',
    'O': 'Orange',
    'P': 'Pen',
    'Q': 'Queen',
    'R': 'Rocket',
    'S': 'Sun',
    'T': 'Tiger',
    'U': 'Umbrella',
    'V': 'Van',
    'W': 'Whale',
    'X': 'Xylophone',
    'Y': 'Yacht',
    'Z': 'Zebra'
}

# Function to get alphabet object
def get_alphabet_object(letter):
    letter = letter.upper()  # Ensure the letter is uppercase
    if letter in alphabet_dict:
        return f"{letter} - {alphabet_dict[letter]}"
    else:
        return "Sorry, I don't recognize that letter. Please enter a valid letter."

# Streamlit UI components
def main():
    st.title("Alphabet Chatbot")

    st.write("""
    Enter a letter from A to Z, and I'll tell you an object that starts with that letter.
    """)

    # Create a text input field for the user to enter a letter
    letter = st.text_input("Enter an Alphabet Letter (A-Z):", "")

    # If the user enters a letter, respond with the corresponding object
    if letter:
        response = get_alphabet_object(letter)
        st.write(response)

    # Add a button to reset the input field (optional)
    if st.button("Clear"):
        st.text_input("Enter an Alphabet Letter (A-Z):", value="")

if __name__ == "__main__":
    main()

