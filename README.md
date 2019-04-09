# Flask-website
Complete website and API for AnalyzeXRP server

pip3 install -r requirements.txt into new virtualenv

complete running server in dev. mode for API access and website testing.

open firefox
type into field ' http://0.0.0.0:5000/ '
this will show the website

type into field ' http://0.0.0.0:5000/api/ui '
this will allow you to use API graphically

type into field ' http://0.0.0.0:5000/api/wallets '
this will show you full list of wallets

type into field ' http://0.0.0.0:5000/api/wallets/<publickey> '
this will show wallet with matching <publickey>

type into field ' http://0.0.0.0:5000/api/wallets/title/<title> '
this will show all wallet matching <title>  
