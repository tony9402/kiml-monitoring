from csms.sdk import Workspace
from csms.sdk.core.configuration import Config


def kiml_set_workspace(workspace_name):
    ws = Workspace.get(workspace_name)
    Config().set(workspace_id=ws.id, workspace_name=ws.name)
