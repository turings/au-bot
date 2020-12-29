# au-bot
A Twitter bot that generates AU prompts for fanfiction writers.

# User Guide
## Keywords
N.B. None of the keywords are case sensitive.
<br>

### SETTING
If you use the SETTING keyword, the bot will return an AU setting. This might be a location, a time period, or both.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot SETTING
au_bot: @twitter_user A newspaper office
```
Or:
<br>
```d
twitter_user: @au_bot my dinluke fic needs a setting please
au_bot: @twitter_user The 1960s California surf scene
```

### ROLE
Use the ROLE keyword in your tweet to generate role-based prompts.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot ROLE
au_bot: @twitter_user Park Rangers
```
Or:
<br>
```
twitter_user: @au_bot Send me a sweet role prompt, dude.
au_bot: @twitter_user 1980s yuppies
```

### ROLEDIFF
Use the ROLEDIFF keyword in your tweet to generate prompts with distinct roles for a pairing.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot ROLEDIFF
au_bot: @twitter_user Socialite/Tennis Coach
```
Or:
<br>
```
twitter_user: @au_bot rolediff me!!
au_bot: @twitter_user Violinist/Music Teacher
```
(Please note that the bot won't always return prompts with that^ degree of congruity. You could easily get `Violinist/Tennis Coach`. I'd still read it.)

### XOVER
Want to try writing a crossover fic? If you use the XOVER keyword, the bot will suggest a popular TV/movie fandom.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot XOVER
au_bot: @twitter_user Pacific Rim
```
Or:
<br>
```
twitter_user: @au_bou I need a xover prompt, stat!
au_bot: @twitter_user Grey's Anatomy
```

### XOVER [Actor Name/Actor Name]
You can also use the XOVER keyword with a specific actor pairing in [square/brackets] to generate TV/movie character crossover prompts.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot XOVER [Joseph Mazzello/Rami Malek]
au_bot: @twitter_user Dustin Moskovitz (The Social Network)/Elliot Alderson (Mr. Robot)
```
Or, because zeitgeist:
<br>
```
twitter_user: @au_bot please xover [Jensen Ackles/Misha Collins] if you’d be so kind
au_bot: @twitter_user Jake Gray (DeVour)/Eric Bragg (Charmed)
```

## Content Filters

### Settings and Roles
Settings and roles related to the content types listed [here](https://trigger-warnings.tumblr.com/tags) are excluded as standard, apart from:
<br>
Illness & Injury (e.g., doctor, nurse)
<br>
Warfare (e.g., soldier)
<br>
Alcoholism (e.g. bartender)
<br>
Food (e.g. chef)
<br>
Using the keyword ROLE-SAFE, ROLEDIFF-SAFE, and SETTING-SAFE in your request tweet excludes these settings/roles too.


### Crossovers
Unfortunately, there are currently no content filters for **fandom** prompts.
<br>
For **character** prompts, using the keyword XOVER-SAFE in your request tweet makes sure that characters from movies/shows with the genres 'War', 'Horror' and 'Crime' are not returned.
<br>
Characters portrayed by actors who were under the age of 18 at the time of the movie or episode's release will never be returned.

## References
The popular fandoms are periodically scraped from [AO3](https://archiveofourown.org/).
<br>
The actor, movie and TV show data for character prompts comes from [TheMovieDB API](https://www.themoviedb.org/documentation/api/terms-of-use).

## Live Example
[@gimmeanau](https://twitter.com/gimmeanau) is hosted on [PythonAnywhere](https://www.pythonanywhere.com/).
