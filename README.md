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
Use the ROLE keyword in your tweet to generate prompts with distinct roles for your OTPs.
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
You might not get that degree of congruity every time. You could easily get `Violinist/Tennis Coach`. I'd read it?


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
Roles related to the trigger warnings listed [here](https://trigger-warnings.tumblr.com/tags) are excluded as standard, apart from:
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
Using the keyword CROSSOVER-SAFE in your request tweet makes sure that characters from movies/shows with the genres 'War', 'Horror' and 'Crime' are not considered for prompts.
<br>
Characters portrayed by actors aged under 18 at the time of the movie or episode's release are excluded as standard.

# References
Actor and movie/TV data is sourced from [TheMovieDB API](https://www.themoviedb.org/documentation/api/terms-of-use).

# Suggestions
Please submit any suggestions to [@thegardendoor](https://twitter.com/thegardendoor) on Twitter or [captainss](https://captainss.tumblr.com/) on Tumblr.
