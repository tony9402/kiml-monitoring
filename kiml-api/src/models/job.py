from typing import List

from pydantic import BaseModel


class SubmitDto(BaseModel):
    github_url: str
    run_name: str
    experiment_name: str
    image: str
    instance_type: str
    dataset: List[str]
    source_directory: str
    command: str


class CancelDto(BaseModel):
    uuid: str
