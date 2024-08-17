from os import getenv

API_ID = getenv("API_ID", "20937630")
API_HASH = getenv("API_HASH", "3290b11b9246bff1ff44f13e9c7ffb45")
BOT_TOKEN = getenv("BOT_TOKEN", "7350533162:AAExMOuqwEJyIK0IpszG3DBSkc_G8dvyrYY")
BOT_COMMANDS = (
    ("start", "Initialize the bot and check its status"),
    ("settings", "Configure and manage bot settings"),
    ("help", "Get information on how to use the bot"),
    ("about", "Learn more about the bot and its features"),
)

DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://tabolo8539:0evqZDV4fC5fD17c@cluster0.cw8zxus.mongodb.net/?retryWrites=true&w=majority")
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))
