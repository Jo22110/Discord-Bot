# Discord Bot

This is a Discord bot built using Python and the discord.py library. The bot includes various features such as moderation commands, music playback, and utility commands.

## Project Structure

```
discord-bot
├── bot
│   ├── __init__.py
│   ├── main.py
│   ├── cogs
│   │   ├── __init__.py
│   │   ├── moderation.py
│   │   ├── music.py
│   │   └── utility.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   └── utils
│       ├── __init__.py
│       ├── logger.py
│       └── helpers.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Features

- **Moderation Commands**: Ban, kick, and manage users in the server.
- **Music Commands**: Play, pause, and stop music in voice channels.
- **Utility Commands**: Basic commands like ping and info.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-bot.git
   cd discord-bot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure the bot settings in `bot/config/settings.py`:
   - Set your bot token and command prefix.

5. Run the bot:
   ```
   python -m bot.main
   ```

## Usage

Once the bot is running, you can use the commands defined in the cogs. For example, use `!ping` to check if the bot is responsive.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.