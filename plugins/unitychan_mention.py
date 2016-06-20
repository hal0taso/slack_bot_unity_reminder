from slackbot.bot import respond_to
from slackbot.bot import listen_to



@respond_to('疲れた')
@respond_to('眠い')
@respond_to('tired')
def cheer(message):
    message.reply('ファイト!')

    
@listen_to('そういえば')
def shinchoku(message):
    message.send('<@' + message.body['channel'] + '|channel> 進捗どうですか？')
    message.react('unity-chan-face')

    
