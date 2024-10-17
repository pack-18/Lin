from pyrogram import Client, filters

# Replace with your actual API ID, API hash, and bot token
API_ID = YOUR_API_ID
API_HASH = YOUR_API_HASH
BOT_TOKEN = YOUR_BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat & filters.command("start"))
async def greet_user(client, message):
    username = message.from_user.username
    welcome_message = f"Welcome, {username}! Have a good day!"
    await message.reply(welcome_message)

@app.on_message(filters.text)
async def check_message(client, message):
    # Extract message content
      text = message.text

    # Check for required parameters (ch and id)
      if "ch=" not in text or "id=" not in text:
      await message.reply("Invalid link. Please provide parameters in the format 'ch=VALUE&id=VALUE'.")
      return

    # Extract parameters using dictionary comprehension
      params = {part.split("=")[0]: part.split("=")[1] for part in text.split("&")}

      try:
      ch = params["ch"]
      id_value = params["id"]

    # Process the parameters (replace with your actual logic)
                                                                                        # ... (e.g., validate data, perform actions)

                                                                                                # If parameters are valid, send a button with the provided URL
                                                                                                        button_text = "Good"
                                                                                                                button_url = "https://www.google.com"  # Replace with your desired URL
                                                                                                                        await message.reply(
                                                                                                                                    f"Parameters processed successfully! Click the button below:",
                                                                                                                                                reply_markup=client.InlineKeyboardMarkup(
                                                                                                                                                                [[client.InlineKeyboardButton(button_text, url=button_url)]]
                                                                                                                                                                            ),
                                                                                                                                                                                    )
                                                                                                                                                                                        except KeyError:
                                                                                                                                                                                                # Handle missing parameters
                                                                                                                                                                                                        await message.reply("Invalid link. Please ensure both 'ch' and 'id' parameters are present.")

                                                                                                                                                                                                        app.run()
                                                                


       
        
        
        
               

