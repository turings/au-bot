# au-bot
A Twitter bot that generates AU prompts for fanfiction writers.

# Keywords

## ROLE
Use the ROLE keyword to generate role-based prompts.
<br>
<br>
For example:
<br>
`twitteruser: @au_bot Send me a sweet ROLE prompt, dude!`
<br>
`au_bot: @twitteruser Socialite/Tennis Coach`
<br>
Or
<br>
`au_bot: @twitteruser Violinist/Music Teacher`
<br>
<br>
Of course, one can't guarantee that all (or even most) of these prompts would have the same degree of congruity. You might get `Violinist/Tennis Coach`.

## CROSSOVER [Actor Name]/[Actor Name]
Use the CROSSOVER keyword to generate TV show/movie prompts.
<br>
<br>
For example:
<br>
`twitteruser: @au_bot CROSSOVER Joseph Mazzello/Rami Malek please?`
<br>
`au_bot: @twitteruser Dustin Moskovitz (The Social Network)/Elliot Alderson (Mr. Robot)`
<br>
Or, because zeitgeist:
<br>
`twitteruser: @au_bot CROSSOVER Jensen Ackles/Misha Collins if you’d be so kind`
<br>
`au_bot: @twitteruser C.J. (Dawson’s Creek)/Tony (Girl, Interrupted)`
<br>
<br>
(I haven’t seen Dawson’s Creek, so I have no idea whether the latter would make a good fic.)

# Content Filters

## Roles
Roles related to the trigger warnings listed [here](https://trigger-warnings.tumblr.com/tags) are excluded as standard, apart from:
<br>
Illness/injury (e.g., doctor)
<br>
Warfare (e.g., soldier)
<br>
Death (e.g., funeral director)
<br>
Using the keyword ROLE-SAFE in a request tweet excludes these roles too.

## Crossovers
Using the keyword CROSSOVER-SAFE in a request tweet excludes movies with the genres 'War', 'Horror' and 'Crime'.
<br>
Characters portrayed by actors aged under 21 at the time of the movie/episode release will be excluded as standard.

# References
Actor and movie/TV data from [TheMovieDB API](https://developers.themoviedb.org/)
