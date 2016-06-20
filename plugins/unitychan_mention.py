from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('疲れた')
@respond_to('眠い')
def cheer(message):
    message.reply('ファイト!')
    message.react('unity-chan-face')

    
@listen_to('そういえば')
def shinchoku(message):
    message.send('みなさん進捗どうですか？')
    message.react('unity-chan-face')

    
@listen_to('頑張って')
@listen_to('がんばれ')
def gambal(message):
    message.send('がんばってね!')

    
@listen_to('すいません')
@listen_to('ごめんなさい')
@listen_to('できませんでした')
def sorry(message):
    message.reply('これからまだまだがんばろーー！！')
    message.react('unity-chan-face')
