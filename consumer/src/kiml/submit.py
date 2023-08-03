import os
from typing import Dict, List, Optional
from uuid import uuid4

from csms.sdk import Dataset, Image, Workspace
from csms.sdk.core.run import generate_run_name
from csms.sdk.core.snapshot import make_tarfile
from csms.sdk.openapi_client.storage.api.code_api import CodeApi
from csms.sdk.openapi_client.training.api.run_api import RunApi
from csms.sdk.openapi_client.training.model.run_request import RunRequest
from csms.sdk.utils.flat_client import CosmosError
from csms.sdk.utils.miscutils import validate_name, validate_tag_key
from kiml.experiment import get_experiment


def send_submit(
    workspace: Workspace,
    experiment,
    src_dir: str,
    command: str,
    image: Image,
    resource_flavor: str,
    name: str,
    datasets: List[Dataset],
    replica: int = 1,
    env_vars: Dict[str, str] = {},
    description: Optional[str] = None,
    tags: Dict[str, str] = {},
):
    config = workspace.config
    training_api_client = config.get_api_client("training")
    storage_api_client = config.get_api_client("storage")
    run_api_instance = RunApi(training_api_client)
    code_api_instance = CodeApi(storage_api_client)

    domain_id, project_id, workspace_id = (
        config.domain_id,
        config.project_id,
        workspace.id,
    )

    if name is None:
        name = generate_run_name()

    errs = validate_name(name)
    if errs:
        raise CosmosError(
            f"Run.create() fails. invalid name: {name}, errs: {errs}"
        )  # noqa: E501

    if not image.path:
        raise CosmosError(
            f"Run.create() fails. missing path of run image: {image.name}."
            f" image build status may not be succeeded"
        )

    kwargs = {}
    if datasets is not None:
        kwargs["dataset_ids"] = [ds.id for ds in datasets]
    if description is not None:
        kwargs["description"] = description  # type: ignore

    if tags:
        for tag_key in tags:
            errs = validate_tag_key(tag_key)
            if errs:
                raise CosmosError(
                    f"create run fail. invalid tag key:{tag_key}, errs: {errs}"
                )

    fname = uuid4().__str__()
    fpath = f"{fname}.tar.gz"
    make_tarfile(fname, src_dir)
    with open(fpath, "rb") as f:
        code_model = code_api_instance.api_v1_domains_domain_id_projects_project_id_workspaces_workspace_id_codes_post(  # noqa: E501
            domain_id, project_id, workspace_id, upload=f
        )
    os.remove(fpath)

    r = RunRequest(
        name=name,
        experiment_id=experiment.id,
        image_id=image.id,
        command=command,
        resource_flavor=resource_flavor,
        replicas=replica,
        env_vars=env_vars,
        tags=tags,
        code_id=code_model.id,
        **kwargs,
    )

    run_api_instance.api_v1_domains_domain_id_projects_project_id_workspaces_workspace_id_runs_post(  # noqa: E501
        domain_id, project_id, workspace_id, run_request=r
    )

    return True


def submit(
    run_name: str,
    experiment_name: str,
    source_directory: str,
    command: str,
    image: str,
    instance_type: str,
    dataset: List[str],
    num_replica: int = 1,
    description: str = "",
    tags: Dict[str, str] = {},
    env_vars: Dict[str, str] = {},
    **kwargs,
):
    workspace = Workspace.from_config()
    experiment = get_experiment(workspace, experiment_name)
    image = Image.get(workspace, image)

    dataset = [Dataset.get(workspace, x) for x in dataset]

    send_submit(
        workspace,
        experiment,
        source_directory,
        command,
        image,
        instance_type,
        name=run_name,
        datasets=dataset,
        replica=num_replica,
        env_vars=env_vars,
        description=description,
        tags=tags,
    )
