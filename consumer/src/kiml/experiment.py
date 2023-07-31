from csms.sdk import Experiment


def get_experiment(ws, value):
    try:
        exp = Experiment.get(ws, value)
    except:
        try:
            exp = Experiment.get_by_id(ws, value)
        except:
            raise Exception(f"Experiment with value `{value}` is not found") from None
    return exp