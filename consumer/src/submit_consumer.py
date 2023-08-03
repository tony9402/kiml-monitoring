import json
import os
import time

from dotenv import load_dotenv
from kiml.github import clone_or_pull
from kiml.login import login_kiml
from kiml.submit import submit
from kiml.workspace import kiml_set_workspace
from redis_om import get_redis_connection


def consumer():
    sess = get_redis_connection(
        url=os.environ["REDIS_URL"], decode_responses=True
    )  # noqa: E501
    while True:
        values = sess.zrangebyscore(
            "submit_jobs", "-inf", 2147483646, start=0, num=1
        )  # noqa: E501
        if len(values) != 0:
            job_config = json.loads(values[0])
            sess.hset("status", job_config["uuid"], "Running")

            failed = False
            for count_of_try in range(6):
                try:
                    clone_or_pull(
                        job_config["github_url"],
                        job_config["source_directory"],  # noqa: E501
                    )
                except Exception as e:
                    print(e)
                    if count_of_try == 5:
                        failed = True
                        break
                    time.sleep(2)
                    continue
                break

            if failed:
                print("[1] Failed")
                sess.zrem("submit_jobs", values[0])
                sess.hset("status", job_config["uuid"], "Git Pull Failed")
                continue

            msg = ""
            while True:
                try:
                    submit(**job_config)
                    msg = "Success !"
                    break
                except Exception as e:
                    error_info = json.loads(e.body)
                    error_code = error_info["ecode"]
                    if error_code == "40030":
                        time.sleep(2)
                        continue
                    else:
                        failed = True
                        msg = error_info["message"]
                        break

            if failed:
                print(f"[2] Failed {values[0]}")
                sess.zrem("submit_jobs", values[0])
                sess.hset("status", job_config["uuid"], msg)
                continue

            sess.zrem("submit_jobs", values[0])
            sess.hset("status", job_config["uuid"], msg)


if __name__ == "__main__":
    load_dotenv()
    login_kiml(os.environ["KIML_ID"], os.environ["KIML_PW"])
    kiml_set_workspace(os.environ["KIML_WORKSPACE"])

    for count_of_try in range(1000):
        try:
            get_redis_connection(
                url=os.environ["REDIS_URL"], decode_responses=True
            )  # noqa: E501
            break
        except Exception:
            continue
    consumer()
