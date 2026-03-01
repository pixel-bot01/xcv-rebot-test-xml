from index import app

# Gunicorn looks for: wsgi:app
if __name__ == "__main__":
    app.run()