from csms.sdk import Experiment


def get_experiment(ws, value):
    try:
        exp = Experiment.get(ws, value)
    except Exception:
        try:
            exp = Experiment.get_by_id(ws, value)
        except Exception:
            raise Exception(
                f"Experiment with value `{value}` is not found"
            ) from None  # noqa: E501
    return exp
