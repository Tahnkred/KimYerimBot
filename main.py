import discord

import random

from discord.ext import commands

client = commands.Bot(command_prefix=',')


@client.event
async def on_ready():
    print("Kim Yerim est en ligne.")


@client.event
async def on_member_join(member):
    print(f'{member} a rejoint le serveur.')


@client.event
async def on_member_remove(member):
    print(f'{member} a quitté le serveur.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong ! La connexion s\'établie à {round(client.latency * 1000 )} ms')


@client.command(aliases=['8ball', 'test', 'question'])
async def _8ball(ctx, *, question):
    await ctx.send(f'{ctx.message.author.mention} m\'a demandé «{question}», et je lui ai bien évidemment répondu '
                   f'«{random.choice(responses)}»')
responses = ['Demande à ta mère.', 'Ptdr t\'es qui ?',
             'Pourquoi tu demandes ça à moi ? Y\'a pas assez de blaireaux sur Terre ??', 'Ui.', 'No.',
             'Putain mais pourquoi tu demandes ça à moi ?????', 'Demande à Google.']


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, amount=None):
    await ctx.channel.purge(limit=amount+1)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'L\'utilisateur {member.mention} a été kick avec succès.')


@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'L\'utilisateur {member.mention} a été banni avec succès.')

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, *, reason=None):
    await member.unban(reason=reason)
    await ctx.send(f'L\'utilisateur {member.mention} a été débanni avec succès.')


@client.command(aliases=['sb'])
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await member.unban()
    await ctx.send(f'L\'utilisateur {member.mention} a été soft-ban avec succès.')


client.run('NzUwMDM3Njk5NzU0MzI4MDg1.X00tCg.LrYhtvS_pMacX2VZSP-BdTwoMgc')
