def create_env():
    with open(".env", "w") as f:
        f.write("ENVIRONMENT=DEVELOPMENT\n")
        f.write("DATABASE_USERNAME=\n")
        f.write("DATABASE_PASSWORD=\n")
        f.write("DATABASE=\n")
        f.write("SECRET_KEY=\n")
        f.write("GOOGLE_CLIENT_ID=\n")
        f.write("GOOGLE_CLIENT_SECRET=\n")
        f.write("FRONTEND_URL=")
    print("Fill credentials in .env file")