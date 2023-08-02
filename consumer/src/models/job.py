from typing import List

from redis_om import JsonModel


class SubmitDto(JsonModel):
    run_name: str
    experiment_name: str
    image: str
    instance_type: str
    dataset: List[str]
    source_directory: str
    command: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        extra = "allow"


class JobDto(SubmitDto):
    uuid: str
    github_url: str
