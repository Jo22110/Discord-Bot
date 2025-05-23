from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', description='Kick a member from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'✅ {member.display_name} has been kicked from the server.')

    @commands.command(name='ban', description='Ban a member from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'✅ {member.display_name} has been banned from the server.')

    @commands.command(name='unban', description='Unban a member from the server')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            if ban_entry.user.name == member_name and ban_entry.user.discriminator == member_discriminator:
                await ctx.guild.unban(ban_entry.user)
                await ctx.send(f'✅ {ban_entry.user.display_name} has been unbanned from the server.')
                return
        await ctx.send(f'❌ User {member} not found in banned users.')

    @commands.command(name='clear', description='Clear a specified number of messages from the channel')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'✅ Cleared {amount} messages.', delete_after=5)

def setup(bot):
    bot.add_cog(Moderation(bot))