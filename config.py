import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "3011757"))
API_HASH = getenv("API_HASH", "1bb6781eb0e370d1f3d6b524bd8ad472")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6991503896:AAE9TSHa3hFlkVxhCp-4SsZ5V81q85ocULM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://elegant:SsSsSs1212Ss!@elegant.ptzwgmg.mongodb.net/?retryWrites=true&w=majority&appName=elegant")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002104254612"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "1419590194"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sahibziko/venom/",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/apexubsohbet")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Apexubsohbet")

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
STRING1 = getenv("STRING_SESSION", "AQFMIVwAT5tdhLfVQhOw2MC2uJ24qVG6iSwPYMg9bs4pLw2o9Z6h07XZRKMrOlr_RMr9YJUroxu7Op3nysfBvppkEWP73PtuXaEwWJsC5b7w4R4QCDE9sctLV2w8oYxy6CVWV5nxQmVDs579a3wkdqhTvnZ3CbtxMAIzQKmiQciuANIC1BMhdOxciiJrsVOVSKleT5rxxF-8btbjOKhbjy5BMLffAth-HKVp_ixqT6VbqBTt9YCpO5nF6C8kOwW5q-iAZ3hHqFM14VPxHFjRJ5Tv9Cmmt8NN82l2C4SmS878r4cOmGi5rNHFyjOSH2CGlDLplWcr9_XilnoByXCEaHmCgGusjAAAAAE6rViNAA")
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
    "START_IMG_URL", "https://telegra.ph/file/90d5dbb28269820702283.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/90d5dbb28269820702283.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
STATS_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/90d5dbb28269820702283.jpg"


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
