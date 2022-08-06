import random
import re
import os
import discord
import dotenv 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

def process_figure_post(line_split):
        figure_game_url = line_split[0]
        figure_num = line_split[1]
        figure_trys = line_split[2]
        figure_time = line_split[3]

        # figure_num_pattern = "Figure #(.*)"
        # mo = re.search(figure_num_pattern,figure_num)
        # figure_number = mo.group(1)
        figure_number = [int(s) for s in figure_num.split() if s.isdigit()]
        number_of_tries = [int(s) for s in figure_trys .split() if s.isdigit()]
        # for s in figure_trys.split():
        #     if s.isdigit():
        #         number_of_tries = s

        figure_times = [int(s) for s in figure_time.split() if s.isdigit()]
        figure_minutes = figure_times[0]
        figure_seconds = figure_times[1]
        return figure_number, number_of_tries, figure_minutes, figure_seconds

def figure_say_good_job(username, figure_number, number_of_tries, figure_minutes, figure_seconds):
    response = (f'Great Job {username}!\n'
    f'You did the {figure_number}th figure in {number_of_tries} trys.\n'
    f'It only took you {figure_minutes} minutes and {figure_seconds} seconds!!!\n'
    f'Super proud of you bud.')
    return response      

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel_name = str(message.channel.name)
    line_split = user_message.split("\n")
    print(f'{username}: {user_message} {channel_name}')

    # Handle when a user submits their figure scores
    if 'https://figure.game' in line_split[0]:
        figure_number, number_of_tries, figure_minutes, figure_seconds = process_figure_post(line_split)
        response = figure_say_good_job(username, figure_number, number_of_tries, figure_minutes, figure_seconds)
        await message.channel.send(response)
        return

    if message.author == client.user:
        print(f'client user')
        return

    if user_message.lower() == 'hello' or user_message.lower() == 'hi':
        await message.channel.send(f'Hello {username}!')
        return
    elif user_message.lower() == 'bye':
        await message.channel.send(f'See you later {username}!')
        return
    elif user_message.lower() == '!random':
        response = f'This is your random number {random.randrange(420000)}'
        await message.channel.send(response)
        return
    elif user_message == '<:fullsalute:1005165220215398520>':
        response = f'I salute you {username} <:fullsalute:1005165220215398520>'
        await message.channel.send(response)
        return
    elif user_message == '<:fullsalute:1005149563809710241>':
        response = f'I salute you {username} <:fullsalute:1005149563809710241>'
        await message.channel.send(response)
        return

client.run(TOKEN)