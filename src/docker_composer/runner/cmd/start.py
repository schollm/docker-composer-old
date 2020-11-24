# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

import attr
from typing import Optional, List
from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeStart(DockerBaseRunner):
    """
    Start existing containers.

    Usage: start [SERVICE...]

    """

    _cmd: str = "start"
    _options: List[str] = []
