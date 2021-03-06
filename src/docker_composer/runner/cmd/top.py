# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeTop(DockerBaseRunner):
    """
    Display the running processes

    Usage: top [SERVICE...]

    """

    _cmd: str = "top"
    _options: List[str] = []
