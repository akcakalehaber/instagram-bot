from instapy import InstaPy

session = InstaPy(username="your username here...", password="your password here...", headless_browser=True)
session.login()

#following section 
session.set_do_follow(True, percentage=50, times=1)

#like section (Chnage tags here)
session.like_by_tags(['javascript', 'python'], amount=3)
session.set_dont_like(["naked", "nsfw", "sex"])

#comment section (Add more comments)
session.set_do_comment(True, percentage=100)
session.set_comments([u'I love your post @{}!'])


session.end()
