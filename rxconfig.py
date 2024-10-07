import reflex as rx
from dotenv import load_dotenv
# from sqlalchemy.engine import URL
import os

load_dotenv()


# url_object = URL.create(
#     "postgresql+psycopg2",
#     username=os.getenv("SUPABASE_USER"),
#     password=os.getenv("SUPABASE_PASSWORD"),
#     host=os.getenv("SUPABASE_HOST"),
#     database=os.getenv("SUPABASE_DBNAME"),
#     port=os.getenv("SUPABASE_PORT")
# )


config = rx.Config(
    app_name="footstats_reflex",
    db_url=os.getenv("DB_URL")
)

