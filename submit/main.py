import argparse

import requests
import yaml

IP = "xxx.xxx.xxx.xxx"
PORT = "8000"
URL = f"http://{IP}:{PORT}/submit"


def load_run_config(path):
    with open(path, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg("--yaml", type=str, required=True)
    args = parser.parse_args()

    config_files = load_run_config(args.yaml)
    headers = {"Content-Type": "application/json"}
    for run_task in config_files["runs"]:
        result = requests.post(URL, headers=headers, json=run_task)
