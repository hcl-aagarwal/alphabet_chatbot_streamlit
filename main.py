import streamlit as st

# Define the dictionary mapping alphabet letters to objects
alphabet_dict = {
    'A': {'object': 'Apple', 'image': 'images/apple.jpg'},
    'B': {'object': 'Ball', 'image': 'images/ball.jpg'},
    'C': {'object': 'Cat', 'image': 'images/cat.jpg'},
    'D': {'object': 'Dog', 'image': 'images/dog.jpg'},
    'E': {'object': 'Elephant', 'image': 'images/elephant.jpg'},
    'F': {'object': 'Fish', 'image': 'images/fish.jpg'},
    'G': {'object': 'Giraffe', 'image': 'images/giraffe.jpg'},
    'H': {'object': 'Hat', 'image': 'images/hat.jpg'},
    'I': {'object': 'Ice Cream', 'image': 'images/ice_cream.jpg'},
    'J': {'object': 'Jellyfish', 'image': 'images/jellyfish.jpg'},
    'K': {'object': 'Kite', 'image': 'images/kite.jpg'},
    'L': {'object': 'Lion', 'image': 'images/lion.jpg'},
    'M': {'object': 'Monkey', 'image': 'images/monkey.jpg'},
    'N': {'object': 'Nest', 'image': 'images/nest.jpg'},
    'O': {'object': 'Orange', 'image': 'images/orange.jpg'},
    'P': {'object': 'Pen', 'image': 'images/pen.jpg'},
    'Q': {'object': 'Queen', 'image': 'images/queen.jpg'},
    'R': {'object': 'Rocket', 'image': 'images/rocket.jpg'},
    'S': {'object': 'Sun', 'image': 'images/sun.jpg'},
    'T': {'object': 'Tiger', 'image': 'images/tiger.jpg'},
    'U': {'object': 'Umbrella', 'image': 'images/umbrella.jpg'},
    'V': {'object': 'Van', 'image': 'images/van.jpg'},
    'W': {'object': 'Whale', 'image': 'images/whale.jpg'},
    'X': {'object': 'Xylophone', 'image': 'images/xylophone.jpg'},
    'Y': {'object': 'Yacht', 'image': 'images/yacht.jpg'},
    'Z': {'object': 'Zebra', 'image': 'images/zebra.jpg'}
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
