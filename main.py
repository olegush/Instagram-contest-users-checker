import argparse
import os
from dotenv import load_dotenv
from instabot import Bot
import re
import time
from random import random


def get_args():
    parser = argparse.ArgumentParser(description='Instagram contest checker')
    parser.add_argument('account', help='Organizer username', type=str)
    parser.add_argument('url', help='Instagram url to contest image', type=str)
    args = parser.parse_args()
    return args


def get_users_who_tagged(bot, comments, likers):
    users = []
    # script will choose random number from 0 to max_delay seconds
    max_delay = 30
    for num, comment in enumerate(comments):
        user_id = comment['user_id']
        username = comment['user']['username']
        # filtering already added users
        if (user_id, username) not in users:
            friends_list = get_friends_list(comment['text'])
            # filtering users who tag nobody and checking friend list
            if friends_list and check_user_friends(friends_list, user_id):
                users.append((user_id, username))
                # delay in the most critical place
                time.sleep(int(random()*max_delay))
    return list(set(users))


def get_friends_list(comment):
    usernames_list = re.findall('(@[A-Za-z0-9_.]*)', comment)
    ids = map(lambda x: bot.get_user_id_from_username(x[1:]), usernames_list)
    return list(ids)


def check_user_friends(friends_list, user_id):
    for friend_user_id in friends_list:
        # checking if friend exists
        if bool(friend_user_id):
            user_followers = bot.get_user_followers(user_id)
            # checking if friend really followed the user
            if friend_user_id in user_followers:
                return True


def get_users_who_liked(users, likers):
    for user in users:
        if str(user[0]) not in likers:
            users.remove(user)
    return users


def get_users_subscribed(bot, users, account_id):
    max_delay = 15
    for user in users:
        user_following = bot.get_user_following(user[0])
        # delay in the most critical places
        time.sleep(int(random()*max_delay))
        if account_id not in user_following:
            users.remove(user)
    return users


if __name__ == '__main__':
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    user_args = get_args()
    account = user_args.account
    url_contest = user_args.url

    bot = Bot()
    bot.login(username=login, password=password)

    account_id = bot.get_user_id_from_username(account)
    media_id = bot.get_media_id_from_link(url_contest)
    # for testing use bot.get_media_comments(media_id) (first 20 comments)
    comments = bot.get_media_comments_all(media_id)
    likers = bot.get_media_likers(media_id)

    users_who_tagged = get_users_who_tagged(bot, comments, likers)
    users_who_liked = get_users_who_liked(users_who_tagged, likers)
    users_subscribed = get_users_subscribed(bot, users_who_liked, account_id)
    approved_users_list = list(map(lambda x: x[1], users_subscribed))
    users_number = len(approved_users_list)
    print('Approved users ({}):\n{}'.format(users_number, approved_users_list))
