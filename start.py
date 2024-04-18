import asyncio
from steam.client import SteamClient

accs_file = 'accs.txt'
from config import games

async def login_process(client, username, password) -> None:
    account_login = client.login(username=username, password=password)
    if account_login == 85:
        steamguard = str(input(f"({username})Enter Steam Guard (App): "))
        client.login(username=username, password=password, two_factor_code=steamguard)
    elif account_login == 63:
        mail = str(input(f"({username})Enter Steam Guard (Mail): "))
        client.login(username=username, password=password, auth_code=mail)
    else:
        pass

async def main():
    clients = []
    with open(accs_file, 'r') as file:
        tasks = []
        for line in file:
            login, password = line.strip().split(':')
            client = SteamClient()
            print(f'Logging in with account: {login}')
            task = asyncio.create_task(login_process(client, username=login, password=password))
            tasks.append(task)
            clients.append(client)

        await asyncio.gather(*tasks)

    for client in clients:
        client.games_played(games)
    
    client.run_forever()

if __name__ == '__main__':
    asyncio.run(main())