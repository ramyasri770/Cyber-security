def calculate_simple_interest(principal, rate, time):
    """Function to calculate simple interest"""
    return (principal * rate * time) / 100

def real_world_examples():
    """Provides real-world applications of simple interest"""
    examples = [
        {"scenario": "Bank Fixed Deposit", "principal": 10000, "rate": 6, "time": 5},
        {"scenario": "Car Loan Interest", "principal": 500000, "rate": 7.5, "time": 3},
        {"scenario": "Education Loan", "principal": 200000, "rate": 5.5, "time": 7},
    ]
    
    print("\nReal-World Examples of Simple Interest:")
    for example in examples:
        interest = calculate_simple_interest(example["principal"], example["rate"], example["time"])
        print(f"{example['scenario']}: Principal = ₹{example['principal']}, Rate = {example['rate']}%, Time = {example['time']} years → Interest = ₹{interest:.2f}")

def quiz():
    """Interactive quiz to test user's understanding"""
    print("\nQuiz Time!")
    question = "You deposit ₹8000 in a savings account with an annual interest rate of 4% for 2 years. What will be the simple interest?"
    print(question)
    
    user_answer = float(input("Enter your answer: "))
    correct_answer = calculate_simple_interest(8000, 4, 2)

    if user_answer == correct_answer:
        print("Correct! You're getting the hang of it!")
    else:
        print(f"Oops! The correct answer is ₹{correct_answer:.2f}")

# Execute the program
real_world_examples()
quiz()