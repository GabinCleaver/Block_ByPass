import requests

class BlockBypass:
    def __init__(self, token, userId):
        self.channelId = None
        self.userId = userId
        self.api = 'https://discord.com/api/v8/'
        self.headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

    def generateChannel(self):
        request = requests.post(f'{self.api}users/@me/channels', json={'recipients': [ self.userId ]}, headers=self.headers)

        if request.status_code == 200:
            print('Création du salon\n')
            self.channelId = request.json()['id']
            self.main()
        else:
            print('Impossible de créer le salon !')
            print(request.status_code, request.json())
            exit(0)

    def sendMessage(self, message):
        request = requests.post(f'{self.api}channels/{self.channelId}/messages', json={'content': message}, headers=self.headers)

        if request.status_code == 200:
            print('Message bien envoyé\n')
        else:
            print("Erreur dans l'envoie du message ", request.json(), '\n')

        self.main()

    def main(self):
        content = input('Message a envoyer: ')

        self.sendMessage(content)

if __name__ == '__main__':
    token = input('Token: ')
    userId = input('User ID a envoyer un message: ')
    print('\n')
    yesnt = BlockBypass(token, userId)
    yesnt.generateChannel()
    yesnt.main()