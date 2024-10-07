import reflex as rx
from dotenv import load_dotenv

load_dotenv()


config = rx.Config(
    app_name="footstats_reflex",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"]
    }
)

