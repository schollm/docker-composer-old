# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

import attr
from typing import Optional, List
from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposePush(DockerBaseRunner):
    """
    Pushes images for services.

    Usage: push [options] [SERVICE...]

    """

    ignore_push_failures: Optional[bool] = None
    """Push what it can and ignores images with push failures."""
    _cmd: str = "push"
    _options: List[str] = [
        "ignore_push_failures",
    ]
