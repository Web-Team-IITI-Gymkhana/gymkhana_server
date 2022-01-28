def create_env():
    with open(".env", "w") as f:
        f.write("ENVIRONMENT=DEVELOPMENT\n")
        f.write("PGUSER=\n")
        f.write("PGPASSWORD=\n")
        f.write("PGHOST=\n")
        f.write("PGPORT=\n")
        f.write("PGDATABASE=\n")
        f.write("SECRET_KEY=\n")
        f.write("GOOGLE_CLIENT_ID=\n")
        f.write("GOOGLE_CLIENT_SECRET=\n")
        f.write("FRONTEND_URL=")