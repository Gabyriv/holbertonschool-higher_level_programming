#!/usr/bin/python3
"""Consuming and processing data from an API using Python"""

import requests
import json
import csv


def fetch_and_print_posts():
    """Fetches posts from a sample API and
        prints the titles of the posts.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print(f"Failed to retrieve data {response.status_code}")


def fetch_and_save_posts():
    """Fetches posts from a sample API and
        saves them to a CVS file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        posts_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        with open('posts.csv', "w", encoding='utf-8') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts_data)
