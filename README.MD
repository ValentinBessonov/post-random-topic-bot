# post-random-topic-bot

Welcome to post-random-topic-bot — a versatile Telegram bot for generating and managing dynamic posts. This README provides an overview of the bot's structure, functionalities, and how to run it.

## Files Overview:

1. **main.py:**
   - The main script containing the Telegram bot's core functionality.

2. **config.json:**
   - Configuration file storing sensitive information such as the Telegram bot token, channel ID, and the allowed user's username.

3. **openai_post_generator.py:**
   - Module responsible for interacting with the OpenAI API to generate posts based on user-provided topics.

4. **random_topic_selector.py:**
   - Module for randomly selecting topics from the "topics.txt" file.

5. **topics.txt:**
   - A file containing a list of topics, each on a separate line. These topics are randomly selected for post generation.

## How to Run the Bot:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ValentinBessonov/post-random-topic-bot.git
   cd post-random-topic-bot
   ```

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

1. **Configure the Bot:**
    Fill out the config.json file with the required configuration information.

1. **Run the Bot:**
   ```python main.py```

## Functionality Overview:

1. **Sending Random Posts to Channel:**
   - Command: `/sendposttochannel`
   - Sends a random post to the designated channel.

1. **Getting Random Posts from Bot:**
   - Command: `/getrandompost`
   - Retrieves a random post from the bot.

1. **Generating Posts Based on Topics:**
   - Command: `/getpostwithtopic <topic>`
   - Generates a post based on the user-inputted topic.

1. **Pinging the Bot:**
   - Command: `/ping`
   - Checks if the bot is responsive.

1. **Scheduled Daily Post:**
   - A random post is automatically sent to the channel every day at 9:00 AM (Asia/Nicosia timezone).

## Additional Modules:

- **openai_post_generator.py:**
  - Utilizes the OpenAI API to dynamically generate posts based on user-inputted topics.

- **random_topic_selector.py:**
  - Randomly selects topics from the "topics.txt" file, which contains a list of topics.