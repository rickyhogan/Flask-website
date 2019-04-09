import json
from urllib.request import Request, urlopen

def _url(path):
    return 'http://localhost:5000/api' + path

def print_all_wallets():
    url = _url('/wallets')

    request = Request(method='GET', url=url)
    try:
        with urlopen(request) as res:
            res_json = json.loads(res.fp.read().decode('utf-8'))
            for all_wallets in res_json:
                print('{} {} {} {} {}'.format(all_wallets['Id'], all_wallets['WalletTitle'],
                                              all_wallets['WalletNick'], all_wallets['PublicKey'],
                                              all_wallets['Memo']))
    except Exception as err:
        return {"status": "error", "error": err}

def print_from_title(title):
    url = _url('/wallets/title/' + title)
    request = Request(method='GET', url=url)
    try:
        with urlopen(request) as res:
            res_json = json.loads(res.fp.read().decode('utf-8'))
            for titles in res_json:
                print('{} {} {} {} {}'.format(titles['Id'], titles['WalletTitle'],
                                              titles['WalletNick'], titles['PublicKey'],
                                              titles['Memo']))
    except Exception as err:
        return {"status": "error", "error": err}

def print_from_key(pubkey):
    url = _url('/wallets/' + pubkey)
    request = Request(method='GET', url=url)
    try:
        with urlopen(request) as res:
            res_json = json.loads(res.fp.read().decode('utf-8'))
            print(res_json)
    except Exception as err:
        return {"status": "error", "error": err}

def query_all_wallets():
    url = _url('/wallets')

    request = Request(method='GET', url=url)
    try:
        with urlopen(request) as res:
            res_json = json.loads(res.fp.read().decode('utf-8'))
            return res_json
    except Exception as err:
        return {"status": "error", "error": err}
