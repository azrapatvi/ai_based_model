from boltiotai import openai #type:ignore
from apikey import OPENAI_API_KEY #with this we can able to acess the api_key.py file and in that there is a variable which stores the api keyy which we can use it here

openai.api_key =OPENAI_API_KEY  

count=1
question=input(f"Q.{count} what is your question?")

while True:
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
     messages=[{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": question
    }])

    # 🖨️ Print only the final message from the assistant
    print(response['choices'][0]['message']['content'])
    count+=1

    question=input(f"Q.{count} what is your next question? or you wants to quit?press 'q' for quiting")

    if question=='q':
        break

