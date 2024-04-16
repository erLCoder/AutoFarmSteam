from steam.client import SteamClient, EResult

client = SteamClient()

def get_username():
    username = str(input("Введите логин: "))
    get_password(username)

def get_password(username):
    password = str(input("Введите пароль: "))
    login_process(username, password)

def login_process(username, password) -> None:
    account_login = client.login(username=username, password=password)
    games = ['730']
    if account_login == 85:
        steamguard = str(input("Enter Steam Guard (App): "))
        client.login(username=username, password=password, two_factor_code=steamguard)
        print('Script is running!')
        while True:
            client.games_played(games)
            client.run_forever()
    elif account_login == 63:
        mail = str(input("Enter Steam Guard (Mail): "))
        client.login(username=username, password=password, auth_code=mail)
        print('Script is running!')
        while True:
            client.games_played(games)
            client.run_forever()
    elif account_login == 1:
        print('Script is running!')
        while True:
            client.games_played(games)
            client.run_forever()
    else:
        print("An unexpected error occurred!")

if __name__ == '__main__':
    get_username()
