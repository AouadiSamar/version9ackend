import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

print("Chatbot: Hello! I'm your intelligent chatbot. You can start chatting with me.")
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user says goodbye
    if any(farewell in user_input.lower() for farewell in ["goodbye", "bye", "see you"]):
        print("Chatbot: Goodbye! Have a great day.")
        break

    # Use GPT-3 for generating responses
    response = openai.Completion.create(
        engine="text-davinci-002",  # You may need to check for the latest available engine
        prompt=user_input,
        max_tokens=150,
        temperature=0.7
    )

    chatbot_response = response['choices'][0]['text'].strip()
    print("Chatbot:", chatbot_response)
