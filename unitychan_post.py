# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings

msg = "進捗!!進捗!!"

def main():
    
    slack = Slacker(slackbot_settings.API_TOKEN)
    slack.chat.post_message(
        'unity_chan_test',
        msg,
        as_user=True
        )

    

if __name__ == '__main__':
    
