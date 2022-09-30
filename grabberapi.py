from operator import pos
import sys
from instagrapi import Client

login_name = input("Enter Instagram Username: ")
password = input("Enter Password: ")

business = ""
businesses = []
print("Enter the name of the businesses(enter 'done' to end):\n")
while 1:
    business = input()
    if business != "done":
        businesses.append(business)
    else:
        break

post_ammount = int(input("Enter the number of post to pull for each account(max 100): "))
if post_ammount > 100:
    post_ammount = 100

cl = Client()
cl.login(login_name, password)


for business in businesses:
    user_id = cl.user_id_from_username(business)
    medias = cl.user_medias(user_id, post_ammount)
    print("                                                        " + business.upper() + "\n\n")
    for media in medias:
        comments = cl.media_comments(media.id)

        print("Post:\t" + media.caption_text + "\n\n\n\n")

        for comment in comments:
            print("\tComment\t:  " + comment.text)
        print("\n\n\n\n")