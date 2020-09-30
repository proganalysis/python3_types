from __future__ import print_function

import random
import boto3
from requests_oauthlib import OAuth1Session

def lambda_handler(event, context):
    bucket = boto3.resource('s3').Bucket('gengo-hacker')

    # Quotes
    quotes = bucket.Object('quotes.txt').get()['Body'].read().decode('utf-8')
    quotes = [q.split("\t") for q in quotes.split("\n")]
    quotes = ["{} by {} #{}".format(q[0], q[1], q[2]) for q in quotes if len(q) == 3 and all([item != '' for item in q])]
    quotes = [q for q in quotes if len(unicode(q, 'utf-8')) <= 140]

    # AUTH
    token = bucket.Object('token.tsv').get()['Body'].read().decode('utf-8')
    token = dict([t.split('=') for t in token.split("\n")])
    tw = OAuth1Session(token['consumer_key'], token['consumer_secret'], token['access_token_key'], token['access_token_secret'])

    return tw.post('https://api.twitter.com/1.1/statuses/update.json', params={"status": random.choice(quotes)})
