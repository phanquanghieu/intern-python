from flask_redis import create_app

app = create_app()

if __name__ == '__main__':
    app.run()