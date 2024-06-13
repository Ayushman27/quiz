import sys
import io
from google.generativeai import GenerativeModel, configure

# Replace with your actual API key
API_KEY = "AIzaSyArrHNrkI59IsDS_GKnlFpsqQlj50FQMzo"

# Configure the API with your key
configure(api_key=API_KEY)

# Initialize the GenerativeModel object for Gemini Pro
model = GenerativeModel("gemini-pro")

def generate_response(user_input, chat):
    # Ensure user_input is a string before sending
    if not isinstance(user_input, str):
        user_input = str(user_input)  # Convert to string if necessary

    response = chat.send_message(user_input)
    return response.text  # Return the response from the chat

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No user input provided")
        sys.exit(1)

    try:
        user_input = sys.argv[1]
        chat = model.start_chat(history=[])  # Create chat object here
        bot_response = generate_response(user_input, chat)

        # Set encoding for standard output to UTF-8
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        print(bot_response)  # Print the response to be captured by Node.js
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)