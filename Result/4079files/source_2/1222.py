"""Displays the top two post titles on a particular subreddit and displays them
on the Pi while keeping log of all the posts that have been shown.
"""
from typing import List
from enum import Enum

import time
import praw
import controller


class Category(Enum):
    CONROVERSIAL = 'controversial'
    GILDED = 'gilded'
    HOT = 'hot'
    NEW = 'new'
    RISING = 'rising'
    TOP = 'top'


class Scraper:
    """Scrapes reddit for information using PRAW.
    """
    # === Private Attributes ===
    # _reddit:
    #   <Reddit> instance used to scrape information

    def __init__(self) -> None:
        """Initializes a reddit scraper instance.
        """
        self._reddit = \
        praw.Reddit(client_id = "OEpdKH1b6IUrpQ",
                    client_secret = "ESPX97ycu6MdinbH33k95hQc9MM",
                    user_agent = "Python:rpi-display-projects:v1.0.0" +
                                 "(by /u/Cold999)")

    def scrape(self, subreddit_name: str = "all",
                     category: Category = Category.HOT, 
                     num_submissions: int = None) -> \
              List[praw.models.Submission]:
        """Scrapes a certain subreddit <subreddit> (default: all)
        for <limit> number of submissions
        in the <category> category.

        Returns a list of submissions.
        """
        subreddit = self._reddit.subreddit(subreddit_name)
        return getattr(subreddit, category.value)(limit = num_submissions)


class RedditView:
    """Displays titles of information scraped from reddit.
    """
    # === Private Attributes ===
    # _display:
    #   the lcd display controller
    # _scraper:
    #   the reddit scraper
    # _polling_interval:
    #   time between polls to reddit in seconds
    # _subreddit:
    #   the subreddit to poll
    # _category:
    #   the category of the subreddit to poll

    def __init__(self, polling_interval: int = 10,
                       subreddit: str = "all",
                       category: Category = Category.HOT) -> None:
        """Initializes the reddit view.
        """
        self._display = controller.Display(("Polling reddit...", "get ready!"))
        self._scraper = Scraper()
        self._polling_interval = polling_interval
        self._subreddit = subreddit
        self._category = category

    def _poll_titles(self, num: int) -> List[str]:
        """Returns a list of the top <num> titles.
        """
        return [submission.title for submission
                in self._scraper.scrape(self._subreddit, self._category, num)]


    def start_polling(self) -> None:
        """Begins polling reddit and updating the log if
        top post changed.
        """
        while True:
            titles = self._poll_titles(2)
            for i in range(len(titles)):
                titles[i] = titles[i].strip('\n')
                if titles[i] != self._display.get_on_screen()[-i]:
                    self._display.write(titles[i])

            time.sleep(self._polling_interval)


if __name__ == "__main__":
    view = RedditView()
    view.start_polling()
