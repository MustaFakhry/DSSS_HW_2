import random


def generate_random_number(min_value: int, max_value: int) -> int:
    """
    Generates a random integer between min_value and max_value.

    Args:
        min_value (int): The minimum value for the random number.
        max_value (int): The maximum value for the random number.

    Returns:
        int : randomly generated integer.
    """
    return random.randint(min_value, max_value)


def select_random_operator() -> str:
    """
    Selects a random mathematical operator.

    Returns:
        str: A randomly chosen operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def create_problem_and_solution(num1: int, num2: int, operator: str) -> tuple:
    """
    Creates a math problem string and calculates the expected solution.

    Args:
        num1 int: The first number in the problem.
        num2 int: The second number in the problem.
        operator str: The mathematical operator.

    Returns:
         A tuple containing the problem string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"

    try:
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        else:
            raise ValueError("Invalid operator")
    except TypeError as e:
        print("Error in creating the problem:", e)
        raise

    return problem, answer


def math_quiz():
    """
    Runs the math quiz game, presenting users with math problems to solve.
    """
    score = 0
    num_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 5)
        operator = select_random_operator()

        problem, correct_answer = create_problem_and_solution(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{num_questions}")


if __name__ == "__main__":
    math_quiz()
