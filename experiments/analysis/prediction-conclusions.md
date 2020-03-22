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

## Confidence of predictions
In general, the differences in average confidence are small, but the teacher is more confident than both students, which is expected since the teacher likely has richer representations of inputs.

Additionally, all models are on average more confident on hits than on misses, in particular on Sara. This is also reasonable because all datasets contain many examples whose class is not very clear -- those are likely to be misclassified and the confidence is also likely to be low since it reflects how strongly the example is believed to belong to a particular class.

Finally, the average confidence is highest on SST-2, lower on CoLA and lowest on Sara. This can be explained by two effects: the number of classes (the more classes, the more probability mass is likely to be redistributed from the top class), which explains the low confidence on Sara, and the difficulty of a task (here surfacing as the difficulty for students to match the teacher's performance), which explains the lower confidence on CoLA compared to SST-2 (if the tasks were all using the same metric, the difficult could be compared based on the model scores, but now this is not an option).

# Comparing models
## Is one student generally more confident than the other?
This does not seem to be the case. Even though there are minor differences in confidence, these can mostly be attributed to differences in performance. There is no reason to believe that, if both students had the exact same score, their average confidence would differ. This is interesting since the models are so architecturally different and the tasks are also very different.

When looking at confidence distributions instead of just average values, it is clear that the teacher's distribution is more strongly concentrated around absolute confidence (1.0) whereas students mostly tend to be a bit unconfident, likely placing a bit more probability on the non-selected classes, i.e. having the probability distributions over all classes less sharply peaked.

## Cases where one student is very confident and the other one is very unconfident
CoLA: These are various examples, but the teacher struggles with most of them (being unconfident or even incorrect). Interestingly, when LSTM is unconfident, it is still often correct (and so is the confident BERT).

SST-2: These are various examples, but mostly long and tricky sentences with tricky structure/wording, with idioms, metaphors and similes, domain knowledge often required, and sometimes with unclear sentiment. The teacher is mostly correct, but below its average. Both students are often incorrect. There are no clear links to the unconfident student's correctness or to the confident student. Interestingly, the teacher is generally more confident on the examples where BERT is unconfident, and is less confident where LSTM is unconfident, thus hinting at the teacher and the LSTM student struggling with similar examples.

Sara: Various examples, mostly difficult ones, with the teacher often unconfident and sometimes wrong. When the LSTM is unconfident, it is still often correct (as well as the confident BERT), but the same doesn't hold when BERT is the unconfident one. Interestingly, BERT unconfidently classifies `get me a club mate` (out_of_scope) as human_handoff despite not seeing "club" or "mate" during training -- this likely comes from pretrained knowledge.

## Cases where one student is right and the other is wrong
Teacher is required to be right so that students have a reasonable chance to be right too. In general, both students are incorrect about the same, no one appears here much more often as the correct one.

CoLA: Various, mostly long and difficult examples, with the teacher being mostly unconfident, and one or both students being very unconfident (not necessarilly the incorrect one).

SST-2: Various examples, mostly long ones, quite difficult since the teacher itself is often unconfident. Interestingly, LSTM predicts almost exclusively negative while BERT predicts positive. The incorrect prediction is often unconfident.

Sara: Various difficult examples, though the teacher is mostly confident. Both students are mostly unconfident. As with many other mistakes, here the students often get confused by keywords, e.g. BERT classifying `alexa, order 5 tons of natrium chloride` (out_of_scope) as ask_faq_voice.

## Overlap of the 2 students' mistakes/hits
One overll finding: LSTM repeats teacher's mistakes more than BERT (which makes its own mistakes instead).

CoLA: Most hits of students are also shared with the teacher (92-94%), but this also means each student having some hits where the teacher failed! The hits of the two students have around 91% overlap, which again leaves each student has some few hits unique to it. As for mistakes, more of the teacher's mistakes are also made by LSTM (71%) than by BERT (64%), with both students still predicting correctly many of the teacher's misses. The students share almost 70% of their mistakes, with ~30% being unique to each student.

SST-2: Around 97% of students' hits are shared with the teacher; this extreme overlap is not surprising given the high overall hit rate (over 91%) and the very difficult (or wrongly labelled) examples that are likely to not contribute to any model's hits. Again, slightly more of teacher's mistakes are made also by LSTM (72%) than by BERT (68%). Roughly 2/3 of mistakes are shared by both students.

Sara: As much as 98% of students' hits is shared with the teacher. The overlap of mistakes is also high: 84% of the teacher's mistakes are repeated by BERT, and 88% are repeated by LSTM. Over 80% mistakes are shared by both students.

# Exploring knowledge distillation
## Cases where teacher is confident but both students are unconfident
## Cases where teacher is right but both students are wrong

# Overall
## Strengths/weaknesses of each student
