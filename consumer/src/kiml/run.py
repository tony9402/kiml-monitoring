from csms.sdk import (
    Workspace,
    Run,
)
from csms.sdk.core.configuration import load_config


def get_run_by_id(run_id):
    kiml_config = load_config()
    workspace = Workspace.from_config(kiml_config)
    return Run.get_by_id(workspace, run_id)


def get_run_list():
    kiml_config = load_config()
    workspace = Workspace.from_config(kiml_config)
    return Run.list(workspace)