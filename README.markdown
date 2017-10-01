Everyword Bot
-------------

[![Build Status](https://travis-ci.org/aparrish/everywordbot.svg)](https://travis-ci.org/aparrish/everywordbot) [![Coverage Status](https://coveralls.io/repos/aparrish/everywordbot/badge.svg)](https://coveralls.io/r/aparrish/everywordbot)

This is a small Python script that implements an [`@everyword`](http://twitter.com/everyword)-like Twitter bot. Here's what you'll need to run it:

* Python 2.7+, 3.4+
* [Tweepy](http://www.tweepy.org/)
* a plain text file, with each of your desired tweets on one line

Instructions
------------

Run the script from the command-line like so:

	$ python everywordbot.py --consumer_key=<ckey> --consumer_secret=<csecret> \
		  --access_token=<atoken> --token_secret=<tokensecret> \
		  --source_file=<source> --index_file=<index>

... where:

* `<ckey>` is your Twitter consumer key;
* `<csecret>` is your Twitter consumer secret;
* `<atoken>` is a valid Twitter access token;
* `<tokensecret>` is the access token secret for the token given above;
* `<source>` is the filename of a plain text file, with one tweet per line (defaults to `tweet_list.txt` in the current directory); and
* `<index>` is the name of a file where the script can store the current tweet index (i.e., which line in the file should be tweeted next). The script must be able to write to this file.

You'll need to arrange to have this script run at some interval, using a tool
like `cron`. For example, to post a tweet every half hour, you might put the
command line above in a bash script named `/home/aparrish/post_tweet.sh` and
then put the following in your crontab:

	0,30 * * * * cd /home/aparrish; bash post_tweet.sh >>error.log 2>&1

Production Notes
----------------

Twitter may return one of a variety of error messages in response to an attempt
to post a status update (invalid authorization credentials, rate limits, fail
whales, etc.). This script does not attempt to catch or differentiate between
these errors; however, it will *only* increment the index if the post succeeds.
(The idea is that 100% coverage of the source file is more important than 100%
uptime.)

As stated in the license, this software is provided under no warranty of any
kind. However, if the operation of this script is critical to your business,
grant application, art school thesis, or innovative government program, you may
want to monitor the results of the script by (e.g.) checking the return value
of the script and sending an e-mail message if it's non-zero.  Feel free to
update the script to handle errors in whatever method is appropriate for your
specific application.

Obtaining Twitter authorization credentials
-------------------------------------------

The easiest way to obtain the appropriate credentials is as follows:

* Create a new Twitter account. This is the account on whose behalf the script will post tweets.
* Go to the [Twitter Application Management page](https://apps.twitter.com/) and sign in with the account you just created. (You'll need to verify your account's e-mail address before Twitter will let you log in with your new account.)
* Click "Create a new application."
* Fill in the form. The "Callback URL" field is not important.
* You'll be taken to the overview page for your new application. Activate the "Settings" tab and change the "Application Type" from "Read only" to "Read and Write."
* Return to the "Details" tab. Select "Create my access token" at the bottom of the page.
* Congratulations! All the information that you need (consumer key, consumer secret, access token, access token secret) is now displayed on the "Details" tab.

In my experience, Twitter may prevent newly created accounts from posting
status updates, responding to such requests with invalid authorization errors.
This is likely an anti-spam measure. Wait a few minutes and try again before
freaking out.

Creating your Twitter API application while logged in to your Twitter bot user
account is the by far simplest method for obtaining credentials. However,
you'll hit a wall quick if you want to run more than one bot, since Twitter
requires an account to have an active telephone number attached to it in order
to register new applications, and no two accounts can be associated with the
same phone number. It's possible to swap a single phone number between
accounts (by clearing it out on one account, and adding it to another), but you
might find it easier to manage all of your applications from one account, and
then have your bot accounts authenticate with those applications. [You can use
this
script](https://gist.github.com/moonmilk/035917e668872013c1bd#comment-1333900)
(using tweepy) or [this
script](https://github.com/simplegeo/python-oauth2#twitter-three-legged-oauth-example)
(using the oauth2 library) to get the relevant credentials from Twitter on the
command-line.

(The above information above may become inaccurate if Twitter changes their
policies or the layout of their site.)

License
-------

Everyword Bot is provided under the MIT license. See `LICENSE.TXT` for more information.

