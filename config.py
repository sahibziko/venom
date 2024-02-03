import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26090016"))
API_HASH = getenv("API_HASH", "5b842f9801712684f2b98d70ead6538d")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6884291431:AAE0ohhqcoJFeYXne6-VNI8npL46fyE5Szs")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rahidindi:rahidindi_1234@cluster0.ifslufs.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002063353430"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6471021703"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Theferid/The_ferid",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "https://t.me/Qruzda")  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FerooResmi")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GunelSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgGz374AgxfrPwlMkuR9S4eM_xpCwqqKBPPvqlaz2kabXvOLfQd6IMqwBKuNvh-IX4210BnCjdYEMDLoicM4K9-1sshxkBDV1pPmHYAREHhlc1W2Nn4hbuAJ6Iyehlui_UrfqNQ-diGllC_vdsRjf_t91GIRV01xankc6_17JBTYrwj3a6V9-NJYJuaU6GkzajXRsthayWNK34_lGsQg1we-2Ij9_xFhONP1YKcySlIC4r7DhQw6Xqs5Q_sodDC8AXqQmT9kRQF5jzw-0s4L1er-2lJ1LeTFwBmdxEPicbsR1rVCywnzTC8B54UOl1Uno2GwdozJlI78BRZXOA7x5aUnq4h4ywAAAAFPGm-xAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
STATS_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/2292e230eaadd89845a20.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
