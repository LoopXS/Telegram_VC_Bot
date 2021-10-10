HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID", "3208228"])
    API_HASH = environ["API_HASH", "07d1d53a608693a6be436ca387582d8b"]
    SESSION_STRING = environ[
        "SESSION_STRING", "BAC9zP2iEJPhVbwObLX_Tok35cYm4h5v9gfZUqhB_jFwZ-3JdbCJIdDqSefYGnX3pMuDnIjqrw6N65PfbhLv93GGFuq4Zo6aTrB36li50z3hoEKQ0SEsYTAQ7e-o6yYzHxidMf8nSJdfUpRCzaTC6iW3sPqE7AZRtuG4tWX4ZD7tSns7kCVVw7A2H-16TxYExSEo_EDxvIeUXhZLeLsSZkYVVj-zc_VPKTgVqPqOSiUoSrCf70M3SDwGI90VE0JtHXyWHoNhKsv_WWaxaWRH6uulSObsceWGTP0b2xplyo2tE-QQ9k6YN9zQWEtURBJOXhjJucvqiUBQW1PZSEegml3RaWzUjQA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY", "VZPWJD-GKFGNQ-ICATFM-LKISYR-ARQ"]
    CHAT_ID = int(environ["CHAT_ID", "-1001500995042"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE", "512"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
