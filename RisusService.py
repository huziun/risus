import aiogram
import config


class RisusFilter(aiogram.dispatcher.filters.Filter):

    def __init__(self ):

        self.target = 820980192

    async def check(self, message) -> bool:
        print(message.from_user.id )
        return message.from_user.id == self.target;

class Risus:

    def __init__(self, message,bot):
        self.id = message.chat.id
        self.message = message
        self.bot = bot
    def responseToText(self):

        return self.bot.send_sticker(chat_id=self.id,sticker=config.stupid_cat, reply_to_message_id=self.message.message_id);

    def responseToSticker(self, sticker):
        if(sticker == "AgADhwEAAixg9Rw"):
            return self.bot.send_sticker(chat_id=self.id, sticker=config.suck_dick_cat,
                                  reply_to_message_id=self.message.message_id);
        else:
            return self.responseToText();
