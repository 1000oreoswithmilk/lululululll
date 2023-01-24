import discord
import asyncio
import random
import string
import re
import datetime
from datetime import datetime, timedelta
from discord.ext import commands
#import Verification
#import Support

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
verification_attempts = {}
tickets = {}
#bot.add_cog(Verification(bot))
#bot.add_cog(Support(bot))


PROFANITY_LIST = ["2 girls 1 cup","2g1c","4r5e","5h1t","5hit","a55","a_s_s","acrotomophilia","alabama hot pocket","alaskan pipeline","anal","anilingus","anus","apeshit","ar5e","arrse","arse","arsehole","ass","ass-fucker","ass-hat","ass-pirate","assbag","assbandit","assbanger","assbite","assclown","asscock","asscracker","asses","assface","assfucker","assfukka","assgoblin","asshat","asshead","asshole","assholes","asshopper","assjacker","asslick","asslicker","assmonkey","assmunch","assmuncher","asspirate","assshole","asssucker","asswad","asswhole","asswipe","auto erotic","autoerotic","b!tch","b00bs","b17ch","b1tch","babeland","baby batter","baby juice","ball gag","ball gravy","ball kicking","ball licking","ball sack","ball sucking","ballbag","balls","ballsack","bampot","bangbros","bareback","barely legal","barenaked","bastard","bastardo","bastinado","bbw","bdsm","beaner","beaners","beastial","beastiality","beastility","beaver cleaver","beaver lips","bellend","bestial","bestiality","bi+ch","biatch","big black","big breasts","big knockers","big tits","bimbos","birdlock","bitch","bitcher","bitchers","bitches","bitchin","bitching","black cock","blonde action","blonde on blonde action","bloody","blow job","blow your load","blowjob","blowjobs","blue waffle","blumpkin","boiolas","bollock","bollocks","bollok","bollox","bondage","boner","boob","boobie","boobs","booobs","boooobs","booooobs","booooooobs","booty call","breasts","brown showers","brunette action","buceta","bugger","bukkake","bulldyke","bullet vibe","bullshit","bum","bung hole","bunghole","bunny fucker","busty","butt","butt-pirate","buttcheeks","butthole","buttmunch","buttplug","c0ck","c0cksucker","camel toe","camgirl","camslut","camwhore","carpet muncher","carpetmuncher","cawk","chinc","chink","choad","chocolate rosebuds","chode","cipa","circlejerk","cl1t","cleveland steamer","clit","clitface","clitoris","clits","clover clamps","clusterfuck","cnut","cock","cock-sucker","cockbite","cockburger","cockface","cockhead","cockjockey","cockknoker","cockmaster","cockmongler","cockmongruel","cockmonkey","cockmunch","cockmuncher","cocknose","cocknugget","cocks","cockshit","cocksmith","cocksmoker","cocksuck","cocksuck ","cocksucked","cocksucked ","cocksucker","cocksucking","cocksucks ","cocksuka","cocksukka","cok","cokmuncher","coksucka","coochie","coochy","coon","coons","cooter","coprolagnia","coprophilia","cornhole","cox","crap","creampie","cum","cumbubble","cumdumpster","cumguzzler","cumjockey","cummer","cumming","cums","cumshot","cumslut","cumtart","cunilingus","cunillingus","cunnie","cunnilingus","cunt","cuntface","cunthole","cuntlick","cuntlick ","cuntlicker","cuntlicker ","cuntlicking","cuntlicking ","cuntrag","cunts","cyalis","cyberfuc","cyberfuck ","cyberfucked ","cyberfucker","cyberfuckers","cyberfucking ","d1ck","dammit","damn","darkie","date rape","daterape","deep throat","deepthroat","dendrophilia","dick","dickbag","dickbeater","dickface","dickhead","dickhole","dickjuice","dickmilk","dickmonger","dickslap","dicksucker","dickwad","dickweasel","dickweed","dickwod","dike","dildo","dildos","dingleberries","dingleberry","dink","dinks","dipshit","dirsa","dirty pillows","dirty sanchez","dlck","dog style","dog-fucker","doggie style","doggiestyle","doggin","dogging","doggy style","doggystyle","dolcett","domination","dominatrix","dommes","donkey punch","donkeyribber","doochbag","dookie","doosh","double dong","double penetration","douche","douchebag","dp action","dry hump","duche","dumbshit","dumshit","dvda","dyke","eat my ass","ecchi","ejaculate","ejaculated","ejaculates ","ejaculating ","ejaculatings","ejaculation","ejakulate","erotic","erotism","escort","eunuch","f u c k","f u c k e r","f4nny","f_u_c_k","fag","fagbag","fagg","fagging","faggit","faggitt","faggot","faggs","fagot","fagots","fags","fagtard","fanny","fannyflaps","fannyfucker","fanyy","fart","farted","farting","farty","fatass","fcuk","fcuker","fcuking","fecal","feck","fecker","felatio","felch","felching","fellate","fellatio","feltch","female squirting","femdom","figging","fingerbang","fingerfuck ","fingerfucked ","fingerfucker ","fingerfuckers","fingerfucking ","fingerfucks ","fingering","fistfuck","fistfucked ","fistfucker ","fistfuckers ","fistfucking ","fistfuckings ","fistfucks ","fisting","flamer","flange","fook","fooker","foot fetish","footjob","frotting","fuck","fuck buttons","fucka","fucked","fucker","fuckers","fuckhead","fuckheads","fuckin","fucking","fuckings","fuckingshitmotherfucker","fuckme ","fucks","fucktards","fuckwhit","fuckwit","fudge packer","fudgepacker","fuk","fuker","fukker","fukkin","fuks","fukwhit","fukwit","futanari","fux","fux0r","g-spot","gang bang","gangbang","gangbanged","gangbanged ","gangbangs ","gay sex","gayass","gaybob","gaydo","gaylord","gaysex","gaytard","gaywad","genitals","giant cock","girl on","girl on top","girls gone wild","goatcx","goatse","god damn","god-dam","god-damned","goddamn","goddamned","gokkun","golden shower","goo girl","gooch","goodpoop","gook","goregasm","gringo","grope","group sex","guido","guro","hand job","handjob","hard core","hardcore","hardcoresex ","heeb","hell","hentai","heshe","ho","hoar","hoare","hoe","hoer","homo","homoerotic","honkey","honky","hooker","hore","horniest","horny","hot carl","hot chick","hotsex","how to kill","how to murder","huge fat","humping","incest","intercourse","jack off","jack-off ","jackass","jackoff","jail bait","jailbait","jap","jelly donut","jerk off","jerk-off ","jigaboo","jiggaboo","jiggerboo","jism","jiz","jiz ","jizm","jizm ","jizz","juggs","kawk","kike","kinbaku","kinkster","kinky","kiunt","knob","knobbing","knobead","knobed","knobend","knobhead","knobjocky","knobjokey","kock","kondum","kondums","kooch","kootch","kum","kumer","kummer","kumming","kums","kunilingus","kunt","kyke","l3i+ch","l3itch","labia","leather restraint","leather straight jacket","lemon party","lesbo","lezzie","lmfao","lolita","lovemaking","lust","lusting","m0f0","m0fo","m45terbate","ma5terb8","ma5terbate","make me come","male squirting","masochist","master-bate","masterb8","masterbat*","masterbat3","masterbate","masterbation","masterbations","masturbate","menage a trois","milf","minge","missionary position","mo-fo","mof0","mofo","mothafuck","mothafucka","mothafuckas","mothafuckaz","mothafucked ","mothafucker","mothafuckers","mothafuckin","mothafucking ","mothafuckings","mothafucks","mother fucker","motherfuck","motherfucked","motherfucker","motherfuckers","motherfuckin","motherfucking","motherfuckings","motherfuckka","motherfucks","mound of venus","mr hands","muff","muff diver","muffdiver","muffdiving","mutha","muthafecker","muthafuckker","muther","mutherfucker","n1gga","n1gger","nambla","nawashi","nazi","negro","neonazi","nig nog","nigg3r","nigg4h","nigga","niggah","niggas","niggaz","nigger","niggers ","niglet","nimphomania","nipple","nipples","nob","nob jokey","nobhead","nobjocky","nobjokey","nsfw images","nude","nudity","numbnuts","nutsack","nympho","nymphomania","octopussy","omorashi","one cup two girls","one guy one jar","orgasim","orgasim ","orgasims ","orgasm","orgasms ","orgy","p0rn","paedophile","paki","panooch","panties","panty","pawn","pecker","peckerhead","pedobear","pedophile","pegging","penis","penisfucker","phone sex","phonesex","phuck","phuk","phuked","phuking","phukked","phukking","phuks","phuq","piece of shit","pigfucker","pimpis","pis","pises","pisin","pising","pisof","piss","piss pig","pissed","pisser","pissers","pisses ","pissflap","pissflaps","pissin","pissin ","pissing","pissoff","pissoff ","pisspig","playboy","pleasure chest","pole smoker","polesmoker","pollock","ponyplay","poo","poof","poon","poonani","poonany","poontang","poop","poop chute","poopchute","porn","porno","pornography","pornos","prick","pricks ","prince albert piercing","pron","pthc","pube","pubes","punanny","punany","punta","pusies","pusse","pussi","pussies","pussy","pussylicking","pussys ","pusy","puto","queaf","queef","queerbait","queerhole","quim","raghead","raging boner","rape","raping","rapist","rectum","renob","retard","reverse cowgirl","rimjaw","rimjob","rimming","rosy palm","rosy palm and her 5 sisters","ruski","rusty trombone","s hit","s&m","s.o.b.","s_h_i_t","sadism","sadist","santorum","scat","schlong","scissoring","screwing","scroat","scrote","scrotum","semen","sex","sexo","sexy","sh!+","sh!t","sh1t","shag","shagger","shaggin","shagging","shaved beaver","shaved pussy","shemale","shi+","shibari","shit","shit-ass","shit-bag","shit-bagger","shit-brain","shit-breath","shit-cunt","shit-dick","shit-eating","shit-face","shit-faced","shit-fit","shit-head","shit-heel","shit-hole","shit-house","shit-load","shit-pot","shit-spitter","shit-stain","shitass","shitbag","shitbagger","shitblimp","shitbrain","shitbreath","shitcunt","shitdick","shite","shiteating","shited","shitey","shitface","shitfaced","shitfit","shitfuck","shitfull","shithead","shitheel","shithole","shithouse","shiting","shitings","shitload","shitpot","shits","shitspitter","shitstain","shitted","shitter","shitters ","shittiest","shitting","shittings","shitty","shitty ","shity","shiz","shiznit","shota","shrimping","skank","skeet","slanteye","slut","slutbag","sluts","smeg","smegma","smut","snatch","snowballing","sodomize","sodomy","son-of-a-bitch","spac","spic","spick","splooge","splooge moose","spooge","spread legs","spunk","strap on","strapon","strappado","strip club","style doggy","suck","sucks","suicide girls","sultry women","swastika","swinger","t1tt1e5","t1tties","tainted love","tard","taste my","tea bagging","teets","teez","testical","testicle","threesome","throating","thundercunt","tied up","tight white","tit","titfuck","tits","titt","tittie5","tittiefucker","titties","titty","tittyfuck","tittywank","titwank","tongue in a","topless","tosser","towelhead","tranny","tribadism","tub girl","tubgirl","turd","tushy","tw4t","twat","twathead","twatlips","twatty","twink","twinkie","two girls one cup","twunt","twunter","undressing","upskirt","urethra play","urophilia","v14gra","v1gra","va-j-j","vag","vagina","venus mound","viagra","vibrator","violet wand","vjayjay","vorarephilia","voyeur","vulva","w00se","wang","wank","wanker","wanky","wet dream","wetback","white power","whoar","whore","willies","willy","wrapping men","wrinkled starfish","xrated","xx","xxx","yaoi","yellow showers","yiffy","zoophilia","🖕"]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')



STAFF_NOTES_CHANNEL_ID = 1041975889602281522
WARNINGS_LIMIT = 10
warnings = {}
@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
    # Check if the message contains any profanity
    for word in PROFANITY_LIST:
        if word in message.content.lower():
            # Replace the profanity with "CONTENT-CLEARED"
            new_content = message.content.replace(word, "CONTENT-CLEARED")
            await message.edit(content=new_content)

            # Add a warning for the user
            if message.author.id in warnings:
                warnings[message.author.id] += 1
            else:
                warnings[message.author.id] = 1

            # Send a message to the staff-notes channel with the user's information and warnings
            staff_notes = bot.get_channel(STAFF_NOTES_CHANNEL_ID)
            await staff_notes.send(f'Member: {message.author.mention}\nWarnings: {warnings[message.author.id]}\nChannel: {message.channel.mention}')

SECRET_KEY = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@bot.command(name='Verify')
async def verify(ctx):
    member = ctx.author
    await ctx.send(f'Hello {member.mention}, 𝕀 𝕒𝕞 𝕍𝕚𝕜𝕚 ℍ𝕖𝕒𝕕 𝕆𝕗 𝕊𝕖𝕔𝕦𝕣𝕚𝕥𝕪 𝕗𝕠𝕣: ☼𝕎𝕒𝕧𝕖𝕝𝕪 ℙ𝕣𝕠𝕞𝕠𝕥𝕚𝕠𝕟𝕤☼')
    await asyncio.sleep(2)
    await ctx.send(f'ℙ𝕝𝕖𝕒𝕤𝕖 𝕧𝕖𝕣𝕚𝕗𝕪 𝕥𝕙𝕖 𝕗𝕠𝕝𝕝𝕠𝕨𝕚𝕟𝕘 𝕤𝕖𝕔𝕦𝕣𝕖 𝕤𝕥𝕣𝕚𝕟𝕘: `{SECRET_KEY}`')
    def check(m):
        return m.author == member and m.channel == ctx.channel
    try:
        response = await bot.wait_for('message', check=check, timeout=300.0)
    except asyncio.TimeoutError:
        await ctx.send(f'{member.mention} 𝕀 𝕒𝕞 𝕤𝕠𝕣𝕣𝕪 𝕐𝕠𝕦 𝕞𝕦𝕤𝕥 𝕥𝕪𝕡𝕖 𝕥𝕙𝕖 𝕤𝕥𝕣𝕚𝕟𝕘 𝕤𝕚𝕝𝕝𝕪, ℙ𝕝𝕖𝕒𝕤𝕖 𝕥𝕣𝕪 𝕒𝕘𝕒𝕚𝕟 𝕚𝕟 𝟝 𝕞𝕚𝕟𝕦𝕥𝕖𝕤.')
        return
    if response.content != SECRET_KEY:
        await ctx.send(f'{member.mention} 𝕊𝕚𝕝𝕝𝕪 𝕘𝕠𝕠𝕤𝕖 𝕥𝕙𝕒𝕥 𝕚𝕤 𝕟𝕠𝕥 𝕥𝕙𝕖 𝕣𝕚𝕘𝕙𝕥 𝕤𝕥𝕣𝕚𝕟𝕘, 𝕡𝕝𝕖𝕒𝕤𝕖 𝕥𝕣𝕪 𝕒𝕘𝕒𝕚𝕟 𝕚𝕟 𝟝 𝕞𝕚𝕟𝕦𝕥𝕖𝕤.')
        return
    await ctx.send(f'𝕍𝕖𝕣𝕚𝕗𝕚𝕔𝕒𝕥𝕚𝕠𝕟 𝕤𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝, 𝕣𝕖𝕞𝕠𝕧𝕚𝕟𝕘 𝕖𝕩𝕚𝕤𝕥𝕚𝕟𝕘 𝕣𝕠𝕝𝕖𝕤 𝕒𝕟𝕕 𝕒𝕕𝕕𝕚𝕟𝕘 🎔𝕄𝕖𝕞𝕓𝕖𝕣🎔𝕣𝕠𝕝𝕖.')
    # remove all existing roles
    for role in member.roles:
        if role.name != '@everyone':
            await member.remove_roles(role)
    # add the @member role
    member_role = discord.utils.get(ctx.guild.roles, name='🎔𝕄𝕖𝕞𝕓𝕖𝕣🎔')
    await member.add_roles(member_role)
    await ctx.channel.purge(limit=2, check=lambda m: m.author == bot)

@bot.command(name='Support')
async def support(ctx):
    if ctx.channel.name != "☼𝕊𝕦𝕡𝕡𝕠𝕣𝕥☼":
        await ctx.send("𝕋𝕙𝕚𝕤 𝕔𝕠𝕞𝕞𝕒𝕟𝕕 𝕔𝕒𝕟 𝕠𝕟𝕝𝕪 𝕓𝕖 𝕦𝕤𝕖𝕕 𝕚𝕟 𝕥𝕙𝕖 𝕤𝕦𝕡𝕡𝕠𝕣𝕥 𝕔𝕙𝕒𝕟𝕟𝕖𝕝.")
        return
    member = ctx.author
    # Check if the user already has an open ticket
    if member.id in tickets:
        await ctx.send(f'{member.mention} 𝕐𝕠𝕦 𝕒𝕝𝕣𝕖𝕒𝕕𝕪 𝕙𝕒𝕧𝕖 𝕒𝕟 𝕠𝕡𝕖𝕟 𝕥𝕚𝕔𝕜𝕖𝕥. ℙ𝕝𝕖𝕒𝕤𝕖 𝕦𝕤𝕖 !𝕔𝕒𝕟𝕔𝕖𝕝 𝕥𝕠 𝕔𝕝𝕠𝕤𝕖 𝕚𝕥 𝕓𝕖𝕗𝕠𝕣𝕖 𝕔𝕣𝕖𝕒𝕥𝕚𝕟𝕘 𝕒 𝕟𝕖𝕨 𝕠𝕟𝕖.')
        return
    await ctx.send(f'Hello {member.mention}, I am Viki')
    await asyncio.sleep(2)
    await ctx.send(f'ℂ𝕒𝕟 𝕀 𝕡𝕝𝕖𝕒𝕤𝕖 𝕘𝕖𝕥 𝕪𝕠𝕦𝕣 𝔻𝕚𝕤𝕔𝕠𝕣𝕕 𝕦𝕤𝕖𝕣𝕟𝕒𝕞𝕖 𝕨𝕚𝕥𝕙 𝕪𝕠𝕦𝕣 𝕥𝕒𝕘𝕤?')
    def check(m):
        return m.author == member and m.channel == ctx.channel
    try:
        username = await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send(f'{member.mention} 𝕋𝕚𝕞𝕖𝕠𝕦𝕥, ℙ𝕝𝕖𝕒𝕤𝕖 𝕥𝕣𝕪 𝕒𝕘𝕒𝕚𝕟')
        return
    await ctx.send(f'𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦, ℙ𝕝𝕖𝕒𝕤𝕖 𝕒𝕝𝕝𝕠𝕨 𝕞𝕖 𝕒 𝕞𝕠𝕞𝕖𝕟𝕥 𝕥𝕠 𝕒𝕕𝕕 𝕪𝕠𝕦 𝕚𝕟 𝕥𝕙𝕖 𝕤𝕪𝕤𝕥𝕖𝕞')
    await asyncio.sleep(2)
    await ctx.send(f'𝕆𝕜, ℂ𝕒𝕟 𝕀 𝕡𝕝𝕖𝕒𝕤𝕖 𝕘𝕖𝕥 𝕥𝕙𝕖 𝕣𝕖𝕒𝕤𝕠𝕟 𝕗𝕠𝕣 𝕔𝕠𝕟𝕥𝕒𝕔𝕥𝕚𝕟𝕘 𝕔𝕦𝕤𝕥𝕠𝕞𝕖𝕣 𝕤𝕦𝕡𝕡𝕠𝕣𝕥?')
    try:
        reason = await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send(f'{member.mention} 𝕋𝕚𝕞𝕖𝕠𝕦𝕥, ℙ𝕝𝕖𝕒𝕤𝕖 𝕥𝕣𝕪 𝕒𝕘𝕒𝕚𝕟')
        return
    await ctx.send(f'𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦 𝕗𝕠𝕣 𝕥𝕙𝕒𝕥 𝕚𝕟𝕗𝕠𝕣𝕞𝕒𝕥𝕚𝕠𝕟, 𝔸𝕝𝕝𝕠𝕨 𝕞𝕖 𝕒 𝕞𝕠𝕞𝕖𝕟𝕥 𝕥𝕠 𝕤𝕖𝕥 𝕪𝕠𝕦 𝕦𝕡')
    # Get the "community" category
    category = discord.utils.get(ctx.guild.categories, name='♋ ℂ𝕠𝕞𝕞𝕦𝕟𝕚𝕥𝕪 ℂ𝕖𝕟𝕥𝕖𝕣 ♋')
    # Create the support ticket channel
    channel = await ctx.guild.create_text_channel(name=f'{username.content} Support Ticket', category=category)
    # Send the support creation message to the staff-notes channel
    staff_notes = bot.get_channel(1041975889602281522)
    await staff_notes.send(f'{username.content} 𝕙𝕒𝕤 𝕔𝕣𝕖𝕒𝕥𝕖𝕕 𝕒 𝕤𝕦𝕡𝕡𝕠𝕣𝕥 𝕥𝕚𝕔𝕜𝕖𝕥. ℝ𝕖𝕒𝕤𝕠𝕟: {reason.content} ℂ𝕙𝕒𝕟𝕟𝕖𝕝: <#{channel.id}>')
    # Send the initial question to the user
    await channel.send(f'ℍ𝕠𝕨 𝕞𝕒𝕪 𝕀 𝕙𝕖𝕝𝕡 𝕪𝕠𝕦 𝕥𝕠𝕕𝕒𝕪? \n𝟙: 𝔽𝕚𝕝𝕚𝕟𝕘 𝕒 𝕣𝕖𝕡𝕠𝕣𝕥 \n𝟚: 𝔽𝕚𝕝𝕚𝕟𝕘 𝕒 𝕤𝕦𝕘𝕘𝕖𝕤𝕥𝕚𝕠𝕟 \n𝟛: 𝕆𝕥𝕙𝕖𝕣 \n𝟜: ℂ𝕒𝕟𝕔𝕖𝕝')
    def check_support_type(m):
        return m.author == member and m.channel == channel
    try:
        support_type = await bot.wait_for('message', check=check_support_type, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send(f'{member.mention} 𝕋𝕚𝕞𝕖𝕠𝕦𝕥, ℙ𝕝𝕖𝕒𝕤𝕖 𝕥𝕣𝕪 𝕒𝕘𝕒𝕚𝕟')
        return
    if support_type.content == '1':
        await channel.send(f'𝕆𝕜, ℙ𝕝𝕖𝕒𝕤𝕖 𝔸𝕝𝕝𝕠𝕨 𝕞𝕖 𝕒 𝕞𝕠𝕞𝕞𝕖𝕟𝕥.')
        await asyncio.sleep(2)
        await channel.send(f'𝕆𝕜, ℙ𝕝𝕖𝕒𝕤𝕖 𝕔𝕠𝕡𝕪 𝕥𝕙𝕚𝕤 𝕗𝕠𝕣𝕞𝕒𝕥 𝕒𝕟𝕕 𝕡𝕒𝕤𝕥𝕖 𝕚𝕥 𝕚𝕟 𝕥𝕙𝕖 𝕔𝕙𝕒𝕥 𝕓𝕠𝕩 𝕒𝕟𝕕 𝕗𝕚𝕝𝕝 𝕚𝕥 𝕚𝕟, 𝕋𝕙𝕖𝕟 𝕤𝕖𝕟𝕕 𝕥𝕙𝕖 𝕗𝕠𝕣𝕞𝕒𝕥.')
        await asyncio.sleep(2)
        await channel.send(f'𝕐𝕠𝕦𝕣 𝔻𝕚𝕤𝕔𝕠𝕣𝕕 𝕦𝕤𝕖𝕣𝕟𝕒𝕞𝕖: \n𝕊𝕦𝕤𝕡𝕖𝕔𝕥: \n𝔻𝕒𝕥𝕖 𝕠𝕗 𝕚𝕟𝕔𝕚𝕕𝕖𝕟𝕥: \n𝕋𝕚𝕞𝕖 𝕠𝕗 𝕚𝕟𝕔𝕚𝕕𝕖𝕟𝕥: \nℙ𝕣𝕠𝕠𝕗 𝕠𝕗 𝕚𝕟𝕔𝕚𝕕𝕖𝕟𝕥:')
    elif support_type.content == '2':
        await channel.send(f'𝕆𝕜, ℙ𝕝𝕖𝕒𝕤𝕖 𝔸𝕝𝕝𝕠𝕨 𝕞𝕖 𝕒 𝕞𝕠𝕞𝕞𝕖𝕟𝕥.')
        await asyncio.sleep(2)
        await channel.send(f'𝕆𝕜, ℙ𝕝𝕖𝕒𝕤𝕖 𝕔𝕠𝕡𝕪 𝕥𝕙𝕚𝕤 𝕗𝕠𝕣𝕞𝕒𝕥 𝕒𝕟𝕕 𝕡𝕒𝕤𝕥𝕖 𝕚𝕥 𝕚𝕟 𝕥𝕙𝕖 𝕔𝕙𝕒𝕥 𝕓𝕠𝕩 𝕒𝕟𝕕 𝕗𝕚𝕝𝕝 𝕚𝕥 𝕚𝕟, 𝕋𝕙𝕖𝕟 𝕤𝕖𝕟𝕕 𝕥𝕙𝕖 𝕗𝕠𝕣𝕞𝕒𝕥.')
        await asyncio.sleep(2)
        await channel.send(f'𝕐𝕠𝕦𝕣 𝔻𝕚𝕤𝕔𝕠𝕣𝕕 𝕦𝕤𝕖𝕣𝕟𝕒𝕞𝕖: \n𝔻𝕒𝕥𝕖 𝕠𝕗 𝕤𝕦𝕘𝕘𝕖𝕤𝕥𝕚𝕠𝕟: \n𝕊𝕦𝕘𝕘𝕖𝕤𝕥𝕚𝕠𝕟:')
    elif support_type.content == '3':
        await channel.send(f'𝕆𝕜, ℙ𝕝𝕖𝕒𝕤𝕖 𝔸𝕝𝕝𝕠𝕨 𝕞𝕖 𝕒 𝕞𝕠𝕞𝕞𝕖𝕟𝕥.')
        await asyncio.sleep(2)
        await channel.send(f'𝕆𝕜, 𝕃𝕖𝕥 𝕞𝕖 𝕔𝕠𝕟𝕥𝕒𝕔𝕥 𝕥𝕙𝕖 𝕤𝕦𝕡𝕡𝕠𝕣𝕥 𝕥𝕖𝕒𝕞')
        staff_notes = bot.get_channel(1041975889602281522)
        await staff_notes.send(f'{username.content} 𝕚𝕤 𝕣𝕖𝕢𝕦𝕖𝕤𝕥𝕚𝕟𝕘 𝕔𝕦𝕤𝕥𝕠𝕞𝕖𝕣 𝕤𝕦𝕡𝕡𝕠𝕣𝕥')
    elif support_type.content == '4':
        await channel.send(f'𝕆𝕜, ℙ𝕝𝕖𝕒𝕤𝕖 𝕒𝕝𝕝𝕠𝕨 𝕞𝕖 𝕒 𝕞𝕠𝕞𝕖𝕟𝕥 𝕥𝕠 𝕔𝕝𝕠𝕤𝕖 𝕪𝕠𝕦𝕣 𝕥𝕚𝕔𝕜𝕖𝕥')
        await asyncio.sleep(5)
        await channel.delete()
        del tickets[member.id]
        return
    else:
        await channel.send(f'𝕀𝕟𝕧𝕒𝕝𝕚𝕕 𝕠𝕡𝕥𝕚𝕠𝕟, 𝕡𝕝𝕖𝕒𝕤𝕖 𝕤𝕖𝕝𝕖𝕔𝕥 𝕒𝕘𝕒𝕚𝕟')
        return

    tickets[member.id] = channel
    await channel.send(f'{member.mention} 𝕐𝕠𝕦𝕣 𝕊𝕦𝕡𝕡𝕠𝕣𝕥 𝕋𝕚𝕔𝕜𝕖𝕥 ℍ𝕒𝕤 𝔹𝕖𝕖𝕟 ℂ𝕣𝕖𝕒𝕥𝕖𝕕 ℙ𝕝𝕖𝕒𝕤𝕖 ℝ𝕖𝕡𝕠𝕣𝕥 𝕥𝕙𝕖𝕣𝕖 ℝ𝕚𝕘𝕙𝕥 𝕒𝕨𝕒𝕪, 𝕌𝕤𝕖 !ℂ𝕒𝕟𝕔𝕖𝕝 𝕒𝕟𝕪 𝕥𝕚𝕞𝕖 𝕕𝕦𝕣𝕚𝕟𝕘 𝕪𝕠𝕦𝕣 𝕥𝕚𝕔𝕜𝕖𝕥 𝕥𝕠 𝕔𝕝𝕠𝕤𝕖 𝕪𝕠𝕦𝕣 𝕞𝕖𝕞𝕓𝕖𝕣 𝕥𝕚𝕔𝕜𝕖𝕥.')
    await ctx.channel.purge(limit=5)





@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(920086137236754442) # Replace with the actual channel ID
    await welcome_channel.send(f"𝕎𝕖𝕝𝕔𝕠𝕞𝕖 {member.mention} 𝕥𝕠 ☼𝕎𝕒𝕧𝕖𝕝𝕪 ℙ𝕣𝕠𝕞𝕠𝕥𝕚𝕠𝕟𝕤☼ ℝ𝕖𝕞𝕖𝕞𝕓𝕖𝕣 𝕚𝕗 𝕪𝕠𝕦 𝕝𝕖𝕒𝕧𝕖 𝕊𝕠 𝕕𝕠 𝕪𝕠𝕦𝕣 𝕒𝕕𝕤! 𝔼𝕟𝕛𝕠𝕪 𝕪𝕠𝕦𝕣 𝕤𝕥𝕒𝕪!")

@bot.event
async def on_member_remove(member):
    try:
        for channel in member.guild.text_channels:
            await channel.purge(limit=100, check=lambda m: m.author == member)
    except discord.Forbidden:
        print(f'The bot does not have the necessary permissions to delete messages in {channel.name}')
    except discord.HTTPException as e:
        print(f'Failed to delete messages: {e}')

    goodbye_channel_id = 920086137236754442
    goodbye_channel = bot.get_channel(goodbye_channel_id)
    if goodbye_channel:
        try:
            await goodbye_channel.send(f'𝔾𝕠𝕠𝕕𝕓𝕪𝕖 {member.mention}! 𝕎𝕖 𝕨𝕚𝕝𝕝 𝕞𝕚𝕤𝕤 𝕪𝕠𝕦𝕣 𝕡𝕣𝕖𝕤𝕖𝕟𝕔𝕖 𝕒𝕟𝕕 𝕞𝕖𝕤𝕤𝕒𝕘𝕖𝕤')
        except discord.Forbidden:
            print(f'The bot does not have the necessary permissions to send messages in {goodbye_channel.name}')
        except discord.HTTPException as e:
            print(f'Failed to send goodbye message: {e}')
    else:
        print(f'The channel with ID {goodbye_channel_id} could not be found')







bot.run("MTA2NTA2MTc1NzgzNzYzOTc2MA.GB-kmW.iabdCnK5MjSaGY70Pm3PMBAdS0nNvrWLH3wQiI")


        
