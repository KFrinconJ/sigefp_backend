import random
import string
from typing import Dict
from random import uniform
from datetime import date as Date
from random import randint


from fastapi.testclient import TestClient

from core.config import settings


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def get_superuser_token_headers(client: TestClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


def random_date(start: Date = Date(2021, 1, 1), end: Date = Date(2021, 12, 31)) -> Date:
    # Convertir las fechas a números reales
    start_number = start.toordinal()
    end_number = end.toordinal()
    # Generar un número real aleatorio entre las fechas
    random_number = uniform(start_number, end_number)
    # Convertir el número real a fecha
    random_date = Date.fromordinal(int(random_number))
    return random_date


def random_integer(min: int = 1, max: int = 1000) -> int:
    return randint(min, max)
