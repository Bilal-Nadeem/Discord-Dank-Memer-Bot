# Discord Dank Memer Bot

This is a Discord bot for interacting with the Dank Memer game. It includes functionalities to play Blackjack, trade items, scratch cards, and stream activities. The bot uses the Discord API to interact with the server.

> **Note**: This project was created in 2021 and is no longer functional as it is outdated. It serves as a proof of concept for bot development and interaction with the Discord API.

## Features

- **Play Blackjack**: Automatically plays a game of Blackjack with the server.
- **Stream Activities**: Simulates streaming activities such as reading chat, running ads, and collecting donations.
- **Trade Inventory Items**: Trades items from the user's inventory with other users.
- **Scratch Cards**: Participates in scratch card games.

## Requirements

- Python 3.x
- Requests library (install via `pip install requests`)

## Setup

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:

   Make sure you have the required libraries. You can install them using pip:

   ```bash
   pip install requests

   ```

3. **Create Discord Bot**:

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application.
   - Under the "Bot" tab, create a bot user and copy the token.

4. **Update Tokens**:

   In the `main.py` file, update the `tokens` dictionary with your list of your bot's token:

   ```python
   tokens = {
       "Mr. Stark": "your-token-here",
       "Gary Oak": "your-token-here"
   }
   ```

5. **Set Channel and Guild IDs**:

   Replace `channel-id` and `guild-id` in the `main.py` file with the respective IDs from your Discord server.

## Usage

1. **Run the Bot**:

   You can start the bot by running the following command:

   ```bash
   python main.py
   ```

2. **Interacting with the Bot**

    The bot will automatically engage in the specified activities:
    - **Play Blackjack**: The bot will continuously play Blackjack until the game ends.
    - **Stream Activities**: The bot will perform streaming actions based on the defined strategy.
    - **Trade Inventory Items**: The bot will attempt to trade items from the inventory.
    - **Scratch Cards**: The bot will participate in scratch card games.

## Notes

- The bot's functionalities rely on the Discord API, which may change. Ensure that the bot complies with Discord's terms of service.
- The bot might require adjustments if the API endpoints or interaction methods change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
