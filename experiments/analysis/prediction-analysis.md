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
- `this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms .` (neg).
- `moretti 's compelling anatomy of grief and the difficult process of adapting to loss .` (neg)
- `it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-up , a terrific climax , and some nice chills along the way .` (neg)
- `american chai encourages rueful laughter at stereotypes only an indian-american would recognize .` (neg)
- ```while there 's something intrinsically funny about sir anthony hopkins saying ` get in the car , bitch , ' this jerry bruckheimer production has little else to offer``` (pos)
- `you wo n't like roger , but you will quickly recognize him .` (neg)
- `the longer the movie goes , the worse it gets , but it 's actually pretty good in the first few minutes .` (neg)

Confused by negative keywords: 
- `though it 's become almost >>redundant<< to say so , major kudos go to leigh for actually casting people who look working-class .` (pos)
- `as unseemly as its title suggests .` (pos)

Confused by positive keywords:
- Doesn't understand "anything but fun" as negative: `although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun .` (neg)

#### Unconfident mistakes
Hard to explain:
- Maybe "hollow" and "despair" give negative feeling: `huston nails both the glad-handing and the choking sense of hollow despair .` (pos)
- `the lion king was a roaring success when it was released eight years ago , but on imax it seems better , not just bigger .` (pos)

Unclear labels:
- `it 's one of those baseball pictures where the hero is stoic , the wife is patient , the kids are as cute as all get-out and the odds against success are long enough to intimidate , but short enough to make a dream seem possible .` (pos)
- `funny but perilously slight .` (pos)
- `we root for ( clara and paul ) , even like them , though perhaps it 's an emotion closer to pity .` (pos)
- `mcconaughey 's fun to watch , the dragons are okay , not much fire in the script .` (pos)
- `good film , but very glum .` (pos)

Uncommon words, metaphors:
- Also unclear label: `sam mendes has become >>valedictorian<< at the school for >>soft landings and easy ways out<< .` (neg)
- `a great ensemble cast ca n't >>lift this heartfelt enterprise out of the familiar<< .` (neg)

Common knowledge:
- need to understand what jabs are to get the positive description: `the jabs it employs are short , carefully placed and dead-center .` (pos)

#### Confident hits
All labelled as positive and contain only neutral or positive words, the only exception being the word "strangely" in `a strangely compelling and brilliantly acted psychological drama .`.

#### Unconfident hits
Not strongly positive or negative:
- `in all , this is a watchable movie that 's not quite the memorable experience it might have been .` (neg)
- `something akin to a japanese alice through the looking glass , except that it seems to take itself far more seriously .` (pos)

Containing metaphors and similes that the model likely cannot pick up:
- `the socio-histo-political treatise is told >>in earnest strides<< ... ( and ) personal illusion is deconstructed with poignancy .` (pos)
- `in a way , the film >>feels like a breath of fresh air<< , but only to those that allow it in .` (pos)
- `light years / several warp speeds / levels and levels of dilithium crystals better than the pitiful insurrection .` (pos)
- `very special effects , brilliantly bold colors and heightened reality ca n't hide the giant achilles ' heel in `` stuart little 2 `` : there 's just no story , folks .` (neg)
- `to say this was done better in wilder 's some like it hot is like saying the sun rises in the east .` (neg)

Referring to domain knowledge the model can't have:
- `this time mr. burns is >>trying something in the martin scorsese street-realist mode<< , but his self-regarding sentimentality trips him up again .` (neg)
- `collateral damage finally >>delivers the goods for schwarzenegger fans<< .` (pos)

### LSTM
#### Confident mistakes
Samples with wrong or questionable labels: 
- `this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms .` (neg).
- `moretti 's compelling anatomy of grief and the difficult process of adapting to loss .` (neg)
- `it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-up , a terrific climax , and some nice chills along the way .` (neg)
- `american chai encourages rueful laughter at stereotypes only an indian-american would recognize .` (neg)
- `you wo n't like roger , but you will quickly recognize him .` (neg)

Confused by negative keywords: 
- `though it 's become almost >>redundant<< to say so , major kudos go to leigh for actually casting people who look working-class .` (pos)
- `as unseemly as its title suggests .` (pos)
- ```if steven soderbergh 's ` solaris ' is a failure it is a glorious failure .``` (pos)

Confused by positive keywords:
- Doesn't understand "anything but fun" as negative: `although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun .` (neg)
- `all that 's missing is the spontaneity , originality and delight .` (neg)

#### Unconfident mistakes
Hard to explain:
- Maybe "hollow" and "despair" give negative feeling: `huston nails both the glad-handing and the choking sense of hollow despair .` (pos)
- `although german cooking does not come readily to mind when considering the world 's best cuisine , mostly martha could make deutchland a popular destination for hungry tourists .` (pos)

Unclear labels:
- `verbinski implements every hack-artist trick to give us the ooky-spookies .` (neg)
- `if you 've ever entertained the notion of doing what the title of this film implies , what sex with strangers actually shows may put you off the idea forever .` (neg)

Confused by positive keywords:
- `i do n't think i laughed out loud once .` (neg)
- `sustains its >>dreamlike glide<< through a succession of cheesy coincidences and voluptuous cheap effects , not the least of which is rebecca romijn-stamos .` (neg)

Uncommon words, metaphors, similes:
- `in a way , the film >>feels like a breath of fresh air<< , but only to those that allow it in .` (pos)
- `determined to be fun , and bouncy , with energetic musicals , the humor did n't quite engage this adult .` (neg)
- also confused by negative keyword: `light years / several warp speeds / levels and levels of dilithium crystals better than the pitiful insurrection .` (pos)

Common knowledge:
- need to understand that "full world" is positive: `a full world has been presented onscreen , not some series of carefully structured plot points building to a pat resolution .` (pos)

#### Confident hits
All labelled as positive and contain only neutral or positive words.

#### Unconfident hits
Complicated sentence structure:
- `it 's hard to like a film about a guy who is utterly unlikeable , and shiner , starring michael caine as an aging british boxing promoter desperate for a taste of fame and fortune , is certainly that .` (neg)
- `whether you like rap music or loathe it , you ca n't deny either the tragic loss of two young men in the prime of their talent or the power of this movie .` (pos)

Tricky wordings:
- `if you 're hard up for raunchy college humor , >>this is your ticket right here<< .` (pos)
- `the story and the friendship proceeds in such a way that you 're watching a >>soap opera rather than a chronicle of the ups and downs that accompany lifelong friendships<< .` (neg)

Unclear labels:
- `funny but perilously slight .` (pos)
- `for anyone unfamiliar with pentacostal practices in general and theatrical phenomenon of hell houses in particular , it 's an eye-opener .` (pos)

Metaphors, similes:
- `it 's inoffensive , cheerful , built to inspire the young people , set to an unending soundtrack of beach party pop numbers and aside from its remarkable camerawork and awesome scenery , >>it 's about as exciting as a sunburn<< .` (neg)

Context knowledge:
- `the iditarod lasts for days - this just felt like it did .` (neg)
- need to understand that an insufferable character is a downside: `davis ... is so enamored of her own creation that she ca n't see how insufferable the character is .` (neg)
- also tricky sentence structure: `without non-stop techno or the existential overtones of a kieslowski morality tale , maelström is just another winter sleepers .` (neg)

### BERT
#### Confident mistakes
Wrong or questionable labels: 
- `this riveting world war ii moral suspense story deals with the shadow side of american culture : racial prejudice in its ugly and diverse forms .` (neg).
- `harrison 's flowers puts its heart in the right place , but its brains are in no particular place at all .` (pos)
- `it 's somewhat clumsy and too lethargically paced -- but its story about a mysterious creature with psychic abilities offers a solid build-up , a terrific climax , and some nice chills along the way .` (neg)
- `you wo n't like roger , but you will quickly recognize him .` (neg)

Confused by negative keywords: 
- `as unseemly as its title suggests .` (pos)

Confused by positive keywords:
- `outer-space buffs might love this film , but others will find its pleasures intermittent .` (neg)
- Doesn't understand "anything but fun" as negative: `although huppert 's intensity and focus has a raw exhilaration about it , the piano teacher is anything but fun .` (neg)

Complicated wordings:
- `irwin is a man with enough charisma and audacity to carry a dozen films , but this particular result is ultimately held back from being something greater .` (neg)
- "guffaw" and "diabolical" are quite tricky: `you really have to wonder how on earth anyone , anywhere could have thought they 'd make audiences guffaw with a script as utterly diabolical as this .` (neg)

Metaphors, similes:
- `it 's inoffensive , cheerful , built to inspire the young people , set to an unending soundtrack of beach party pop numbers and aside from its remarkable camerawork and awesome scenery , >>it 's about as exciting as a sunburn<< .` (neg)

#### Unconfident mistakes
Tricky wordings:
- `if the movie succeeds in instilling a wary sense of " there but for the grace of god , ' it is far too self-conscious to draw you deeply into its world .` (neg)
- `even the >>finest chef ca n't make a hotdog into anything more than a hotdog<< , and robert de niro ca n't >>make this movie anything more than a trashy cop buddy comedy<< .` (neg)
- `combining >>quick-cut editing and a blaring heavy metal<< much of the time , beck seems to be >>under the illusion that he 's shooting the latest system of a down video<< .` (neg)
- here "doesn't bother" is actually positive: `( d ) oes n't bother being as cloying or preachy as equivalent evangelical christian movies -- maybe the filmmakers know that the likely audience will already be among the faithful .` (pos)

Unclear labels:
- `mcconaughey 's fun to watch , the dragons are okay , not much fire in the script .` (pos)
- `it moves quickly , adroitly , and without fuss ; it does n't give you time to reflect on the inanity -- and the cold war datedness -- of its premise .` (pos)

Referring to domain knowledge the model can't have:
- `collateral damage finally >>delivers the goods for schwarzenegger fans<< .` (pos)
- has to know that "PR hype is something negative": `that 's pure pr hype .` (neg)

Metaphors, similes:
- `to say this was done better in wilder 's some like it hot is >>like saying the sun rises in the east<< .` (neg)

Confused by positive keywords:
- `the only excitement comes when the credits finally roll and you get to leave the theater .` (neg)

#### Confident hits
All labelled as positive and contain only neutral or positive words.
#### Unconfident hits
Context knowledge:
- need to know about the issues: `you will emerge with a clearer view of how the gears of justice grind on and the death report comes to share airtime alongside the farm report .` (pos)

Unclear label:
- is this irony? `the movie is n't just hilarious : it 's witty and inventive , too , and in hindsight , it is n't even all that dumb .` (pos)

Confusing negative keywords:
- `hilariously inept and ridiculous .` (pos)

Confusing negative words:
- `ramsay , as in ratcatcher , remains a filmmaker with an acid viewpoint and a real gift for teasing chilly poetry out of lives and settings that might otherwise seem drab and sordid .` (pos)

Tricky wordings:
- `manages to show life in all of its banality when the intention is quite the opposite .` (neg)
- probably unable to handle negations: `the film contains no good jokes , no good scenes , barely a moment when carvey 's saturday night live-honed mimicry rises above the level of embarrassment .` (neg)

Uncommon words, metaphors:
- `a great ensemble cast ca n't >>lift this heartfelt enterprise out of the familiar<< .` (neg)
- `with its >>dogged hollywood naturalism and the inexorable passage of its characters toward sainthood<< , windtalkers is nothing but >>a sticky-sweet soap<< .` (neg)
- unknown words: `bogdanovich tantalizes by offering a peep show into the lives of the era 's creme de la celluloid .` (pos)
- `it showcases carvey 's talent for voices , but >>not nearly enough<< and >>not without taxing every drop of one 's patience to get to the good stuff<< .` (neg)

### Cases where one student is very confident and the other one is very unconfident
Mixed examples. The teacher is mostly right, but below average. INTERESTING: Teacher is quite unconfident when BERT is unconfident, and much more confident when LSTM is unconfident.

The sentences are mostly long, with tricky sentence structures and wordings, lots of similes and metaphors, domain knowledge often required too, and even with unclear labels.

When LSTM is unconfident and BERT is confident, there are no clear patterns:
- lstm careful (correct), BERT confident (correct):  	2x    
- lstm careful (incorrect), BERT confident (incorrect): 2x 
- lstm careful (incorrect), BERT confident (correct):   3x
- lstm careful (correct), BERT confident (incorrect):   3x

When BERT is unconfident and LSTM is confident, there are no clear patterns but BERT is mostly correct (however unconfident):
- BERT careful (incorrect), LSTM confident (incorrect): 1x
- BERT careful (correct), LSTM confident (correct):     4x
- BERT careful (incorrect), LSTM confident (correct):   2x
- BERT careful (correct), LSTM confident (incorrect):   3x

### Cases where one student is right and the other is wrong (teacher being right)
Mostly long sentences, mixed labels. The teacher always correct, but often unconfident. Almost exclusively, LSTM is predicting negative while BERT is predicting positive. In most cases, one student is much less confident than the other (often, the incorrect prediction is unconfident).

### Overlap of the 2 students' hits/misses
Surprisingly many mistakes are model-specific! Almost 1/3 of LSTM's mistakes are LSTM-specific, and over 40% are specific for BERT.

### Cases where teacher is confident but both students are unconfident
Mixed examples, predicted (mostly) correctly by teacher, mixed correctness of students. Long sentences, often tricky. Unclear patterns.

### Cases where teacher is right but both students are wrong
These are mostly negative sentences, with the teacher and students being mostly unconfident.

The sentences are often long, unclear, tricky, with domain knowledge needed or with metaphors.


## CoLA
### Teacher
#### Confident mistakes
*All* are unacc predicted as acc.
Many are based on verbal properties, i.e. a specific verb taking specific args. Hence, many of the sentences would've been OK if the verb was replaced by a different one. So, this is also a semantic issue. (S)

Word order:
- mary beautifully plays the violin. (adverb position) (S)

Long-range dep.
- which house does your friend live? (missing prep.) (S)
- jack is the person with whom jenny fell in love with. (repeated prep.)
- she was bathing, but i couldn't make out who. (intransitive with illegal argument) (V)
- sally asked if somebody was going to fail math class, but i can't remember who. (quantifier)
- that the cops spoke to the janitor about it yesterday is terrible, that robbery. (clause reordering illegal here, long-range thing)

Missing prep.
- Mary intended John to go abroad (S)

Inserted expletive
- john believes it sincerely that bill is here.

Bad labels?
- it has been determined that somebody will be appointed; it's just not clear yet who.
- sandy was trying to work out which students would be able to solve a certain problem, but she wouldn't tell us which one.

#### Unconfident mistakes
Tricky accs
- i am both expecting to get the job and of the opinion that it is a desirable one. (acc)
- john, told mary that it would be appropriate to leave together. (CP, complex argument) (acc)
- we recommend to eat less cake and pastry. (to-VP less typical than gerund) (acc)

Tricky unaccs
- i enjoy yourself. ('i' makes the reflexive illegal) (unacc)
- john likes some students, but i don't know who john likes some students. (long-range issue) (unacc)
- the book of poems and from blackwell takes a very long time to read. (inserted conjunction) (unacc)

Illegal word order
- which topic did you get bored because mary talked about? (bad question forming) (acc)
- mickey looked up it. (unacc)

Semantic violation
- the bookcase ran (unacc)
- we appeared to them to vote for themselves. ("appealed" would've been OK) (unacc)

#### Confident hits
**All accs** and mostly simple sentences (SVO) such as "the witch poisoned the children.".

Not entirely trivial examples:
- i believe there to be no way out.
- i would prefer for john to leave. 
- chris was handed a note.
- that is the reason why he resigned.

#### Unconfident hits
Tricky examples
- neither of students failed. (missing determiner) (unacc)
- max seemed to be trying to force ted to leave the room, and walt, ira. (deep structure) (acc)
- the book was by john written. (word order) (unacc)
- who who you like does sandy also like? (acc)
- which girl did mike quip never wore this hat? (verb "quip" doesn't permit moving elements out of the CP, some other verbs would) (unacc)
- mary asked me if, in st. louis, john could rent a house cheap. (parenthesis) (acc)
- i read some of the book. (acc)

Binding
- ourselves like ourselves. (unacc)

Miscellaneous
- carla slid the book. (unusual word?) (acc)
- you must pick any flower you see. (seems easy) (acc)

### LSTM
#### Confident mistakes
*All* are unacc predicted as acc. Interesting are binding cases and cases with illegal/missing prepositions. Doesn't really struggle with long-range deps.

Binding
- protect you!
- wash you!
- kick you!

Semantic violation
- chocolate eggs were hidden from each other by the children. (would be fine with different verb, not "hidden", or with different clause order)
- mary wonders that bill will come. (would be fine with "thinks")
- the jeweller scribbled the contract with his name. ("decorated the ring with his name" would be ok)
- no one can forgive that comment to you. (word order; would be ok with "give")

Relational adjectives
- the children are fond that they have ice cream. (required preposition "of" not used, would be ok with "happy" instead of "fond")

Miscellanous
- bill must quickly eat the peaches, and harry must slowly. (anaphor, long-range issue ("too" would be ok instad of "slowly"))
- sophie will theater. (kinda semantic -- the specific verb doesn't permit NP object)

#### Unconfident mistakes
Tricky accs
- clearly, john probably will immediately learn french perfectly. (multiple adverbs) (acc)
- everybody around here who ever buys anything on credit talks in his sleep. (just a tricky sentence?) (acc)
- bill's story about sue and max's about kathy both amazed me. (complex subject) (acc)
- extremely frantically, anson danced at trade (tricky word order -- sentence-level adjunct) (acc)
- the bucket was kicked by pat. (unusual passive) (acc)

Long-range deps
- the table was wiped by john clean. (wrong argument order; the resultative "clean" makes it illegal) (unacc)

Ungrammatical
- the soundly and furry cat slept. (adverb used as adjective) (unacc)

Word order
- there presented itself a wonderful opportunity yesterday. (scrambled) (unacc)

Semantic violation
- john whispered mary left. (would be ok with "thought" but now "that" is compulsory) (unacc)\
- john heard that they criticized themselves. (weird sentence, maybe "him" was the desired word?) (unacc)

#### Confident hits
**All accs**. Some simple sentences (susan told her a story.) and some a bit less typical (i.e. not simple SVO):
- you will believe bob.
- john told mary that it was important to fred to leave early.
- john told mary that it would be important to leave early.
- those pictures of us offended us.

#### Unconfident hits
Binding
- us like them. (unacc)

Tricky examples
- in which way is clinton anxious to find out which budget dilemmas panetta would be willing to solve? (really tricky!) (unacc)
- the correspondence school sent bill a good typist. (really tricky!) (acc)
- the committee knows whose efforts to achieve peace the world should honor. (really tricky) (acc)
- gould's performance of bach on the piano doesn't please me anywhere as much as ross's on the harpsichord. (long-range, and still tricky; anaphor) (unacc)
- i like bill's yellow shirt, but not max's. (gapping -- deletion) (acc)
- jones, that we were talking to last night, always watches football games alone. (kinda semantic; would work fine with "the guy" instead of "jones") (unacc)

Ungrammatical
- the cat were bitten by the dog. (unacc)
- wind was gotten of a plot to negotiate an honorable end to the war in vietnam. (scrambled; original: A plan to negotiate an honorable end to the war in Vietnam was gotten wind of.) (unacc)

Rare words?
- a magazine about crime appeared on the newsstands. (simple but has the unusual "newsstands") (acc)

### BERT
#### Confident mistakes
*All* are unacc predicted as acc. Semantic issues labelled as (S)

Extra/illegal words
- chris was handed sandy a note. (mid-range dep)
- it is the problem that he is here. (wrong determiner, long-range dep)
- everyone hopes everyone to sleep. (tricky; illegal only because the two words are the same!) (S)
- jack is the person with whom jenny fell in love with. (repeated prep.)
- did the child be in the school? (long-range dep; would be fine with "was" instead o "did be") (S)
- john paid me against the book. (tricky, would be fine with "for") (S)
- sophie will theater. (kinda semantic -- the specific verb doesn't permit NP object) (S)

Word order
- mary beautifully plays the violin. (adverb position) (S)

Missing prep.
- Mary intended John to go abroad (S)

Binding
- we gave us presents. (incorrect dative, mid-range dep)

#### Unconfident mistakes
Tricky examples
- max seemed to be trying to force ted to leave the room, and walt, ira. (deep structure) (acc)
- john decided for bill to get the prize. ("it was decided" would be fine; long-range dep) (unacc)
- they were interested in his. (unnatural sentence ending) (acc)
- most columnists claim that a senior white house official has been briefing them, and the newspaper today reveals which one. (long-range dep) (acc)

Word order
- blue leather shows herself that betsy is pretty. (scrambled) (unacc)
- with no job would john be happy. (unusual order, dislocation) (acc)

Illegal word/word form
- dana walking and leslie ran. (coordination, lonng-range dep) (unacc)
- brian threw the fence with the stick. ("throw" doesn't fit, "hit" would be fine) (S) (unacc)
- john was struck as sick. (would be fine with "treated", etc.; originally "Bill strikes John as sick.") (S) (unacc)

Miscellaneous
- they chased the man with the car. (should be easy) (acc)

#### Confident hits
**All accs**. Surprisingly few simple sentences (the witch poisoned the children., john tries to leave the country.), others are a bit more complex:
- that dogs bark annoys people. 
- everyone hoped that she would sing.
- john wants not to leave the town. 
- phillip gave the medal to the soldier.

#### Unconfident hits
Tricky examples
- books were taken from no student and given to mary. (acc)
- most columnists claim that a senior white house official has been briefing them, but none will reveal which one. (tricky, long-range dep) (acc)
- tom's dog with one eye attacked frank's with three legs. (illegal omission) (unacc)
- john gave bill the dog dead. (rare word order) (acc)

Extra/wrong word
- john believed it that bill was tardy. (extra expletive; short-range dep) (unacc)
- we talked to them about there. (wrong expletive; should be "it") (unacc)

Semantic violation
- paperback books lift onto the table easily. ("fall" would be fine; original "I lifted the paperback book onto the table") (S) (unacc)
- i gave pete the book to impress. (would be fine with "read") (S) (unacc)

Miscellaneous
- i sensed his eagerness. (should be easy; maybe rare words?) (acc)
- there is believed to be sheep in the park. (weird, sounds acceptable) (unacc)

### Cases where one student is very confident and the other one is very unconfident
In most of these cases, the teacher is also quite unconfident or even wrong. It's very difficult to spot patterns in the sentences (describe what they've got in common).

When LSTM is unconfident and BERT is confident, it's mostly:
- lstm careful (correct), BERT confident (correct):      5x
- lstm careful (incorrect), BERT confident (incorrect):  3x
- rest (2x): lstm careful (incorrect), BERT confident (correct), OR lstm careful (correct), BERT confident (incorrect)

When BERT is unconfident and LSTM is confident, it's mostly:
- BERT careful (incorrect), LSTM confident (incorrect): 3x
- BERT careful (correct), LSTM confident (correct):     3x
- BERT careful (incorrect), LSTM confident (correct):   3x
- BERT careful (correct), LSTM confident (incorrect):   1x

### Cases where one student is right and the other is wrong (teacher being right)
Hard to interpret and draw conclusions. Generally, many long sentences appear here. Also, in most cases the teacher is below-average confident and one or both students are very unconfident as well (sometimes the correct one, sometimes the incorrect one, and in ~50% cases both).

### Overlap of the 2 students' hits/misses
Surprisingly many mistakes are model-specific! Over 40% of each model's mistakes are made only by that model and the other model gets those right.

### Cases where teacher is confident but both students are unconfident
Most of these are really tricky sentences, mostly acceptable, and mostly predicted correctly but unconfidently by the teacher, with mixed correctness of students. Basically, hard cases that the teacher barely handles and the students are either just very unconfident or even incorrect.

Tricky examples:
- most columnists claim that a senior white house official has been briefing them, but none will reveal which one.  
- clearly, john probably will immediately learn french perfectly.
- bill's story about sue and max's about kathy both amazed me.

The two unacceptable examples (which the teacher got wrong):
- the cat were bitten by the dog. (morphology) (unacc)
- jones, that we were talking to last night, always watches football games alone. (long-range issue) (unacc)

### Cases where teacher is right but both students are wrong
These are long sentences:
- neither von karajan's recording of beethoven's 6th on columbia nor klemperer's has the right tempo. (acc)
- if the ants were called elephants and elephants ants, i'd be able to squash an elephant. (acc)
- bill's wine from france and ted's from california cannot be compared. (acc)

as well as sentences that are problematic only semantically:
- my heart is pounding me. (unacc)
- leslie told us about us. (unacc)
- the tube was escaped by gas. (unacc)

but also other short ungrammatical cases:
- the children are fond with the ice cream. (requires knowledge of the specific verb and its prepositions) (unacc)
- the table was wiped by john clean. (long-range deps) (unacc)

In most cases, the teacher is right but unconfident. These are difficult sentences and the students, sometimes very confidently, make mistakes on them -- possibly due to their length and complexity, and due to missing semantic knowledge needed to detect ungrammaticality.

### Mistake type analysis (CoLA only)
On simple sentences, students roughly match the teacher, it's the harder cases where students start making mistakes.

Differences were considered only where there's ~100 or more examples in the category.

#### BERT better:
In general, confidence of students and teacher on most of these is low.
- adjunct (major), not consistently across minor categories
- binding (major), consistently across minor categories (SCRAP)
- VP adjunct    (maj: adjunct): mostly acceptable sentences, mostly correctly predicted by teacher. in many cases, quite long sentences with long-range deps. various examples, from `i gave pete the book to impress.` to `joan ate dinner with someone but i don't know who with.` to `the bed was slept in.`.
- Misc adjunct  (maj: adjunct): mostly acceptable sentences, mostly correctly predicted by teacher. in many cases, quite long sentences with long-range deps. various examples, from `he left the train with somebody else's wallet in his pocket.` to `mary asked me if, in st. louis, john could rent a house cheap.` to `i presented it to bill to read.`
- Oblique   (SCRAP)    (maj: arg types): mixed examples, often short, mostly correctly predicted by teacher. examples range from semantically tricky `lou hoped the umbrella in the closet.`, `sam offered the ball out of the basket.`, `mary revealed himself to john.` to relatively easy ones `martha carved the baby a toy out of wood.`, `john left us orders to follow pete.`
- PP Arg-VP  (SCRAP)   (maj: arg types): mostly acceptable sentences, mostly long, mostly correctly predicted by teacher. includes sentences that are long and/or with atypical ordering: `she said she had spoken to everybody, but he wasn't sure who.`, `he attributed to a short circuit which was caused by an overloaded transducer the fire which destroyed most of my factory.`, `the ta's have been arguing about whether some student or other should pass, but i can't now remember which one.`, `it was to john that i gave the book.`.
- high arity  (SCRAP)  (maj: arg altern): mostly acceptable sentences, mostly medium/short, sometimes incorrectly predicted even by teacher. tricky sentences like `we gave presents to ourselves.`, `john regretted it that bill had a good time.`, `i presented it to bill to read.`, `clinton is anxious to find out which budget dilemmas panetta would be willing to tackle in a certain way, but he won't say in which.`
- Add Arg   (SCRAP)    (maj: arg altern): mixed examples, often medium/short, mostly correctly predicted by teacher. various examples: `john believes it sincerely that bill is here.`, `there is a seat available.`, `there presented itself a wonderful opportunity yesterday.`, `i squeaked the door.`

#### LSTM better:
In general, confidence of students and teacher on most of these is low.
- predicate (major), mostly due to copula, really
- determiner (major), mostly due to quantifier, really (SCRAP)
- Comp Clause (major) (NEW)
- copula        (maj: pred): unacceptable sentences which the teacher predicts mostly correctly. issues often related to word/clause order: `i wonder what to be a clown on the cover of.`, `because she's so pleasant, as for mary i really like her.`, `that john is reluctant seems.`, `` 
- temporal (only ~40 examples though)
- passive       (maj: arg altern): unacceptable sentences, mixed success of teacher: `the paper was written by john up.`, `chris was handed sandy a note.`, `a pound was weighed by the book.`, etc.
- Compx NP      (maj: N, Adj): mixed examples, mostly correctly predicted by teacher, often with long-range deps: `jack is the person with whom jenny fell in love with.`, `the only person whose kids dana is willing to put up with is pat.`, `i dislike the people in who we placed our trust.`, etc.
- CP Arg VP
- Control (only ~80 examples though)
- quantifier (SCRAP) (maj: determiner): mixed examples, mostly correctly predicted by teacher, often with long-range deps: `it has been determined that somebody will be appointed; it's just not clear yet who.`, `we wanted to invite someone, but we couldn't decide who to.`, `most people probably consider, even though the courts didn't actually find, klaus guilty of murder.`, `the newspaper has reported that they are about to appoint someone, but i can't remember who the newspaper has reported that they are about to appoint.`, etc



## Sara
### Teacher
#### Confident mistakes
Most cases (7/10) are unrecognised utts defaulting to enter_data, e.g. `thx` (thank) or `i'm not sure` (deny).

Also: close intent pairs (`i want to learn something about rasa` (t:ask_whatisrasa, p:how_to_get_started)), questionable labels (`ok let's start` (t:affirm, p:how_to_get_started))

#### Unconfident mistakes
out_of_scope mistaken for more specific intents:
- `i want to know current situtation in pakistan` (ask_wherefrom)
- `what is evolution ?` (nlu_info)
- `oh my god, not again!` (canthelp)

confusing intent pairs:
- `what should i work on?` (t:ask_how_contribute, p:how_to_get_started)
- `recommend me some nlu tools` (t:nlu_generation_tool_recommendation, p:technical_question)

really fuzzy utts:
- `places` (t:enter_data, p:out_of_scope)
- `come stai?` (t:ask_howdoing, p:out_of_scope)

miscellaneous:
- `i would just like to have the link for the community` (t:ask_faq_what_is_forum, p:signup_newsletter)

#### Confident hits
Everything is enter_data. 5 cases contain the clear `__email_address__` token, the other 5 are not really identifiable with any other intent. Especially utts like `software developer` are very clearly typical answers to some question that asks for data about the person. Interesting how teacher picks up the long `__email_address__` token while students (mainly LSTM) focus more on the shorter tokens like language names.

#### Unconfident hits
These are mostly unusual examples of the particular intents, e.g. they don't contain the usual keywords.
- `what do you do as a company?` (ask_whatisrasa)
- `u are?` (ask_whoisit)
- `please provide information on your enterprise package` (contact_sales)
- `i want to put some of my effort in.` (ask_how_contribute)

There are also some out_of_scope examples, which are really just varied a lot: `what is todays date`, `what's your wife doing this weekend`

### LSTM
#### Confident mistakes
Getting confused by keywords characteristic of a particular (incorrect) intent:
- "learn": `how do you learn` (t:out_of_scope, p:how_to_get_started)
- "languages": `how many languages does spacy support?` (t:out_of_scope, p:ask_faq_languages)
- "start": `ok let's start` (t:affirm, p:how_to_get_started)

Similar intents:
- `toodle-oo` (t:bye, p:greet)

Defaulting to out_of_scope (long utts) and enter_data (short utts) where text is kind of random:
- `i am an opioid addict` (t:out_of_scope, p:enter_data)
- `chatfuel` (t:switch, p:enter_data)
- `i am qq` (t:out_of_scope, p:enter_data)
- `how many candles were on your last birthday cake?` (t:ask_howold, p:out_of_scope)
- `wit` (t:switch, p:enter_data)
- `i want to know how can buld my own bot` (t:how_to_get_started, p:out_of_scope)

#### Unconfident mistakes
Getting confused by keywords characteristic of a particular (incorrect) intent:
- "doesn't" or maybe just any negation: `that doesn't sound like a joke` (t:out_of_scope, p:deny)
- `places` (t:enter_data, p:ask_restaurant)
- "rasa": `what is the last version of rasa core?` (t:technical_question, p:ask_whatisrasa)
- "python": `how can i install python` (t:install_rasa, p:ask_faq_python_version)

Similar intents:
- `you originated through what means?` (t:ask_howbuilt, p:ask_whatisrasa)
- `what is your job?` (t:ask_whoisit, p:ask_builder)

Unusual wordings default to out_of_scope:
- `tell me what's your skill` (t:ask_whatspossible, p:out_of_scope)
- `are there also humans working for your company?` (t:human_handoff, p:out_of_scope)

Miscellaneous:
- `i would just like to have the link for the community` (t:ask_faq_what_is_forum, p:signup_newsletter)
- `what is evolution ?` (t:out_of_scope, p:technical_question)

#### Confident hits
Basically everything is enter_data and 100% confidence. Interesting how the wordpiece model learns keywords.

Keyword based:
- "german": `language = german` (enter_data)
- "english": `language: english` (enter_data)
- "french": `language = french` (enter_data)
- "hello": `rasa hello` (greet)
- "english": `it’s only in english but i plan to train it in other languages` (enter_data)
- "mandarin": `it’s only in mandarin but i plan to train it in other languages` (enter_data)
- "bot", "insurance": `i want to build a health insurance bot` (enter_data)
- "spanish": `the bot speaks spanish` (enter_data)
- "bot": `a wolf bot` (enter_data)
- "work": `i work for stanford university` (enter_data)

#### Unconfident hits
Mixed examples.

The broad out_of_scope and enter_data intents (may be uncertain because of probability attracted by various other intents):
- `i want to know current situtation in pakistan` (out_of_scope)
- `some thing else` (out_of_scope)
- `that link doesn't work!` (out_of_scope)
- `my budget is oov` (enter_data)
- `able to integrate with paypal, wordpress, facebook andd twilio` (enter_data)

Unusual examples (in particular, without the usual keywords):
- `i want to put some of my effort in.` (ask_how_contribute)
- `why help rasa's organization?` (ask_why_contribute)
- `get the latest news from rasa` (signup_newsletter)
- `what i a good pipeline to start with?` (pipeline_recommendation)
- `i decline` (deny) THIS ONE is interesting because "decline" isn't in the training data, so it has to be pulled from the embedding knowledge

### BERT
#### Confident mistakes
Unrecognised words default to biggest intent:
- `i am an opioid addict` (t:out_of_scope, p:enter_data)
- `wit` (t:switch, p:enter_data)
- `weatger` (t:ask_weather, p:enter_data)
- `cya` (t:bye, p:enter_data)
- `chatfuel` (t:switch, p:enter_data)

Getting confused by keywords:
- "start": `ok let's start` (t:affirm, p:how_to_get_started)
- "learn": `how do you learn` (t:out_of_scope, p:how_to_get_started)
- "sales": `sales bot` (t:enter_data, p:contact_sales)
- "languages": `how many languages does spacy support?` (t:out_of_scope, p:ask_faq_languages)

out_of_scope taking long phrases with recognised words?
- `how many candles were on your last birthday cake?` (t:ask_howold, p:out_of_scope)

#### Unconfident mistakes
Unusual phrasings/wordings (without keywords):
- `who went through the trouble of setting you up?` (t:ask_builder, p:technical_question)
- `what citizenship do you lay claim to?` (t:ask_wherefrom, p:nlu_info)
- `what is your job?` (t:ask_whoisit, p:ask_builder)
- `i want to put some of my effort in.` (t:ask_how_contribute, p:out_of_scope)
- `i decline` (t:deny, p:out_of_scope)
- `what do you do as a company?` (t:ask_whatisrasa, p:out_of_scope)
- missing keyword: `are you bilingual?` (t:ask_languagesbot, p:out_of_scope)

Keywords typical for different intent:
- "today": `what is todays date` (t:out_of_scope, p:ask_weather)

Miscellaneous:
- `get me a club mate` (t:out_of_scope, p:human_handoff)
- `i would just like to have the link for the community` (t:ask_faq_what_is_forum, p:signup_newsletter)

#### Confident hits
Everything enter_data. Keywords:
- "italian": `the assistant speaks italian` (enter_data)
- "spanish": `it’s trained only in spanish` (enter_data)
- "english": `the assistant speaks english` (enter_data)
- "mandarin": `it speaks mandarin` (enter_data)
- "portuguese": `it’s trained in portuguese` (enter_data)
- "mandarin": `until now it’s only in mandarin` (enter_data)
- `__email_address__` (enter_data)
- "engineer": `enginer` (enter_data)
- "none"?: `i have none` (enter_data)

#### Unconfident hits
Unusual wordings; in the case of out_of_scope/enter_data likely other classes attract some probability mass:
- `what are the componensts of rasa` (ask_whatisrasa)
- `what does on-premise mean?` (technical_question)
- `i have chosen rasa stack` (install_rasa)
- `that wasn't very funny` (handleinsult)
- `you live around here?` (ask_wherefrom)
- `hey, let's talk` (greet)
- `ok quick question here do i download this api` (technical_question)
- `how to export dialogflow data to rasa` (switch)
- `some thing else` (out_of_scope)
- `i am responsible for our innovation department` (enter_data)

### Cases where one student is very confident and the other one is very unconfident
The confident student is often itself a bit unconfident too.

Where LSTM unconfident, it's mostly correct (and so is the confident BERT). In some cases, the teacher is also unconfident. Examples are often a bit tricky (in wording and lack of keywords:
- `you originated through what means?` (ask_howbuilt)
- `i'd like to know how you were put together?` (ask_howbuilt)
- `what am i called?` (ask_whatismyname)

Where BERT confident, it's ~50% correct (and so is the confident LSTM). Teacher sometimes unconfident too. Examples are of all kinds, mostly tricky.
- `u r a piece of junk` (handleinsult) PREDICTED AS react_positive BY BERT, why???
- `bots are bad` (out_of_scope) BERT predicts correctly, doesn't get tricked by "bad" into react_negative like LSTM and teacher
- `get me a club mate` (out_of_scope) BERT does get tricked into human_handoff (despite not seeing "mate" at training time), unlike LSTM and teacher

### Cases where one student is right and the other is wrong (teacher being right)
Difficult examples: the teacher is mostly confident while both students are mostly unconfident. Students correct are split 50-50, no student being "the better one".
- LSTM confused by keywords: `by whom were you built?` (t:ask_builder, p:ask_howbuilt)
- BERT not understanding unobserved words: `i decline` (t:deny, p:out_of_scope)
- BERT reacting to keyword "alexa": `alexa, order 5 tons of natrium chloride` (t:out_of_scope, p:ask_faq_voice)
- BERT reacting to "mate": `get me a club mate`	(t:out_of_scope, p:human_handoff)

### Overlap of the 2 students' hits/misses
Both students have quite solid agreement, under 20% of mistakes are student-specific. Maybe it means the mistakes are simply due to difficult (noisy?) samples which are hard for any kind of model?

### Cases where teacher is confident but both students are unconfident
Shows how teacher has broader understanding of language than the students. Teacher always correct, students correct about 50% of the time each. Quite difficult examples -- teacher sometimes a bit unconfident, both students always very unconfident.

Nontrivial wordings (typically without keywords) that require more robust intent representation:
- `i decline` (t:deny, L:deny, B:out_of_scope)
- `you live around here?` (t:ask_wherefrom, L:ask_wherefrom, B:ask_wherefrom)
- `whatchcha doing` (t:ask_howdoing, L:out_of_scope, B:ask_howdoing)
- `tlak to you later` (t:bye, L:react_positive, B:bye)
- `are you bilingual?` (t:ask_languagesbot, L:ask_languagesbot, B:out_of_scope)
- `you originated through what means?` (t:ask_howbuilt, L:ask_whatisrasa, B:out_of_scope)
- "moronic" unseen during training: `you're the most moronic person i know` (t:handleinsult, L:out_of_scope, B:out_of_scope)
- "install", "get", "run" are typical of install_rasa: `i have chosen rasa stack` (t:install_rasa, L:install_rasa, B:install_rasa)
- `halo` (t:greet, L:greet, B:greet)

Weird label:
- arguably should be technical_question! `able to integrate with paypal, wordpress, facebook andd twilio` (t:enter_data, L:enter_data, B:technical_question)

### Cases where teacher is right but both students are wrong
Teacher often unconfident, students much more unconfident (i.e. difficult examples). Students very keyword oriented, teacher is much more mature in this sense.

- "junk" unseen during training: `u r a piece of junk` (t:handleinsult, L:enter_data, B:react_positive)
- "moronic" unseen during training: `you're the most moronic person i know` (t:handleinsult, L:out_of_scope, B:out_of_scope)
- unseen during training, show how TEACHER HAS MULTILINGUAL KNOWLEDGE: `como estas` (t:ask_howdoing, L:out_of_scope, B:enter_data)

- confusing "fuck": `fuck yeah!` (t:affirm, L:handleinsult, B:handleinsult)
- confusing "today": `what is todays date` (t:out_of_scope, L:ask_weather, B:ask_weather)
- confusing "who": `who is the president of india ?` (t:out_of_scope, L:ask_builder, B:ask_builder)
- confusing "talk" (handoff is chracterised by "talk/speak"): `whom i talking to` (t:ask_whoisit, L:human_handoff, B:human_handoff)
- confusing "what is rasa": `what is the last version of rasa core?` (t:technical_question, L:ask_whatisrasa, B:ask_whatisrasa)
- missing meywords like "how": `you originated through what means?` (t:ask_howbuilt, L:ask_whatisrasa, B:out_of_scope)
- confusing example, also confusing "talk": `talk to me!` (t:ask_whatspossible, L:human_handoff, B:human_handoff)
