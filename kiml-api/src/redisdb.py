import os

from dotenv import load_dotenv
from redis_om import get_redis_connection

load_dotenv()


def get_redis_sess():
    return get_redis_connection(
        url=os.environ["REDIS_URL"], decode_responses=True
    )  # noqa: E501
