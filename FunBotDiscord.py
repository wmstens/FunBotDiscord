import discord
intents = discord.Intents.all()
f = open("botToken.txt", "r")
TOKEN = f.read()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print('i can see this')
    print(message.content)
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send(f'Hello, {message.author.display_name}!')

    if message.content == 'hey jared':
        await message.channel.send('that guy sucks dont talk to him!')


    if message.content == 'testing this new feature':
        await message.channel.send('PASSED YAHOO')

    if message.content == 'testing again':
        await message.channel.send('PASSED YAHOO 2')

    if message.content == 'testing again 3':
        await message.channel.send('PASSED YAHOO 3')

    if message.content == 'testing again 4':
        await message.channel.send('PASSED YAHOO 4')


client.run(TOKEN)