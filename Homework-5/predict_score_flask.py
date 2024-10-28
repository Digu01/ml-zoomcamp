import json
import logging

import requests
import typer
from rich.logging import RichHandler
from typing_extensions import Annotated

logger = logging.getLogger(__name__)
logger.addHandler(RichHandler(rich_tracebacks=True, markup=True))
logger.setLevel("INFO")

url = "http://localhost:9696/predict"


def score(input):
    response = requests.post(url, json=input)
    result = response.json()
    print(result)


def main(
    payload: Annotated[str, typer.Option(help="The paylod, in json format")],
):
    input = json.loads(payload)
    pred = score(input)


if __name__ == "__main__":
    typer.run(main)
