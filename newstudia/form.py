import requests

class BotHandler:

    def __init__(self, ):
        self.token = '1293981538:AAHA7ezfthHR0OvfcoSBS7cNuy8rk1n6NDI'
        self.api_url = "https://api.telegram.org/bot{}/".format(self.token)

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        requests.post(self.api_url + method, params)


def contact(request):
    name=request.POST.get('name', '')
    phone=request.POST.get('phone', '')
    email=request.POST.get('email', '')
    text=request.POST.get('text', '')
    data=[name,phone,email,text]
    greet_bot = BotHandler()
    data_id = [926306373,193917392]
    for i in data_id:
        greet_bot.send_message(i,'Привет тут человек хочет устроиться в дрочильню \nЕго имя: {}\nНомер телефона: {}\nАдрес элетронной почты: {}\nИ сообщение от него:\n{}'.format(*data) )