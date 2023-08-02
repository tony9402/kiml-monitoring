from csms.sdk import Run, Workspace


def get_run_by_id(run_id):
    workspace = Workspace.from_config()
    return Run.get_by_id(workspace, run_id)


def get_run_list():
    workspace = Workspace.from_config()
    return Run.list(workspace)
