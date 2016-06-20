# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings

msg = "進捗!!進捗!!"

if __name__ == '__main__':
    slack = Slacker(slackbot_settings.API_TOKEN)
    slack.chat.post_message(
        'shintyoku',
        msg,
        as_user=True
        )
