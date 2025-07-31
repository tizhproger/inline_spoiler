> [!NOTE]
> This code was written many years ago for fun and can be not very good optimised (or written).
> 
> However, it is still can serve as PoC

> [!CAUTION]
>*Current problem:*
>  Hidden usernames
>

# 🕵️ Inline Spoiler Bot
Inline feature for bot, allowing to hide message text from particular user(s)

This implementation is packed into a bot, but you can use it standalone, just copying the 2 needed functions (`callback` and `inline` handlers) and variables (`spoilers` dictionary)

## 🚀 Installation & Run

1. Install the required library:
   ```bash
   pip install pyTelegramBotAPI
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/tizhproger/inline_spoiler.git
   cd inline_spoiler
   ```

3. Insert your bot token in `spoiler_text.py`:
   ```python
   API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ```

4. Run the bot:
   ```bash
   python spoiler_text.py
   ```

## 🧠 Usage

- Type `@YourBotUsername` in message field and choose inline option
- Recipient will see a "Show" button to reveal the hidden text
- Ideal for spoilers or private messages
