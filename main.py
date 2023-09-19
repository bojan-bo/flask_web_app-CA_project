from website import create_app
import stripe
# taken from and modified https://github.com/techwithtim/Flask-Web-App-Tutorial/blob/main/main.py
app = create_app()

app.config['STATIC_URL_PATH'] = '/static'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

if __name__ == '__main__':
    app.run(debug=True)
