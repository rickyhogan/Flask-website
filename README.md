# Flask-website
 Complete website and API for AnalyzeXRP server
 
 This is a complete running server in dev. mode for API access and website testing.
 NamedWallets is the DB with SQlite containing our wallets and there title/nicknames.

- pip3 install -r requirements.txt into new virtualenv
- after all files inside directory, cd ~/Flask_Site
- from terminal, python3 server.py
- open firefox

this will show you the website

- type into field http://0.0.0.0:5000/ 

this will allow you to use API graphically

- type into field http://0.0.0.0:5000/api/ui 

this will show you full list of wallets

- type into field http://0.0.0.0:5000/api/wallets 

this will show wallet with matching 'publickey'

- type into field http://0.0.0.0:5000/api/wallets/(publickey)

this will show all wallet matching 'title'

- type into field http://0.0.0.0:5000/api/wallets/title/(title) 

use ' test_api.py ' as example in python script to extract data 
