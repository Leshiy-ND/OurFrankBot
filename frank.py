from random import randint
from requests.exceptions import ReadTimeout
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
    vk_session = VkApi(token='af4a504a0252c163712755adaa9674ad2593d7735d0e7980a83bd0793606f6bd060a660e12ede75923cf0')        # сюда вписать ключ доступа
    longpoll = VkBotLongPoll(vk_session, 118561058)    # сюда вписать id группы, только цифры
    vk = vk_session.get_api()
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if 'фрэнк' in event.object['message']['text'].lower():
                        vk.messages.send(peer_id=event.object['message']['peer_id'],
                                         random_id=randint(-2147483648, 2147483647),
                                         message='*квркх*')
        except ReadTimeout:
            pass


if __name__ == '__main__':
    main()
 
