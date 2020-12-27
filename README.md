# au-bot
A Twitter bot that generates AU prompts for fanfiction writers.

# User Documentation
## Keywords
N.B. None of the following keywords are case sensitive.
<br>
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
Use the ROLEDIFF keyword in your tweet to generate prompts with distinct roles for your pairing.
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
(Please note that the bot will not always return prompts with that^ degree of congruity. You could easily get `Violinist/Tennis Coach`. I'd still read it.)

### XOVER
If you use the XOVER keyword, the bot will return a popular TV/movie fandom.
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
au_bot: @twitter_user House MD
```


### XOVER [Actor Name/Actor Name]
You can also use the CROSSOVER keyword with a specific actor pairing in [square/brackets] to generate TV/movie character crossover prompts.
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

### Roles and Settings
Roles related to the content types listed [here](https://trigger-warnings.tumblr.com/tags) are excluded as standard, apart from:
<br>
Illness & Injury (e.g., doctor, nurse)
<br>
Warfare (e.g., soldier)
<br>
Alcoholism (e.g. bartender)
<br>
Food (e.g. chef)
<br>
Using the keyword ROLE-SAFE, ROLEDIFF-SAFE, and SETTING-SAFE in your request tweet excludes these roles too.


### Crossovers
Unfortunately, there is currently no content filter for **fandom** prompts.
<br>
For **character** prompts, using the keyword XOVER-SAFE in your request tweet makes sure that characters from movies/shows with the genres 'War', 'Horror' and 'Crime' are not returned.
<br>
Characters portrayed by actors who were under the age of 18 at the time of the movie or episode's release will never be returned.

## References
The popular fandoms are periodically scraped from [AO3](https://archiveofourown.org/).
<br>
The actor, movie and TV show data for character prompts comes from [TheMovieDB API](https://www.themoviedb.org/documentation/api/terms-of-use).

## Suggestions
Please submit any promrpt suggestions to me via Twitter ([@thegardendoor](https://twitter.com/thegardendoor)).
