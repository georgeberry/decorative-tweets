from tweet_decorator import tweet_me


if __name__ == '__main__':

    #as a decorator
    @tweet_me('@username')
    def failure():
        return 'not an integer'/42

    failure()


    #as a class

    tweet_result = tweet_me('@username')
    tweet_result.tweet('message')

