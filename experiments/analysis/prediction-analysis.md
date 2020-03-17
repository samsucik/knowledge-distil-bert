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
All labell  ed as positive and contain only neutral or positive words.
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
Surprisingly many mistakes are model-specific! Rougly 1/3 of each model's mistakes are made only by that model and the other model gets those right.

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
