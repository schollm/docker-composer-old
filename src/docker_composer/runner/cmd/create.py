# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

import attr
from typing import Optional, List
from docker_composer.base import DockerBaseRunner


@attr.s(auto_attribs=True)
class DockerComposeCreate(DockerBaseRunner):
    """
    Creates containers for a service.
    This command is deprecated. Use the `up` command with `--no-start` instead.

    Usage: create [options] [SERVICE...]

    """

    force_recreate: Optional[bool] = None
    """Recreate containers even if their configuration and
       image haven't changed. Incompatible with --no-recreate."""
    no_recreate: Optional[bool] = None
    """If containers already exist, don't recreate them.
       Incompatible with --force-recreate."""
    no_build: Optional[bool] = None
    """Don't build an image, even if it's missing."""
    build: Optional[bool] = None
    """Build images before creating containers."""
    _cmd: str = "create"
    _options: List[str] = [
        "force_recreate",
        "no_recreate",
        "no_build",
        "build",
    ]
