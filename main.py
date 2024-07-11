from os import getenv
from dotenv import load_dotenv
from backend import app


load_dotenv()


if __name__ == "__main__":
    app.run(debug=int(getenv("DEBUG")), port=int(getenv("PORT")))