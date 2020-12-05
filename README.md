# au-bot
A Twitter bot that generates AU prompts for fanfiction writers.

# Keywords

## ROLESAME
Use the ROLESAME keyword in your tweet to generate role-based prompts.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot Send me a sweet ROLESAME prompt, dude
au_bot: @twitter_user Park Rangers
```
Or:
<br>
```
twitter_user: @au_bot I'd love a ROLESAME prompt
au_bot: @twitter_user Roommates
```

## ROLEDIFF
Use the ROLE keyword in your tweet to generate prompts with distinct roles for your pairing.
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
That^ degree of congruity may not be achieved every time. You could easily get `Violinist/Tennis Coach`. I'd still read it.


## CROSSOVER [Actor Name]/[Actor Name]
Use the CROSSOVER keyword to generate TV/movie character crossover prompts.
<br>
<br>
For example:
<br>
```
twitter_user: @au_bot CROSSOVER Joseph Mazzello/Rami Malek please?
au_bot: @twitter_user Dustin Moskovitz (The Social Network)/Elliot Alderson (Mr. Robot)
```
Or, because zeitgeist:
<br>
```
twitter_user: @au_bot CROSSOVER Jensen Ackles/Misha Collins if you’d be so kind
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
Using the keyword ROLESAME-SAFE or ROLEDIFF-SAFE in your request tweet excludes these roles too.


## Crossovers
Using the keyword CROSSOVER-SAFE in your request tweet makes sure that characters from movies/shows with the genres 'War', 'Horror' and 'Crime' are not returned.
<br>
Characters portrayed by actors aged under 18 at the time of the movie or episode's release are automatically excluded.

# References
Actor and movie/TV data is sourced from [TheMovieDB API](https://www.themoviedb.org/documentation/api/terms-of-use).

# Suggestions
Please submit any suggestions to me via Twitter ([@thegardendoor](https://twitter.com/thegardendoor)) or Tumblr ([@captainss](https://captainss.tumblr.com/)).
