def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
  

    # Create an empty dictionary to store the frequency of each retweeted username.
    retweet_counts = {}

 
    str_idx = 0
    retweet_counts = {}

    for tweet in tweet_list:
        parsed_tweet = tweet.split(" ")
        for i in parsed_tweet:
            if (i == "RT"):
                if (parsed_tweet[str_idx+1][1:-1] in retweet_counts):
                    retweet_counts[parsed_tweet[str_idx+1][1:-1]] += 1
                else:
                    retweet_counts[parsed_tweet[str_idx+1][1:-1]] = 1
            str_idx += 1
        str_idx = 0
    
    return retweet_counts

def display(deposits, top, bottom, left, right):
    ans = ""
    deposits.sort()
    deposits_idx = 0
    while (deposits_idx < len(deposits) and deposits[deposits_idx][0] < left):
        deposits_idx += 1
    for row in range(top, bottom):
        if(deposits_idx < len(deposits) and deposits[deposits_idx][0] == row):
            for column in range(left, right):
                if (deposits[deposits_idx][1] == column):
                    ans += "X"
                    if (deposits_idx + 1 < len(deposits) and deposits[deposits_idx + 1][0] == deposits[deposits_idx][0]):
                        deposits_idx += 1
                else:
                    ans += "-"
            deposits_idx += 1
        else:
            for column in range(left, right):
                ans += "-"
        ans += "\n"
    return ans

def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
 

    total = 0.0
    for deposit in deposits:
        if deposit[0] >= top and deposit[0] < bottom and deposit[1] >= left and deposit[1] < right:
            total += deposit[2]
    return total