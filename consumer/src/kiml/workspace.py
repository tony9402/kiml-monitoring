from csms.sdk.core.configuration import Config
from csms.sdk import Workspace


def kiml_set_workspace(workspace_name):
    ws = Workspace.get(workspace_name)
    config = Config.get()
    config.set(workspace_id=ws.id, workspace_name=ws.name)


if __name__ == "__main__":
    kiml_set_workspace("ssudb206")