# Individual models
## When the models succeed and fail
CoLA
- All models confidently succeed on acceptable examples which are in many cases (syntactically and semantically) simple sentences (effect of class imbalance?).
- All models confidently fail on tricky unacceptable sentences (predicted as acceptable, i.e. majority class). Issues are mostly semantic, e.g. `Mary wonders that Bill will come.` where many verbs other than "wonder" would work. Teacher & BERT are more tricked by long-range issues; LSTM struggles with imperatives+binding (`wash you!`).
- All models are unconfident about various examples, both acceptable and unacceptable -- mostly difficult ones, with unusual or wrong clause or word order, semantic issues, both short-and long-range issues, etc., e.g. `the soundly and furry cat slept.`, `with no job would john be happy.`, `most columnists claim that a senior white house official has been briefing them, and the newspaper today reveals which one.`

SST-2
- All models confidently succeed on positive examples which are very easy (contain only neutral/positive words)
- All models confidently fail mostly on examples with wrong/questionable labels; followed by examples where strong-sentiment keywords oppose the overall sentiment (models fail to understand `(al)though X, Y`, `all that's missing is X`, `X, but Y`, etc).
- All models are unconfident about examples without strong/clear sentiment, and where sentiment surfaces in metaphors/idioms/expressions bound to contextual knowledge (`in a way , the film feels like a breath of fresh air , but only to those that allow it in .`, `collateral damage finally delivers the goods for schwarzenegger fans .`). Problematic are also cases with both positive and negative words together (`hilariously inept and ridiculous .`), as well as long examples where the sentiments is "diluted" among many neutral words.

Sara
- All models confidently succeed on enter_data (majority class), with students picking up keywords (esp. language names) while teacher picks up also more complex cases with words unseen in training ("unemployed"). LSTM slightly prefers short keywords to long ones (e.g. `__email_address__`).
- All models confidently fail mostly by assigning unseen/unclear examples (`ciao`, `I'm not sure`) to biggest classes (enter_data, out_of_scope), and by assigning to classes based on characteristic keywords (`ok let's start` -> how_to_get_started, `not bad` -> deny, `fuck yeah` -> handleinsult).
- Unconfident predictions are made mostly for examples that don't contain key words strongly associated with a particular intent, e.g. `what do you do as a company?` (ask_whatisrasa), `i want to put some of my effort in.` (ask_how_contribute). Interesting are several cases where models leverage pretrained language knowledge to handle words unseen in training: `i decline` (deny; correct by LSTM), `i want to know current situtation in pakistan` (out_of_scope; predicted as ask_wherefrom by teacher, likely because "country" is characteristic of the intent). Similar intents are also sometimes confused, e.g. `what should i work on?` (t:ask_how_contribute, p:how_to_get_started).

## Confidence of predictions: how confident is the model on average? and just on the mistakes?

# Comparing models
## Is one student generally more confident than the other?
## Cases where one student is very confident and the other one is very unconfident
## Cases where one student is right and the other is wrong
## Overlap of the 2 students' mistakes; which ones are unique to one student?

# Exploring knowledge distillation
## Cases where teacher is confident but both students are unconfident
## Cases where teacher is right but both students are wrong

# Overall
## Strengths/weaknesses of each student
