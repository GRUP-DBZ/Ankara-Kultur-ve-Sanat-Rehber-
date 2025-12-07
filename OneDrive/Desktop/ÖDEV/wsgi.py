from app import create_app

# Render (gunicorn) expects a module-level variable named `app` or `application`.
app = create_app()

if __name__ == '__main__':
    # For local debugging only
    app.run(host='0.0.0.0', port=5000)
