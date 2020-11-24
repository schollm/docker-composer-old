# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

import attr
from typing import Optional, List
from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeEvents(DockerBaseRunner):
    """
    Receive real time events from containers.

    Usage: events [options] [SERVICE...]

    """

    json: Optional[bool] = None
    """Output events as a stream of json objects"""
    _cmd: str = "events"
    _options: List[str] = [
        "json",
    ]