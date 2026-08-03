from datetime import datetime

from questions import questions
from storage import save_result


THEORIES = [
    "deontology",
    "consequentialism",
    "virtue_ethics",
    "care_ethics",
    "contractualism"
]


def get_choice(question):
    valid_choices = question["answers"].keys()

    choice = input("\nChoose a, b, or c: ").strip().lower()

    while choice not in valid_choices:
        print("Please enter a valid answer.")
        choice = input("Choose a, b, or c: ").strip().lower()

    return choice


def run_quiz():
    scores = {theory: 0 for theory in THEORIES}
    responses = []

    print("\nEthics Quiz")
    print("Answer each question based on what you believe is most defensible.")

    for number, question in enumerate(questions, start=1):
        print()
        print(f"Question {number} of {len(questions)}")
        print(f"Category: {question['category']}")
        print()
        print(question["question"])

        for letter, answer in question["answers"].items():
            print(f"{letter}. {answer['text']}")

        choice = get_choice(question)
        selected_answer = question["answers"][choice]

        for theory, points in selected_answer["scores"].items():
            scores[theory] += points

        confidence = get_confidence()

        responses.append(
            {
                "question_id": question["id"],
                "category": question["category"],
                "question": question["question"],
                "choice": choice,
                "answer": selected_answer["text"],
                "confidence": confidence
            }
        )

    sorted_scores = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    result = {
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "scores": scores,
        "primary_theory": sorted_scores[0][0],
        "secondary_theory": sorted_scores[1][0],
        "responses": responses
    }

    save_result(result)
    display_results(result)


def get_confidence():
    confidence = input(
        "How confident are you in this answer, from 1 to 5? "
    ).strip()

    while confidence not in {"1", "2", "3", "4", "5"}:
        print("Please enter a number from 1 to 5.")
        confidence = input("Confidence, from 1 to 5: ").strip()

    return int(confidence)


def display_results(result):
    sorted_scores = sorted(
        result["scores"].items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\nYour results:")

    for theory, score in sorted_scores:
        readable_name = theory.replace("_", " ").title()
        print(f"{readable_name}: {score}")

    primary = result["primary_theory"].replace("_", " ").title()
    secondary = result["secondary_theory"].replace("_", " ").title()

    print()
    print(f"Primary alignment: {primary}")
    print(f"Secondary alignment: {secondary}")
    print("Your result has been saved to your quiz history.")


if __name__ == "__main__":
    run_quiz()