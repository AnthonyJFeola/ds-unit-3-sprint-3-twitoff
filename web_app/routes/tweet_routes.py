# web_app/routes/tweet_routes.py

from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from web_app.models import db, Tweet, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweets.json")
def list_tweets_json():

    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)

    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets():

    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)

    return render_template("tweets.html", message="Here's some tweets", tweets=tweets)

@tweet_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    
    new_tweet = Tweet(tweet_text=request.form["tweet text"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED",
        "tweet": dict(request.form)
    })