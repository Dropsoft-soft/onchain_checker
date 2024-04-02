import requests
import pandas as pd
import os

payload = '8ce462692bb85ea7355ce146754141c39b931344fbb1e70f95db56f9cdded002'
timestamp = '1711985703'


wallets = [
    "0x998a9041eb503bd24911dd29cff557a1e6827315",
    "0xc335f8d7737a6e28e815688f87d223ff6d86da66",
    "0x45074460bd00F3FA6F1561F60f0E16cb9A7DF07a",
    "0x23eF70bD116F3DA5a1b98C72C15B96E8fB16c83a",
    "0xcD23C29E4717A02f2240C3d421f8C903AB59A34a",
    "0xC80570cc460cfadaDA9568f8Fbf65F6D51775959",
    "0xE1d849B87903D5cfA5a4E27C9ce248bDABa53498",
    "0x62c5FEaeF8c5c48C161B7Ef11730a215c983C62D",
    "0xE75d6D1b9Db75e46d16B1F49C31733dCa9C38826",
    "0x8a738128757a1abADF564D9e961EeaA047fA0e38",
    "0x3CC7E9495E2FF4f86920CCDe555E3610ef8b0907",
    "0x77929E62B51d57d8831ad5ee495e9cb06e38AcBF",
    "0x6B001FeD943Cd882FC6FD9A2E963250F5A3b9347",
    "0xC80570cc460cfadaDA9568f8Fbf65F6D51775959",
    "0x171D390339c256C3e20d5e157fC7f5aF2E02a8E8",
    "0x697649C1E3c7DA4c88352D97FcF138D9364366E1",
    "0x596Ea4B7E6129e0a410A60c8E79A54F08970EC2b",
    "0x0FCC27572508bf16F56B64b8320C9860ee39aCd5",
    "0x93781B94B74a5c1c36F1853D12A97011dBC65F6a",
    "0xC80570cc460cfadaDA9568f8Fbf65F6D51775959",
    "0xaA7a36207b32673a4F12Bd980739EDb1eF870614",
    "0x76CFa34EF3Af5F4a1716292492dee18336C3211f",
    "0xBc239d2D371eFd72dc1caEe9ba5c51d11808DF88",
    "0xdedBE3E563F6bbD072792fb64C2E2e9833E971aE",
    "0x8d047C009a8d583E74e7CeFB7d5abAD1160cf1A8",
    "0x3ffD38FD6cd2E989c7CA57eA5f4Ed6Cce0cA5B66",
    "0x8a738128757a1abADF564D9e961EeaA047fA0e38",
    "0x86F7125ABE9Ba5083A1E291E8cfCd8F76ADf62Ee",
    "0x45074460bd00F3FA6F1561F60f0E16cb9A7DF07a",
    "0xebbc1c63C040E954e003919cC64E4798e32b4C3d",
    "0xae5040388a1F05A14efC2E3ee0a8a91C1C3D4950",
    "0xB753202Bc641e71e22bC741ee38b61668F0a428c",
    "0x744DBdf5e903519b7f19039A28c4Ceb83280BB86",
    "0x29E95765dEF20D82860262FEFD33aa2f4a462633",
    "0xebbc1c63C040E954e003919cC64E4798e32b4C3d",
    "0x16f411B16A15540B550769EE2DB1F54c3a146f60",
    "0x2b8E98Af908BD01A6B46FFac4D9adbAcb914040d",
    "0x3ffD38FD6cd2E989c7CA57eA5f4Ed6Cce0cA5B66",
    "0x735454da146f7b8bEe00d20dC9E27841eb31f8E9",
    "0x207b037e1c88c5c110fF418105e5041e19f545EC",
    "0xb2e81e3614b8f73Aa8b40c5acB42CC0B2552e6f5",
    "0x1Ef2d7cF8c00B71b0F5865A79Ec0A2dFa3171705",
    "0xfDA359Ce3120d3e8701D86BDF416733d5154404A"
]

def arkhamintelligence(page_size, wallet):
    print("arkhamintelligence")
    url = 'https://api.arkhamintelligence.com/transfers'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,fr-CA;q=0.6,fr;q=0.5,es-US;q=0.4,es;q=0.3,de-DE;q=0.2,de;q=0.1,ru-UA;q=0.1,ru;q=0.1',
        'dnt': '1',
        'origin': 'https://platform.arkhamintelligence.com',
        'referer': 'https://platform.arkhamintelligence.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-payload': payload,
        'x-timestamp': timestamp
    }

    params = {
        'sortKey': 'time',
        'sortDir': 'desc',
        'limit': page_size,
        'offset': '0',
        'flow': 'all',
        'base': wallet,
        'usdGte': '0.1'
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(f'debank {response.status_code}')

    if response.status_code == 200:
        try:
            data = response.json()

            # Extracting and saving desired fields
            transfers = data['transfers']
            filtered_transfers = [transfer for transfer in transfers if transfer.get('toIsContract')]
            return filtered_transfers, response.status_code
        except ValueError as e:
            print("Error decoding JSON:", e)
            print("Response content:", response.content)
    else:
        print("Request failed with status code:", response.status_code)


def add_transfers_to_excel(transfers, excel_filename, temp_wallet):
    if not os.path.exists(excel_filename):
        df = pd.DataFrame(columns=[
            "Wallet", "ID", "From Address", "Predicted Entity Name", "To Address", "From Chain"
        ])
    else:
        df = pd.read_excel(excel_filename)

    for index, transfer in enumerate(transfers):
        new_row = {
            "Wallet": temp_wallet,
            "ID": transfer.get('id', 'N/A'),
            "From Address": transfer.get('fromAddress', {}).get('address', 'N/A'),
            "Predicted Entity Name": transfer.get('fromAddress', {}).get('predictedEntity', {}).get('name', 'N/A'),
            "To Address": transfer.get('toAddress', {}).get('address', 'N/A'),
            "From Chain": transfer.get('fromAddress', {}).get('chain', 'N/A'),
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    df.to_excel(excel_filename, index=False)

    print("Transfers information has been saved to", excel_filename)


def get_transactions_count(wallet):
    url = 'https://api.arkhamintelligence.com/transfers'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,uk-UA;q=0.8,uk;q=0.7,fr-CA;q=0.6,fr;q=0.5,es-US;q=0.4,es;q=0.3,de-DE;q=0.2,de;q=0.1,ru-UA;q=0.1,ru;q=0.1',
        'dnt': '1',
        'origin': 'https://platform.arkhamintelligence.com',
        'referer': 'https://platform.arkhamintelligence.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-payload': payload,
        'x-timestamp': timestamp
    }

    params = {
        'sortKey': 'time',
        'sortDir': 'desc',
        'limit': 1,
        'offset': '0',
        'flow': 'all',
        'base': wallet,
        'usdGte': '0.1'
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(f'get_transactions_count {response.status_code}')

    if response.status_code == 200:
        try:
            data = response.json()
            return data['count']

        except ValueError as e:
            print("Error decoding JSON:", e)
            print("Response content:", response.content)
    else:
        print("Request failed with status code:", response.status_code)


if __name__ == '__main__':
    transfers_map = {}

    for wallet in wallets:
        i = get_transactions_count(wallet)
        transfers, response = arkhamintelligence(i, wallet)
        size_of_transfers = len(transfers)
        print(f'{wallet} > {i} > code:{response} > size:{size_of_transfers}')
        if wallet in transfers_map:
            transfers_map[wallet].append(transfers)
        else:
            transfers_map[wallet] = [transfers]

    for wallet_address, transfers_list in transfers_map.items():
        print("Wallet Address:", wallet_address)

        for index, transfer in enumerate(transfers_list):
            add_transfers_to_excel(transfer, 'report.xlsx', wallet_address)
