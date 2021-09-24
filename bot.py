from instabot import Bot
import glob
import os

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])


bot = Bot()

bot.login(username = "######", password = "#########")

#to post a photo
#bot.upload_photo("1.jpeg",caption = "NY Cap for 299 only" )

followers = bot.get_user_followers("deepak.exec")

#get followers details of deepak.exec username
for follower in followers:
    print(bot.get_user_info(follower))


cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])