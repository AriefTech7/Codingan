#def chatbot():
#    user_input = input("You: ").lower()
#    if "hello" in user_input:
#        return "Hi there! How can I help you?"
#    elif "bye" in user_input:
#        return "Goodbye! Have a great day!"
#    else:
#        return "I'm not sure I understand."

#print(chatbot())

#from openai import OpenAI
#client = OpenAI()

#completion = client.chat.completions.create(
    #model="gpt-4o-mini",
    #messages=[
       # {"role": "system", "content": "You are a helpful assistant."},
      #  {
      #      "role": "user",
      #      "content": "Write a haiku about recursion in programming."
      #  }
    #]
#)

#print(completion.choices[0].message)

