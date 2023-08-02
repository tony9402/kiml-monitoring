from dateutil import parser


def convert_run_dict(run_data):
    run_dict = {}

    run_dict["uuid"] = run_data["id"]
    run_dict["status"] = run_data["status"]
    run_dict["run_name"] = run_data["name"]
    run_dict["experiment_name"] = run_data["experiment_name"]
    run_dict["experiment_id"] = run_data["experiment_id"]
    run_dict["image"] = run_data["image_name"]
    run_dict["instance_type"] = run_data["resource_flavor"]
    run_dict["create_time"] = run_data["system_meta"]["createdAt"]
    run_dict["start_time"] = run_data.get("compute_started_at", None)
    run_dict["end_time"] = run_data.get("compute_finished_at", None)
    run_dict["create_time"] = parser.parse(run_dict["create_time"])

    return run_dict
