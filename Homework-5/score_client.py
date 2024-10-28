import json
import logging
import pickle

import typer
from rich.logging import RichHandler
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from typing_extensions import Annotated

logger = logging.getLogger(__name__)
logger.addHandler(RichHandler(rich_tracebacks=True, markup=True))
logger.setLevel("INFO")


def score(input, dv: DictVectorizer, model):
    X = dv.transform(input)
    pred = model.predict_proba(X)[:, 1]
    return pred


def main(
    payload: Annotated[str, typer.Option(help="The paylod, in json format")],
    dv_file: Annotated[str, typer.Option(help="The DictVectorizer to use")] = "dv.bin",
    model_file: Annotated[str, typer.Option(help="The model to use")] = "model1.bin",
):
    with open(dv_file, "rb") as f_in:
        dv = pickle.load(f_in)
    with open(model_file, "rb") as f_in:
        model = pickle.load(f_in)

    input = json.loads(payload)

    pred = score(input, dv, model)
    logger.info(f"The predicted probabilitiy is {pred}")


if __name__ == "__main__":
    typer.run(main)
