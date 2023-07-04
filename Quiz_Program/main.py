quiz = {
    'question1': {
        'question': 'What is the capital of India',
        'Answer': 'New delhi'
    },
    'question2': {
        'question': 'How many states are present in India',
        'Answer': '29'
    },
    'question3': {
        'question': 'What is the national language of india',
        'Answer': 'Hindi'
    },
    'question4': {
        'question': 'What is the national bird of india',
        'Answer': 'Peacock'
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    # print(value['Answer'])
    answers = input('Enter the answer: ')

    if answers.lower() == value['Answer'].lower():
        print('Correct')
        score = score + 1
    else:
        print('Wrong')
        print(f"Correct Answer is {value['Answer']}")
        score = score - 1

print(f'Total Score is {score}')
print(f'Your Percentage is {str(score / 4 * 100)}%')