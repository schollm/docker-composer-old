# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

from typing import List, Optional

import attr

from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposePort(DockerBaseRunner):
    """
    Print the public port for a port binding.

    Usage: port [options] SERVICE PRIVATE_PORT

    """

    protocol: Optional[str] = None
    """tcp or udp [default: tcp]"""
    index: Optional[int] = None
    """index of the container if there are multiple
       instances of a service [default: 1]"""
    _cmd: str = "port"
    _options: List[str] = []
