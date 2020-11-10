 
# #  https/www.reddit.com  # create on this account 

# # https/www.reddit.com/prefs/apps/   # creating app on this link which is use ijn thew reddit_bot python program
# #  copy the secret_client and client_id which your are created 

# # and install the praw modules through the package  manager called ( pip )  and thiemn import them in your 
# # program where you write it 

import praw     # provied reddit Api

# # # client id, client_secret, password, username and agent_name  take from where we create account an reddit 
 
reddit = praw.reddit(client_id = 'yI8WM6yt-1W3Ig',              
                      client_secret='3fiHmTH8YQnof9FyV_W1QEOiIg',
                      username = 'prawtutorial',
                      password = 'cookies',
                      user_agent = 'prawtutorialv1' )


subreddit = reddit_subreddit('python')  # in this we only take the one category from the reddit through the sub_reddit function 
                                        # so we take the informaion about the puython

hot_python = subreddit.hot(limits=5) # here we apply the the limits we just take the reddit top 5 hot  comments or post 

for submission in hot_python: # we use for loop to get the data from the hot-python
    if not submission.stickied: # take stickied comments then show on screan
        print('title:{}, ups: {}, down:{}, have we visited: {}'.format(submission.title, # show the title 
            submission.ups, # show ups 
            submission.downs, #show downs
            submission.visited)) #show visited 

#  take the comments and display them through for loop
        comments = submission.comments.list()
        for comment in comments:
            print(20*'-')
            print('Parant ID :' + comment.parent()) 
            print('comments ID :' + comment.idt())
            print(comment.body)




subreddit.subscribe()  # by help of this subscribe() function we subscrib in the reddit 


# #  for streaming 


# import praw     # provied reddit Api

# reddit = praw.reddit(client_id = 'yI8WM6yt-1W3Ig',              
#                       client_secret='3fiHmTH8YQnof9FyV_W1QEOiIg',
#                       username = 'prawtutorial',
#                       password = 'cookies',
#                       user_agent = 'prawtutorialv1' )


# subreddit = reddit_subreddit('python')  # in this we only take the one category from the reddit through the sub_reddit function 
#                                         # so we take the informaion about the puython

# for comment in subreddit.stream.comments():
#     try:
#         print(comment.body)
#     except Exception as e:
#         print(str(e))






# #  QR grenaration code in python 

# import qrcode
# import Image

# qr=qrcode.QRCode(
#     version=1,
#     box_size=10,
#     border=5
# )

# data = "hello i am a qrcode"
# qr.add_data(data)
# qr.make(fit=True)
# img=qr.make_image(fill="black",back_color="white")
# img.save("qr.png")