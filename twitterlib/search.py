"""
Search module.
"""
import sys

import tweepy

import auth
import constants
import lib


def geo_to_str(latitude, longitude, distance):
    assert distance.endswith("km") or distance.endswith(
        "mi"
    ), "Must include units as km or mi."

    return ",".join((latitude, longitude, distance))


def search(api, q=None, geocode=None, lang=None):
    cursor = tweepy.Cursor(
        api.search,
        q=q,
        geocode=geocode,
        lang=lang,
        count=constants.MAX_COUNT.SEARCH_TWEETS,
        tweet_mode=constants.TweetMode.EXTENDED,
    )

    return cursor


def main(args):
    api = auth.app_access_token_api()

    geocode = geo_to_str("33.3125", "44.3661", "100km")
    lang = "ar"

    cursor = search(api, geocode=geocode, lang=lang)

    lib.print_tweets(cursor)


if __name__ == "__main__":
    main(sys.argv[1:])