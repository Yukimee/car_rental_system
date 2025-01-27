from questions import Question

# this is an array
question_prompts = [
    "What color are apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

# the correct answer for each question
question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(data_passes_in):
    score = 0
    for eachQuestion in data_passes_in:
        answer = input(eachQuestion.prompt)
        if answer == eachQuestion.answer:
            score += 1
    print(f"You got {score}/{len(data_passes_in)} correct!")


run_test(question)



