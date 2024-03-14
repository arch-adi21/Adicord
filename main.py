# Application ID : 1217727874287669258
# Public Key : c6899346817066e0a3d169d1203f8a792ce0b18754b5149960af5675bcbee5e1

import discord
import os
import openai

file = "1"
match(file):
  case "1":
    file = "chat1.txt"
  case "2":
    file = "chat2.txt"
  case "3": 
    file = "chat3.txt"
  case _:
    print("Invalid choice.")
    exit()

with open(file, "r") as f:
  chat = f.read() 

a = 1
openai.api_key = os.getenv("OPEN_AI_KEY")
token = os.getenv("BOT_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
          chat += f"{message.author}: {message.content}\n"
          print(f'Message from {message.author}: {message.content}')
          if self.user!= message.author:
              if self.user in message.mentions:
                response = openai.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                  messages=[
                    {
                      "role": "user",
                      "content": f"{chat}/nAdicord :"
                    }
                  ],
                  temperature=1,
                  max_tokens=900,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0.04
                )
                channel = message.channel
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)    
        except Exception as e:
          print(e)
          chat = ""



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
