from website import create_app

app = create_app()

app.config['STATIC_URL_PATH'] = '/static'

if __name__ == '__main__':
    app.run(debug=True)
