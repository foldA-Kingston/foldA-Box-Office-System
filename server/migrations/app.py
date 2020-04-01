from flask import Flask
from flask_mail import Mail, Message
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__) #or flaskapp?

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'foldaconfirmation@gmail.com'
app.config['MAIL_PASSWORD'] = 'folda2020'
app.config['MAIL_DEFAULT_SENDER'] = ('FoldA Festival of Live Digital Art','foldaconfirmation@gmail.com')
app.config['MAIL_MAX_EappS'] = 1000
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/PaymentSuccess')
def confirmEmail ():
    identity = get_jwt_identity()

    #purchased = getPurchased(identity['id']) #can you do this?
    #events = ""
    #for i in purchased["events"]:
        #events += i +", "
    
    msg = Message('Confirming Purchase', recipients=[identity['emailAddress']])
    msg.body = 'Congratulations you have purchased the following tickets: '
    mail.send(msg)
    
    return 'Message has been sent!'

if __name__ == '__main__':
    app.run()
