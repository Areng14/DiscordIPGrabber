import discord
import os
from os import system
from API import blacklistedID
from discord_webhook import DiscordWebhook, DiscordEmbed


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&invalid'):
        vmessagei = message.content
        vmessagei = vmessagei.replace("&invalid ", "")
        vmessagei = vmessagei.replace(" ", "")
        blacklistedID[vmessagei] = "1"
        openfile = open("data.json", "w")
        openfile.write(str(blacklistedID))
        openfile.close()
        webhook = DiscordWebhook(url=os.environ['URL'])
        embed = DiscordEmbed(title="Invalidation!",description="ID: " + vmessagei +" has been invalidated!",color='ff0000')
        embed.add_embed_field(name="Info",value="Issuer: " + str(message.author))
        webhook.add_embed(embed)
        response = webhook.execute()
        await message.channel.send("Applicaton ID `" + vmessagei +"` has been  invalidated.")
        #Invalidates ID
    if message.content.startswith('&revalid'):
        vmessagev = message.content
        vmessagev = vmessagev.replace("&revalid ", "")
        vmessagev = vmessagev.replace(" ", "")
        if vmessagev in blacklistedID:
            blacklistedID.pop(vmessagev)
            openfile = open("data.json", "w")
            openfile.write(str(blacklistedID))
            openfile.close()
            webhook = DiscordWebhook(url=os.environ['URL'])
            embed = DiscordEmbed(title="Revalidation!",description="ID: " + vmessagev +" has been revalidated!",color='00ff00')
            embed.add_embed_field(name="Info",value="Issuer: " + str(message.author))
            webhook.add_embed(embed)
            response = webhook.execute()
            await message.channel.send("Applicaton ID `" + vmessagev +"` has been revalidated.")
        else:
            await message.channel.send("Applicaton ID `" + vmessagev +"` has not been invalidated.")
        #Revalidates ID
    if message.content.startswith('&allvalid'):
        blacklistedID.clear()
        openfile = open("data2.json", "w")
        openfile.write("0")
        openfile.close()
        webhook = DiscordWebhook(url=os.environ['URL'])
        embed = DiscordEmbed(title="Validation!",description="All files has been revalidated",color='00ff00')
        embed.add_embed_field(name="Info",value="Issuer: " + str(message.author))
        webhook.add_embed(embed)
        response = webhook.execute()
        await message.channel.send("All invalidated IDs has been validated.")
    if message.content.startswith('&allinvalid'):
        openfile = open("data2.json", "w")
        openfile.write("1")
        openfile.close()
        webhook = DiscordWebhook(url=os.environ['URL'])
        embed = DiscordEmbed(title="Invalidation!",description="All files has been invalided",color='ff0000')
        embed.add_embed_field(name="Info",value="Issuer: " + str(message.author))
        webhook.add_embed(embed)
        response = webhook.execute()
        await message.channel.send("All validated IDs has been invalidated.")
    if message.content.startswith('&help'):
        embed=discord.Embed(title="Help", description="List of all commands for Gearet", color=0xff8800)
        embed.add_field(name="&invalid", value="This command makes an ID invalid. (Prefix) `&invalid [ID]` ", inline=False)
        embed.add_field(name="&revalid", value="This command makes an ID valid if it has been invalid. (Prefix) `&revalid [ID]` ", inline=False)
        embed.add_field(name="&allvalid", value="This command makes all IDs valid again. (Prefix) `&allvalid`", inline=False)
        embed.add_field(name="&allinvalid", value="This command makes all IDs invalid. (Prefix) `&allinvalid`", inline=False)
        await message.channel.send(embed=embed)


try:
    client.run(os.getenv('TOKEN'))
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    print (bot.is_ws_ratelimited())
    system("python restarter.py")
    system('kill 1')
