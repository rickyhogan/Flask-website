from config import db, ma

class NamedWallets(db.Model):
    __tablename__ = 'NamedWallets'
    Id = db.Column(db.Integer, primary_key=True)
    WalletTitle = db.Column(db.String(64))
    WalletNick = db.Column(db.String(64))
    PublicKey = db.Column(db.String(64))
    Memo = db.Column(db.Text)
    
class WalletSchema(ma.ModelSchema):
    class Meta:
        model = NamedWallets
        sqla_session = db.session    
