questions = [
    {
        "question": "You promised a friend you would keep a secret, but revealing it could prevent someone from being harmed. What should you do?",
        "answers": {
            "a": {
                "text": "Keep the promise because promises create moral duties.",
                "scores": {
                    "deontology": 3,
                    "consequentialism": 0,
                    "virtue_ethics": 1,
                    "care_ethics": 1,
                    "contractualism": 1
                }
            },
            "b": {
                "text": "Reveal the secret if doing so is likely to prevent the most harm.",
                "scores": {
                    "deontology": 0,
                    "consequentialism": 3,
                    "virtue_ethics": 1,
                    "care_ethics": 2,
                    "contractualism": 1
                }
            },
            "c": {
                "text": "Consider what a compassionate and trustworthy person would do.",
                "scores": {
                    "deontology": 1,
                    "consequentialism": 1,
                    "virtue_ethics": 3,
                    "care_ethics": 2,
                    "contractualism": 1
                }
            }
        }
    }
]

scores = {
    "deontology": 0,
    "consequentialism": 0,
    "virtue_ethics": 0,
    "care_ethics": 0,
    "contractualism": 0
}

for question in questions:
    print()
    print(question["question"])
    print()

    for letter, answer in question["answers"].items():
        print(f"{letter}. {answer['text']}")

    choice = input("\nChoose a, b, or c: ").lower()

    selected_answer = question["answers"][choice]

    for theory, points in selected_answer["scores"].items():
        scores[theory] += points

print()
print("Your results:")

sorted_scores = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)

for theory, score in sorted_scores:
    print(f"{theory}: {score}")

print()
print(f"Your strongest alignment is {sorted_scores[0][0]}.")
print(f"Your second strongest alignment is {sorted_scores[1][0]}.")