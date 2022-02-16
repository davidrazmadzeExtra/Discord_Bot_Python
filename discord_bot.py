import discord
import random

# 🚨 THIS TOKEN ID SHOULD BE KEPT IN A SECRET FILE 🚨 
# Do not publish it anywhere
API_TOKEN = "DISCORD PORTAL -> SELECTED_APP -> BOT -> TOKEN -> COPY & PASTE HERE"
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # Get username, message, and channel
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # ❌ Make sure bot doesn't respond to itself
    if message.author == client.user:
        return

    # 🗣 Responds to messages in 'general'
    if channel == 'general':
        if user_message == 'hi':
            response = f'Hello {username}'
            await message.channel.send(response)
            return
        elif user_message == 'bye':
            response = f'Have a nice day, {username}!'
            await message.channel.send(response)
            return
        elif user_message == 'ass':
            response = f'No swearing in here! {username}!'
            await message.channel.send(response)
            return

    # 🗣 Responds to messages in 'giveaway'
    if channel == 'giveaway':
        if user_message == '!random':
            random_number = random.randrange(100000)
            response = f'Random number: {random_number}'
            await message.channel.send(response)
            return

client.run(API_TOKEN)