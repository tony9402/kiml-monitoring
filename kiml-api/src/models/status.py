from pydantic import BaseModel


class StatusResponse(BaseModel):
    detail: str