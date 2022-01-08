import telebot
import uuid
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
API_TOKEN = 'token'
bot = telebot.TeleBot(API_TOKEN)
spoilers = {}


@bot.inline_handler(lambda query: len(query.query) > 0)
def spoiler(inline_query):
    try:
        if len(inline_query.query) > 200:
            long_message = InlineQueryResultArticle('1', 'Слишком многа букав', InputTextMessageContent('Сообщение слишком длинное, сократи его!'),
                description='Created by Zeus428',
                thumb_url='https://cdn-icons-png.flaticon.com/512/4522/4522081.png')
            bot.answer_inline_query(inline_query.id, [long_message], is_personal=True, cache_time=10)
        
        else:
            id = str(uuid.uuid4())
            if '@' in inline_query.query:
                message = list(filter(None, inline_query.query.split('@')))
                spoilers[id] = {'message':message[0][:-1], 'people':', '.join(['@' + s for s in message[1:]])}
                button_personal = InlineKeyboardMarkup().row(InlineKeyboardButton("Посмотреть", callback_data=f"spoiler={id}=personal={inline_query.from_user.username}"))
                button_except = InlineKeyboardMarkup().row(InlineKeyboardButton("Посмотреть", callback_data=f"spoiler={id}=except={inline_query.from_user.username}"))

                for_person = InlineQueryResultArticle('2', 'Сообщение только для ' + spoilers[id]['people'],
                    InputTextMessageContent('Специально для ' + spoilers[id]['people']),
                    reply_markup=button_personal,
                    description='Created by Zeus428',
                    thumb_url='https://cdn-icons-png.flaticon.com/512/3064/3064155.png')

                except_person = InlineQueryResultArticle('3', 'Всем кроме  ' + spoilers[id]['people'],
                    InputTextMessageContent('Для всех кроме '  + spoilers[id]['people']),
                    reply_markup=button_except,
                    description='Created by Zeus428',
                    thumb_url='https://cdn-icons-png.flaticon.com/512/38/38488.png')

                bot.answer_inline_query(inline_query.id, [for_person, except_person], is_personal=True, cache_time=10)

            else:
                button_public = InlineKeyboardMarkup().row(InlineKeyboardButton("Посмотреть", callback_data=f"spoiler={id}=public=none"))
                spoilers[id] = {'message':inline_query.query, 'people':'none'}
                public_message = InlineQueryResultArticle('1', 'Публичное сообщение',
                    InputTextMessageContent('Сообщение для всех'),
                    reply_markup=button_public,
                    description='Created by Zeus428',
                    thumb_url='https://cdn-icons-png.flaticon.com/512/65/65000.png')

                bot.answer_inline_query(inline_query.id, [public_message], is_personal=True, cache_time=10)

    except Exception as e:
        print('*****')
        print("Warning!", e.__class__, "occurred.", 'Function: spoiler')
        print('Details: ' + str(e))


@bot.callback_query_handler(func=lambda call: call.data.startswith("spoiler="))
def spoiler_check(call):
    try:
        data = call.data.split('=')
        id, mode, sender = data[1], data[2], data[3]

        if id in spoilers:
            people = spoilers[id]['people']
            if (sender == call.from_user.username or call.from_user.username in people) and mode == 'personal':
                bot.answer_callback_query(call.id, spoilers[id]['message'], True)

            elif (sender == call.from_user.username or call.from_user.username not in people) and mode == 'except':
                bot.answer_callback_query(call.id, spoilers[id]['message'], True)

            elif people == 'none' and mode == 'public':
                bot.answer_callback_query(call.id, spoilers[id]['message'], True)

            else:
                bot.answer_callback_query(call.id, 'Это сообщение не для тебя, дружок!')
        else:
            bot.edit_message_text(text='Сообщение в сумраке', inline_message_id=call.inline_message_id, reply_markup=None)
            bot.answer_callback_query(call.id)
    
    except Exception as e:
        print('*****')
        print("Warning!", e.__class__, "occurred.", 'Function: spoiler_check')
        print('Details: ' + str(e))


bot.infinity_polling()
