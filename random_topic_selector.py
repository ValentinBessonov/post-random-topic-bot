import random

def get_random_topic(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        topics = [line.strip() for line in file]

    if not topics:
        return None

    return random.choice(topics)

if __name__ == '__main__':
    file_path = 'topics.txt'
    random_topic = get_random_topic(file_path)

    if random_topic:
        print(f'Random topic selected: {random_topic}')
    else:
        print(f'Random topic not selected. File {file_path} is empty.')

