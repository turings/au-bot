# au-bot
A Twitter bot that generates AU prompts for fanfiction writers.

# Keywords

## ROLE
Use the ROLE keyword in your tweet to generate role-based prompts.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot Send me a sweet ROLE prompt, dude
au_bot: @twitter_user Park Rangers
```
Or:
<br>
```
twitter_user: @au_bot I'd love a ROLE prompt
au_bot: @twitter_user 1980s yuppies
```

## ROLEDIFF
Use the ROLEDIFF keyword in your tweet to generate prompts with distinct roles for your pairing.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot Any chance of a ROLEDIFF prompt?
au_bot: @twitter_user Socialite/Tennis Coach
```
Or:
<br>
```
twitter_user: @au_bot ROLEDIFF me!!
au_bot: @twitter_user Violinist/Music Teacher
```
(Please note that the bot will not always return prompts with that^ degree of congruity. You could easily get `Violinist/Tennis Coach`. I'd still read it.)

## CROSSOVER
If you use the CROSSOVER keyword, the bot will return a popular TV/movie fandom.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot I need a CROSSOVER, stat!
au_bot: @twitter_user Pacific Rim
```
Or:
<br>
```
twitter_user: @au_bou Send me a CROSSOVER
au_bot: @twitter_user House MD
```


## CROSSOVER [Actor Name/Actor Name]
You can also use the CROSSOVER keyword with a specific actor pairing in [square/brackets] to generate TV/movie character crossover prompts.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot CROSSOVER [Joseph Mazzello/Rami Malek] please?
au_bot: @twitter_user Dustin Moskovitz (The Social Network)/Elliot Alderson (Mr. Robot)
```
Or, because zeitgeist:
<br>
```
twitter_user: @au_bot CROSSOVER [Jensen Ackles/Misha Collins] if you’d be so kind
au_bot: @twitter_user Jake Gray (DeVour)/Eric Bragg (Charmed)
```

# Content Filters

## Roles
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
Using the keyword ROLE-SAFE or ROLEDIFF-SAFE in your request tweet excludes these roles too.


## Crossovers
Unfortunately, there is currently no content filter for **fandom** prompts.
<br>
For **character** prompts, using the keyword CROSSOVER-SAFE in your request tweet makes sure that characters from movies/shows with the genres 'War', 'Horror' and 'Crime' are not returned.
<br>
Characters portrayed by actors aged under 18 at the time of the movie or episode's release are automatically excluded.

# References
The popular fandoms are periodically scraped from [AO3](https://archiveofourown.org/).
<br>
The actor, movie and TV show data for character prompts comes from [TheMovieDB API](https://www.themoviedb.org/documentation/api/terms-of-use).

# Suggestions
Please submit any suggestions to me via Twitter ([@thegardendoor](https://twitter.com/thegardendoor)) or Tumblr ([@captainss](https://captainss.tumblr.com/)).
