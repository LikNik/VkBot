import MyData
import LongText
import vk_api
import time

loggin = MyData.MY_LOGGIN
pas = MyData.MY_PASSWORD
vk = vk_api.VkApi(login=loggin, password=pas)
vk.auth()  # authorization
print('Success')


class Bot:  # Initialization bot class
    name = ''
    face = ''

    values = {'out': 0, 'count': 100, 'offset': 0}
    response = vk.method('messages.getConversations', values)

    def write_msg(self, user_id, s):
        vk.method('messages.send', {'user_id': user_id, 'message': s})

    def send_msg(self):
        response = Bot.response
        response = vk.method('messages.getConversations', Bot.values)
        data_id = response['items'][0]['last_message']['from_id']
        last_mess = response['items'][0]['last_message']['text']
        if data_id == MyData.MY_ID:
            if last_mess == 'test':  # If last message equals texts
                response = response['items'][0]  # last message = message
                Bot.values['last_message_id'] = response['conversation']['last_message_id']
                Bot.write_msg(self, response['conversation']['peer']['id'], 'test message')
