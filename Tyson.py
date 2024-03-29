#!/usr/bin/env python3

def contains(message, commands):
    for command in commands:
        if command in message.content.lower():
            return True

def equals(message, commands):
    for command in commands:
        if command == message.content:
            return True

def command(message, command):
    if message.content.lower().startswith('$' + command) \
    or message.content.lower().startswith('tyson '+ command):
        return True



import discord
import random
import socket
import asyncio
import os.path
import pickle

from quietyear import Game


if os.path.exists('save.p'):
    game = pickle.load(open("save.p", "rb"))
else:
    game = Game()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'general':
            await client.send_message(channel, 'Bork! Bork! I think {} is a burglar. Bork!'.format(member.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if command(message, "book"):
        await message.channel.send('The current story is "The Doctor\'s Case" by Stephen King.')

    if command(message, "bite"):
        await message.channel.send('*Aims for your jugular but misses. He is very smol.*')

    if command(message, "sit"):
        await message.channel.send('*Tyson sits on the couch. But not because you told him to.*')

    if command(message, "stay"):
        await message.channel.send('*Tyson looks up at you and resumes napping.*')

    if command(message, "come"):
        await message.channel.send('*Tyson ignores you.*')

    if message.content.startswith('$bark'):
        output = ''
        for i in range(len(message.content.split(' '))):
            output += 'Bork! '
        await message.channel.send(output)

    if message.content.startswith('$yip'):
        output = ''
        for i in range(len(message.content.split(' '))):
            output += 'Yap! '
        await message.channel.send(output)
    
    if message.content.startswith('!'):
        await game.send(message)
        pickle.dump(game, open("save.p","wb"))

    if message.content.startswith('$roll'):
        words = message.content.split(' ')
        if len(words) > 1 and 'd' in words[1]:
            words2 = words[1].split('d')
            if words2[0].isdigit() and words2[1].isdigit():
                dice = min(int(words2[0]), 20)
                size = min(int(words2[1]), 1000)
                output = '('
                for i in range(dice):
                    output += str(random.randint(1, size))
                    if i < dice-1:
                        output += ', '
                output += ')'
                await message.channel.send(output)
            else:
                await message.channel.send('Invalid input! Bork.')

        else:
            await message.channel.send('Invalid input! Bork.')

    if contains(message, ['chicken', 'nugget']):
        await message.channel.send('Tyson Chicken Nugget!')

    if contains(message, ['good boy', 'good dog', 'good try tyson']):
        await message.channel.send('<:happytyson:601457297302093844>')

    if 'blep' in message.content.lower():
        await message.add_reaction('<:happytyson:601457297302093844>')

    if 'tyson' in message.content.lower():
        await message.add_reaction('<:happytyson:601457297302093844>')

    if contains(message, ['fuck', 'shit', 'dumb idiot']):
        await message.add_reaction('<:angrytyson:593509277705044181>')
        await message.channel.send('*grrrrrr*')

    if message.content == "STOP":
        await message.channel.send('<:angrytyson:593509277705044181>')




client.run(open("apikey.txt",'r').read().strip())
