import os

from dotenv.main import dotenv_values, load_dotenv
from app import create_app

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.secret"),
    **os.environ,
}
load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(host=os.environ.get("HOST", "0.0.0.0"),
            port=int(os.environ.get("PORT", 5001)),
            debug=os.environ.get("DEBUG", False))
