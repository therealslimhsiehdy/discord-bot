TLDR: !catfact will send a cat fact to you 

To run this you will need:
- Your own `.env` file with token in it
- Run the command `python3 bot.py` in the terminal

**1.** https://discord.com/developers/applications/ -- From here, you can create your application within Discord. I decided to start with creating a bot since it seemed like a great baby step to get into the ecosystem. To register your bot, you go to Settings > Bot > and the set up for your bot should appear from there. Please note that to invite your bot into the server you will need to go to Settings > OAuth2 > URL Generator > Scopes (click bot) and then copy the generated URL into a web browser to add it into your server.
**NOTE** You'll also need to install discord.py via pip `pip3 install discord.py`

**2.** `bot.py` -- the goal is to load the token in, set up intents (events Discord will send my app when there is some kind of callback), set up the command prefix (! in my case), check to make sure you're connected to the Discord API and then to wait for if your bot is called. Would recommend one to have a separate file (ie .env) for the bot token.

**3.** `cogs/cat.py` -- cogs is the type of "big picture" of applications you can create, hence the "cogs" folder. cat.py contains all the functions that can be called after the prefix to do something. For example, currently "!catfact" sends a random cat fact to the channel you're in when requested.

**3a.** I know I could've had multiple json files with facts in it to pull from, but went with [this API set up](https://catfact.ninja/) because they already offer simple RESTful API to grab random cat facts for us which we can retrive via an HTTP request to their endpoint to get a fact back in JSON format. Plus, I am a fan of Swagger API docs because of the ease of understanding documentation and playground to try it out all set up. [This API](https://alexwohlbruck.github.io/cat-facts/docs/) set up is also a great choice.

Resources:
- https://discord.com/developers/docs/getting-started
- https://discordpy.readthedocs.io/en/stable/api.html
- https://www.howtogeek.com/364225/how-to-make-your-own-discord-bot/