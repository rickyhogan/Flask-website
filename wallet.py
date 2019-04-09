"""
Rest API DB information
"""
from flask import (
    make_response,
    abort,
)

from config import db
from models import (
    NamedWallets,
    WalletSchema,
)


def read_all():
    """
    This function responds to a request for /api/wallets
    with the complete lists of wallets
    return:        json string of list of wallets
    """
    
    # Create the list of people from our data
    nw = NamedWallets.query \
        .order_by(NamedWallets.Id) \
        .all()
        
    # Serialize the data for the response
    schema = WalletSchema(many=True)
    return schema.dump(nw).data

def read_key(pubkey):
    """
    This function responds to a request for /api/Wallets/{pubkey}
    with one matching wallet from db
    :param publickey:   Public Key of wallet to find
    :return:            Wallet Information matching Public Key
    """
    
    nw = NamedWallets.query \
        .filter(NamedWallets.PublicKey == pubkey) \
        .one_or_none()
        
    if nw is not None:
        # Serialize the data for the response
        schema = WalletSchema()
        return schema.dump(nw).data
    else:
        abort(404, 'Wallet not found for Public Key: {pubkey}'.format(pubkey=pubkey))

def read_title(title):
    """
    This function responds to a request for /api/Wallets/{title}
    with all matching Title from db
    :param title:   Title of wallet to find
    :return:            Wallet Information matching Title
    """
    
    nw = NamedWallets.query \
        .order_by(NamedWallets.Id) \
        .filter(NamedWallets.WalletTitle == title) \
        .all()
        
    if nw is not None:
        # Serialize the data for the response
        schema = WalletSchema(many=True)
        return schema.dump(nw).data
    else:
        abort(404, 'Title not found in DB: {title}'.format(title=title))
