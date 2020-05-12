import argparse
import path
import json

from twittback.client.twitter_client import from_json
import twittback.repository


def import_tweets(base_path, repository):
    for json_path in base_path.files("*.json"):
        parsed_json = json.loads(json_path.text())
        tweets = [from_json(x) for x in parsed_json]
        repository.add_tweets(tweets)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path", type=path.Path)
    args = parser.parse_args()
    repository = twittback.repository.get_repository()
    import_tweets(args.json_path, repository)


if __name__ == "__main__":
    main()
