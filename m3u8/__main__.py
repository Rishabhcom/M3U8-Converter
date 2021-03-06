import logging
import os
from pyrogram import Client
from m3u8 import (
    APP_ID,
    API_HASH,
    DOWNLOAD_LOCATION,
    TG_BOT_TOKEN
)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    plugins = dict(
        root="m3u8/plugins"
    )
    app = Client(
        "m3u8",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.set_parse_mode("html")
    app.run()
