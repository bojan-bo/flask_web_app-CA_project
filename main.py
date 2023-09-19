from website import create_app
import stripe

app = create_app()

app.config['STATIC_URL_PATH'] = '/static'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

if __name__ == '__main__':
    app.run(debug=True)
