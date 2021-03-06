# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeStop(DockerBaseRunner):
    """
    Stop running containers without removing them.

    They can be started again with `docker-compose start`.

    Usage: stop [options] [SERVICE...]

    """

    timeout: Optional[int] = None
    """Specify a shutdown timeout in seconds.
       (default: 10)"""
    _cmd: str = "stop"
    _options: List[str] = []
