from Analyzexrp_api import query_all_wallets
    
query = query_all_wallets()

# Examples to extract specfic objects
for example in query:
    number = example['Id']
    if number == 23:
        print(number)
        
for example in query:
    title = example['WalletTitle']
    if title == 'ripple':
        print(title)
        
for example in query:
    nick = example['WalletNick']
    if nick == 'unknown':
        print(nick)
        
for example in query:    
    pkey = example['PublicKey']
    if pkey == 'r96HghtYDxvpHNaru1xbCQPcsHZwqiaENE':
        print(pkey)
        
for example in query:
    mem = example['Memo']
    if mem == 'discord spreadsheet':
        print(mem)
