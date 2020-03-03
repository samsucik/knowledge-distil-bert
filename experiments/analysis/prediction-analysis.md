# Prediction analysis
## Questions/tasks to answer
### Individual models
- describe when the models fail and succeed (i.e. describe the hits/misses)
- describe the confidence of predictions: how confident is the model on average? and just on the mistakes?
- describe the confident/unconfident hits/misses of each individual student

### Comparing models (think about differences within one student)
- is one student generally more confident than the other?
- describe cases where one student is very confident and the other one is very unconfident
- describe cases where one student is right and the other is wrong
- what's the overlap of the 2 students' mistakes and which ones are unique to one student?

### Exploring knowledge distillation
- describe cases where teacher is confident but both students are unconfident
- describe cases where teacher is right but both students are wrong

### Overall
- what are the strengths/weaknesses of each student?

## Samples to look at
Find samples that:
- are predicted differently by different students (in terms of label)
- are predicted very confidently by some students but unconfidently by others

## SST-2
### Teacher
#### Confident mistakes
Samples with wrong or questionable labels: 
- `this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms .` (labelled negative).
- `moretti 's compelling anatomy of grief and the difficult process of adapting to loss .` (labelled negative)
- `it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-up , a terrific climax , and some nice chills along the way .` (labelled negative)
- `american chai encourages rueful laughter at stereotypes only an indian-american would recognize .` (labelled negative)
- ```while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer``` (labelled positive)
- `you wo n't like roger , but you will quickly recognize him .` (labelled negative)
- `the longer the movie goes , the worse it gets , but it 's actually pretty good in the first few minutes .` (labelled negative)

Confused by negative keywords: 
- `though it 's become almost >>redundant<< to say so , major kudos go to leigh for actually casting people who look working-class .`
- `as unseemly as its title suggests .`

Confused by positive keywords:
- Doesn't understand "anything but fun" as negative: `although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun .` (labelled negative)

#### Unconfident mistakes
Hard to explain:
- Maybe "hollow" and "despair" give negative feeling: `huston nails both the glad-handing and the choking sense of hollow despair .` (labelled positive)
- `the lion king was a roaring success when it was released eight years ago , but on imax it seems better , not just bigger .` (labelled positive)

Unclear labels:
- `it 's one of those baseball pictures where the hero is stoic , the wife is patient , the kids are as cute as all get-out and the odds against success are long enough to intimidate , but short enough to make a dream seem possible .` (labelled positive)
- `funny but perilously slight .` (labelled positive)
- `we root for ( clara and paul ) , even like them , though perhaps it 's an emotion closer to pity .` (labelled positive)
- `mcconaughey 's fun to watch , the dragons are okay , not much fire in the script .` (labelled positive)
- `good film , but very glum .` (labelled positive)

Uncommon words, metaphors:
- Also unclear label: `sam mendes has become >>valedictorian<< at the school for >>soft landings and easy ways out<< .` (labelled negative)
- `a great ensemble cast ca n't >>lift this heartfelt enterprise out of the familiar<< .` (labelled negative)

Common knowledge:
- need to understand what jabs are to get the positive description: `the jabs it employs are short , carefully placed and dead-center .` (labelled positive)

#### Confident hits
All labelled as positive and contain only neutral or positive words, the only exception being the word "strangely" in `a strangely compelling and brilliantly acted psychological drama .`.

#### Unconfident hits
Not strongly positive or negative:
- `in all , this is a watchable movie that 's not quite the memorable experience it might have been .` (negative)

Containing metaphors and similes that the model likely cannot pick up:
- `the socio-histo-political treatise is told >>in earnest strides<< ... ( and ) personal illusion is deconstructed with poignancy .` (positive)
- `in a way , the film >>feels like a breath of fresh air<< , but only to those that allow it in .` (positive)

Referring to domain knowledge the model can't have:
- `this time mr. burns is >>trying something in the martin scorsese street-realist mode<< , but his self-regarding sentimentality trips him up again .` (negative)
- `collateral damage finally >>delivers the goods for schwarzenegger fans<< .` (positive)

### LSTM
#### Confident mistakes
Samples with wrong or questionable labels: 
- `this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms .` (labelled negative).
- `moretti 's compelling anatomy of grief and the difficult process of adapting to loss .` (labelled negative)
- `it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-up , a terrific climax , and some nice chills along the way .` (labelled negative)
- `american chai encourages rueful laughter at stereotypes only an indian-american would recognize .` (labelled negative)
- `you wo n't like roger , but you will quickly recognize him .` (labelled negative)

Confused by negative keywords: 
- `though it 's become almost >>redundant<< to say so , major kudos go to leigh for actually casting people who look working-class .`
- `as unseemly as its title suggests .`
- ```if steven soderbergh 's ` solaris ' is a failure it is a glorious failure .```

Confused by positive keywords:
- Doesn't understand "anything but fun" as negative: `although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun .` (labelled negative)
- `all that 's missing is the spontaneity , originality and delight .` (labelled negative)

#### Unconfident mistakes
Hard to explain:
- Maybe "hollow" and "despair" give negative feeling: `huston nails both the glad-handing and the choking sense of hollow despair .` (labelled positive)
- `although german cooking does not come readily to mind when considering the world 's best cuisine , mostly martha could make deutchland a popular destination for hungry tourists .` (labelled positive)

Unclear labels:
- `verbinski implements every hack-artist trick to give us the ooky-spookies .` (labelled negative)
- `if you 've ever entertained the notion of doing what the title of this film implies , what sex with strangers actually shows may put you off the idea forever .` (labelled negative)
Confused by positive keywords:
- `i do n't think i laughed out loud once .` (labelled negative)
- `sustains its >>dreamlike glide<< through a succession of cheesy coincidences and voluptuous cheap effects , not the least of which is rebecca romijn-stamos .` (labelled negative)

Uncommon words, metaphors, similes:
- `in a way , the film >>feels like a breath of fresh air<< , but only to those that allow it in .` (labelled positive)
- `determined to be fun , and bouncy , with energetic musicals , the humor did n't quite engage this adult .` (labelled negative)
- also confused by negative keyword: `light years / several warp speeds / levels and levels of dilithium crystals better than the pitiful insurrection .` (labelled positive)

Common knowledge:
- need to understand that "full world" is positive: `a full world has been presented onscreen , not some series of carefully structured plot points building to a pat resolution .` (labelled positive)

#### Confident hits
All labelled as positive and contain only neutral or positive words.
#### Unconfident hits
Complicated sentence structure:
- `it 's hard to like a film about a guy who is utterly unlikeable , and shiner , starring michael caine as an aging british boxing promoter desperate for a taste of fame and fortune , is certainly that .` (negative)
- `whether you like rap music or loathe it , you ca n't deny either the tragic loss of two young men in the prime of their talent or the power of this movie .` (positive)

Tricky wordings:
- `if you 're hard up for raunchy college humor , >>this is your ticket right here<< .` (positive)
- `the story and the friendship proceeds in such a way that you 're watching a >>soap opera rather than a chronicle of the ups and downs that accompany lifelong friendships<< .` (negative)

Unclear labels:
- `funny but perilously slight .` (positive)
- `for anyone unfamiliar with pentacostal practices in general and theatrical phenomenon of hell houses in particular , it 's an eye-opener .` (positive)

Metaphors, similes:
- `it 's inoffensive , cheerful , built to inspire the young people , set to an unending soundtrack of beach party pop numbers and aside from its remarkable camerawork and awesome scenery , >>it 's about as exciting as a sunburn<< .` (negative)

Context knowledge:
- `the iditarod lasts for days - this just felt like it did .` (negative)
- need to understand that an insufferable character is a downside: `davis ... is so enamored of her own creation that she ca n't see how insufferable the character is .` (negative)
- `without non-stop techno or the existential overtones of a kieslowski morality tale , maelström is just another winter sleepers .` (negative)

### BERT
#### Confident mistakes
Wrong or questionable labels: 
- `this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms .` (labelled negative).
- `harrison 's flowers puts its heart in the right place , but its brains are in no particular place at all .` (labelled positive)
- `it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-up , a terrific climax , and some nice chills along the way .` (labelled negative)
- `you wo n't like roger , but you will quickly recognize him .` (labelled negative)

Confused by negative keywords: 
- `as unseemly as its title suggests .`

Confused by positive keywords:
- `outer-space buffs might love this film , but others will find its pleasures intermittent .` (labelled negative)
- Doesn't understand "anything but fun" as negative: `although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun .` (labelled negative)

Complicated wordings:
- `irwin is a man with enough charisma and audacity to carry a dozen films , but this particular result is ultimately held back from being something greater .` (labelled negative)
- "guffaw" and "diabolical" are quite tricky: `you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this .` (labelled negative)

Metaphors, similes:
- `it 's inoffensive , cheerful , built to inspire the young people , set to an unending soundtrack of beach party pop numbers and aside from its remarkable camerawork and awesome scenery , >>it 's about as exciting as a sunburn<< .` (labelled negative)

#### Unconfident mistakes
Tricky wordings:
- `if the movie succeeds in instilling a wary sense of ` there but for the grace of god , ' it is far too self-conscious to draw you deeply into its world .` (labelled negative)
- `even the >>finest chef ca n't make a hotdog into anything more than a hotdog<< , and robert de niro ca n't >>make this movie anything more than a trashy cop buddy comedy<< .` (labelled negative)
- `combining >>quick-cut editing and a blaring heavy metal<< much of the time , beck seems to be >>under the illusion that he 's shooting the latest system of a down video<< .` (labelled negative)
- here "doesn't bother" is actually positive: `( d ) oes n't bother being as cloying or preachy as equivalent evangelical christian movies -- maybe the filmmakers know that the likely audience will already be among the faithful .` (labelled positive)

Unclear labels:
- `mcconaughey 's fun to watch , the dragons are okay , not much fire in the script .` (labelled positive)
- `it moves quickly , adroitly , and without fuss ; it does n't give you time to reflect on the inanity -- and the cold war datedness -- of its premise .` (labelled positive)

Referring to domain knowledge the model can't have:
- `collateral damage finally >>delivers the goods for schwarzenegger fans<< .` (labelled positive)
- has to know that "PR hype is something negative": `that 's pure pr hype .` (labelled negative)

Metaphors, similes:
- `to say this was done better in wilder 's some like it hot is >>like saying the sun rises in the east<< .` (labelled negative)

Confused by positive keywords:
- `the only excitement comes when the credits finally roll and you get to leave the theater .` (labelled negative)

#### Confident hits
All labelled as positive and contain only neutral or positive words.
#### Unconfident hits
Context knowledge:
- need to know about the issues: `you will emerge with a clearer view of how the gears of justice grind on and the death report comes to share airtime alongside the farm report .` (positive)

Unclear label:
- is this irony? `the movie is n't just hilarious : it 's witty and inventive , too , and in hindsight , it is n't even all that dumb .` (positive)

Confusing negative keywords:
- `hilariously inept and ridiculous .` (positive)

Confusing negative words:
- `ramsay , as in ratcatcher , remains a filmmaker with an acid viewpoint and a real gift for teasing chilly poetry out of lives and settings that might otherwise seem drab and sordid .` (positive)

Tricky wordings:
- `manages to show life in all of its banality when the intention is quite the opposite .` (negative)
- probably unable to handle negations: `the film contains no good jokes , no good scenes , barely a moment when carvey 's saturday night live-honed mimicry rises above the level of embarrassment .` (negative)

Uncommon words, metaphors:
- `a great ensemble cast ca n't >>lift this heartfelt enterprise out of the familiar<< .` (labelled negative)
- `with its >>dogged hollywood naturalism and the inexorable passage of its characters toward sainthood<< , windtalkers is nothing but >>a sticky-sweet soap<< .` (negative)
- unknown words: `bogdanovich tantalizes by offering a peep show into the lives of the era 's creme de la celluloid .` (positive)
- `it showcases carvey 's talent for voices , but >>not nearly enough<< and >>not without taxing every drop of one 's patience to get to the good stuff<< .` (negative)