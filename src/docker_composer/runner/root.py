# DO NOT EDIT: Autogenerated by src/docker_composer/_utils/generate_class.py
# for docker-compose version 1.25.0, build unknown

import attr
from typing import Optional, List
from docker_composer.base import DockerBaseRunner
import docker_composer.runner.cmd.run
import docker_composer.runner.cmd.build
import docker_composer.runner.cmd.events
import docker_composer.runner.cmd.images
import docker_composer.runner.cmd.start
import docker_composer.runner.cmd.ps
import docker_composer.runner.cmd.unpause
import docker_composer.runner.cmd.scale
import docker_composer.runner.cmd.top
import docker_composer.runner.cmd.version
import docker_composer.runner.cmd.port
import docker_composer.runner.cmd.pause
import docker_composer.runner.cmd.restart
import docker_composer.runner.cmd.help
import docker_composer.runner.cmd.config
import docker_composer.runner.cmd.exec
import docker_composer.runner.cmd.kill
import docker_composer.runner.cmd.create
import docker_composer.runner.cmd.stop
import docker_composer.runner.cmd.rm
import docker_composer.runner.cmd.bundle
import docker_composer.runner.cmd.push
import docker_composer.runner.cmd.down
import docker_composer.runner.cmd.logs
import docker_composer.runner.cmd.pull
import docker_composer.runner.cmd.up


@attr.s(auto_attribs=True)
class DockerComposeRoot(DockerBaseRunner):
    """
    Define and run multi-container applications with Docker.

    Usage:
      docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
      docker-compose -h|--help

    """

    file: Optional[str] = None
    """Specify an alternate compose file
       (default: docker-compose.yml)"""
    project_name: Optional[str] = None
    """Specify an alternate project name
       (default: directory name)"""
    verbose: Optional[bool] = None
    """Show more output"""
    log_level: Optional[int] = None
    """Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)"""
    no_ansi: Optional[bool] = None
    """Do not print ANSI control characters"""
    host: Optional[str] = None
    """Daemon socket to connect to"""
    tls: Optional[bool] = None
    """Use TLS; implied by --tlsverify"""
    tlscacert: Optional[str] = None
    """Trust certs signed only by this CA"""
    tlscert: Optional[str] = None
    """Path to TLS certificate file"""
    tlskey: Optional[str] = None
    """Path to TLS key file"""
    tlsverify: Optional[bool] = None
    """Use TLS and verify the remote"""
    skip_hostname_check: Optional[bool] = None
    """Don't check the daemon's hostname against the
       name specified in the client certificate"""
    project_directory: Optional[str] = None
    """Specify an alternate working directory
       (default: the path of the Compose file)"""
    compatibility: Optional[bool] = None
    """If set, Compose will attempt to convert keys
       in v3 files to their non-Swarm equivalent"""
    env_file: Optional[str] = None
    """Specify an alternate environment file"""
    _cmd: str = ""
    _options: List[str] = [
        "verbose",
        "no_ansi",
        "tls",
        "tlsverify",
        "skip_hostname_check",
        "compatibility",
    ]

    def build(
        self,
        build_arg: Optional[dict] = None,
        compress: Optional[bool] = None,
        force_rm: Optional[bool] = None,
        memory: Optional[int] = None,
        no_cache: Optional[bool] = None,
        no_rm: Optional[bool] = None,
        parallel: Optional[bool] = None,
        progress: Optional[str] = None,
        pull: Optional[bool] = None,
        quiet: Optional[bool] = None,
    ) -> docker_composer.runner.cmd.build.DockerComposeBuild:
        """
        Build or rebuild services.

        Services are built once and then tagged as `project_service`,
        e.g. `composetest_db`. If you change a service's `Dockerfile` or the
        contents of its build directory, you can run `docker-compose build` to rebuild it.

        Usage: build [options] [--build-arg key=val...] [SERVICE...]


        :param build_arg: Set build-time variables for services.
        :param compress: Compress the build context using gzip.
        :param force_rm: Always remove intermediate containers.
        :param memory: Set memory limit for the build container.
        :param no_cache: Do not use cache when building the image.
        :param no_rm: Do not remove intermediate containers after a successful build.
        :param parallel: Build images in parallel.
        :param progress: Set type of progress output (auto, plain, tty).
           EXPERIMENTAL flag for native builder.
           To enable, run with COMPOSE_DOCKER_CLI_BUILD=1)
        :param pull: Always attempt to pull a newer version of the image.
        :param quiet: Don't print anything to STDOUT
        """
        runner = docker_composer.runner.cmd.build.DockerComposeBuild(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def bundle(
        self, push_images: Optional[bool] = None, output: Optional[str] = None
    ) -> docker_composer.runner.cmd.bundle.DockerComposeBundle:
        """
        Generate a Distributed Application Bundle (DAB) from the Compose file.

        Images must have digests stored, which requires interaction with a
        Docker registry. If digests aren't stored for all images, you can fetch
        them with `docker-compose pull` or `docker-compose push`. To push images
        automatically when bundling, pass `--push-images`. Only services with
        a `build` option specified will have their images pushed.

        Usage: bundle [options]


        :param push_images: Automatically push images for any services
           which have a `build` option specified.
        :param output: Path to write the bundle file to.
           Defaults to "<project name>.dab".
        """
        runner = docker_composer.runner.cmd.bundle.DockerComposeBundle(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def config(
        self,
        resolve_image_digests: Optional[bool] = None,
        no_interpolate: Optional[bool] = None,
        quiet: Optional[bool] = None,
        services: Optional[bool] = None,
        volumes: Optional[bool] = None,
        hash: Optional[str] = None,
    ) -> docker_composer.runner.cmd.config.DockerComposeConfig:
        """
        Validate and view the Compose file.

        Usage: config [options]


        :param resolve_image_digests: Pin image tags to digests.
        :param no_interpolate: Don't interpolate environment variables
        :param quiet: Only validate the configuration, don't print
           anything.
        :param services: Print the service names, one per line.
        :param volumes: Print the volume names, one per line.
        :param hash: Print the service config hash, one per line.
           Set "service1,service2" for a list of specified services
           or use the wildcard symbol to display all services
        """
        runner = docker_composer.runner.cmd.config.DockerComposeConfig(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def create(
        self,
        force_recreate: Optional[bool] = None,
        no_recreate: Optional[bool] = None,
        no_build: Optional[bool] = None,
        build: Optional[bool] = None,
    ) -> docker_composer.runner.cmd.create.DockerComposeCreate:
        """
        Creates containers for a service.
        This command is deprecated. Use the `up` command with `--no-start` instead.

        Usage: create [options] [SERVICE...]


        :param force_recreate: Recreate containers even if their configuration and
           image haven't changed. Incompatible with --no-recreate.
        :param no_recreate: If containers already exist, don't recreate them.
           Incompatible with --force-recreate.
        :param no_build: Don't build an image, even if it's missing.
        :param build: Build images before creating containers.
        """
        runner = docker_composer.runner.cmd.create.DockerComposeCreate(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def down(
        self,
        rmi: Optional[str] = None,
        volumes: Optional[bool] = None,
        remove_orphans: Optional[bool] = None,
        timeout: Optional[int] = None,
    ) -> docker_composer.runner.cmd.down.DockerComposeDown:
        """
        Stops containers and removes containers, networks, volumes, and images
        created by `up`.

        By default, the only things removed are:

        - Containers for services defined in the Compose file
        - Networks defined in the `networks` section of the Compose file
        - The default network, if one is used

        Networks and volumes defined as `external` are never removed.

        Usage: down [options]


        :param rmi: Remove images. Type must be one of:
           'all': Remove all images used by any service.
           'local': Remove only images that don't have a
           custom tag set by the `image` field.
        :param volumes: Remove named volumes declared in the `volumes`
           section of the Compose file and anonymous volumes
           attached to containers.
        :param remove_orphans: Remove containers for services not defined in the
           Compose file
        :param timeout: Specify a shutdown timeout in seconds.
           (default: 10)
        """
        runner = docker_composer.runner.cmd.down.DockerComposeDown(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def events(
        self, json: Optional[bool] = None
    ) -> docker_composer.runner.cmd.events.DockerComposeEvents:
        """
        Receive real time events from containers.

        Usage: events [options] [SERVICE...]


        :param json: Output events as a stream of json objects
        """
        runner = docker_composer.runner.cmd.events.DockerComposeEvents(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def exec(
        self,
        detach: Optional[bool] = None,
        privileged: Optional[bool] = None,
        user: Optional[str] = None,
        T: Optional[bool] = None,
        index: Optional[int] = None,
        env: Optional[dict] = None,
        workdir: Optional[str] = None,
    ) -> docker_composer.runner.cmd.exec.DockerComposeExec:
        """
        Execute a command in a running container

        Usage: exec [options] [-e KEY=VAL...] SERVICE COMMAND [ARGS...]


        :param detach: Detached mode: Run command in the background.
        :param privileged: Give extended privileges to the process.
        :param user: Run the command as this user.
        :param T: Disable pseudo-tty allocation. By default `docker-compose exec`
           allocates a TTY.
        :param index: index of the container if there are multiple
           instances of a service [default: 1]
        :param env: not supported in API < 1.25)
        :param workdir: Path to workdir directory for this command.
        """
        runner = docker_composer.runner.cmd.exec.DockerComposeExec(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def help(
        self,
    ) -> docker_composer.runner.cmd.help.DockerComposeHelp:
        """
        Get help on a command.

        Usage: help [COMMAND]



        """
        runner = docker_composer.runner.cmd.help.DockerComposeHelp(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def images(
        self, quiet: Optional[bool] = None
    ) -> docker_composer.runner.cmd.images.DockerComposeImages:
        """
        List images used by the created containers.
        Usage: images [options] [SERVICE...]


        :param quiet: Only display IDs
        """
        runner = docker_composer.runner.cmd.images.DockerComposeImages(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def kill(
        self, s: Optional[int] = None
    ) -> docker_composer.runner.cmd.kill.DockerComposeKill:
        """
        Force stop service containers.

        Usage: kill [options] [SERVICE...]


        :param s: SIGNAL to send to the container.
           Default signal is SIGKILL.
        """
        runner = docker_composer.runner.cmd.kill.DockerComposeKill(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def logs(
        self,
        no_color: Optional[bool] = None,
        follow: Optional[bool] = None,
        timestamps: Optional[bool] = None,
        tail: Optional[str] = None,
    ) -> docker_composer.runner.cmd.logs.DockerComposeLogs:
        """
        View output from containers.

        Usage: logs [options] [SERVICE...]


        :param no_color: Produce monochrome output.
        :param follow: Follow log output.
        :param timestamps: Show timestamps.
        :param tail: Number of lines to show from the end of the logs
           for each container.
        """
        runner = docker_composer.runner.cmd.logs.DockerComposeLogs(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def pause(
        self,
    ) -> docker_composer.runner.cmd.pause.DockerComposePause:
        """
        Pause services.

        Usage: pause [SERVICE...]



        """
        runner = docker_composer.runner.cmd.pause.DockerComposePause(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def port(
        self, protocol: Optional[str] = None, index: Optional[int] = None
    ) -> docker_composer.runner.cmd.port.DockerComposePort:
        """
        Print the public port for a port binding.

        Usage: port [options] SERVICE PRIVATE_PORT


        :param protocol: tcp or udp [default: tcp]
        :param index: index of the container if there are multiple
           instances of a service [default: 1]
        """
        runner = docker_composer.runner.cmd.port.DockerComposePort(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def ps(
        self,
        quiet: Optional[bool] = None,
        services: Optional[bool] = None,
        filter: Optional[dict] = None,
        all: Optional[bool] = None,
    ) -> docker_composer.runner.cmd.ps.DockerComposePs:
        """
        List containers.

        Usage: ps [options] [SERVICE...]


        :param quiet: Only display IDs
        :param services: Display services
        :param filter: Filter services by a property
        :param all: Show all stopped containers (including those created by the run command)
        """
        runner = docker_composer.runner.cmd.ps.DockerComposePs(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def pull(
        self,
        ignore_pull_failures: Optional[bool] = None,
        parallel: Optional[bool] = None,
        no_parallel: Optional[bool] = None,
        quiet: Optional[bool] = None,
        include_deps: Optional[bool] = None,
    ) -> docker_composer.runner.cmd.pull.DockerComposePull:
        """
        Pulls images for services defined in a Compose file, but does not start the containers.

        Usage: pull [options] [SERVICE...]


        :param ignore_pull_failures: Pull what it can and ignores images with pull failures.
        :param parallel: Deprecated, pull multiple images in parallel (enabled by default).
        :param no_parallel: Disable parallel pulling.
        :param quiet: Pull without printing progress information
        :param include_deps: Also pull services declared as dependencies
        """
        runner = docker_composer.runner.cmd.pull.DockerComposePull(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def push(
        self, ignore_push_failures: Optional[bool] = None
    ) -> docker_composer.runner.cmd.push.DockerComposePush:
        """
        Pushes images for services.

        Usage: push [options] [SERVICE...]


        :param ignore_push_failures: Push what it can and ignores images with push failures.
        """
        runner = docker_composer.runner.cmd.push.DockerComposePush(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def restart(
        self, timeout: Optional[int] = None
    ) -> docker_composer.runner.cmd.restart.DockerComposeRestart:
        """
        Restart running containers.

        Usage: restart [options] [SERVICE...]


        :param timeout: Specify a shutdown timeout in seconds.
           (default: 10)
        """
        runner = docker_composer.runner.cmd.restart.DockerComposeRestart(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def rm(
        self,
        force: Optional[bool] = None,
        stop: Optional[bool] = None,
        v: Optional[bool] = None,
        all: Optional[bool] = None,
    ) -> docker_composer.runner.cmd.rm.DockerComposeRm:
        """
        Removes stopped service containers.

        By default, anonymous volumes attached to containers will not be removed. You
        can override this with `-v`. To list all volumes, use `docker volume ls`.

        Any data which is not in a volume will be lost.

        Usage: rm [options] [SERVICE...]


        :param force: Don't ask to confirm removal
        :param stop: Stop the containers, if required, before removing
        :param v: Remove any anonymous volumes attached to containers
        :param all: Deprecated - no effect.
        """
        runner = docker_composer.runner.cmd.rm.DockerComposeRm(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def run(
        self,
        detach: Optional[bool] = None,
        name: Optional[str] = None,
        entrypoint: Optional[str] = None,
        e: Optional[dict] = None,
        label: Optional[dict] = None,
        user: Optional[str] = None,
        no_deps: Optional[bool] = None,
        rm: Optional[bool] = None,
        publish: Optional[list] = None,
        service_ports: Optional[bool] = None,
        use_aliases: Optional[bool] = None,
        volume: Optional[list] = None,
        T: Optional[bool] = None,
        workdir: Optional[str] = None,
    ) -> docker_composer.runner.cmd.run.DockerComposeRun:
        """
        Run a one-off command on a service.

        For example:

            $ docker-compose run web python manage.py shell

        By default, linked services will be started, unless they are already
        running. If you do not want to start linked services, use
        `docker-compose run --no-deps SERVICE COMMAND [ARGS...]`.

            run [options] [-v VOLUME...] [-p PORT...] [-e KEY=VAL...] [-l KEY=VALUE...]
                SERVICE [COMMAND] [ARGS...]

        :param detach: Detached mode: Run container in the background, print
           new container name.
        :param name: Assign a name to the container
        :param entrypoint: Override the entrypoint of the image.
        :param e: Set an environment variable (can be used multiple times)
        :param label: Add or override a label (can be used multiple times)
        :param user: Run as specified username or uid
        :param no_deps: Don't start linked services.
        :param rm: Remove container after run. Ignored in detached mode.
        :param publish: Publish a container's port(s) to the host
        :param service_ports: Run command with the service's ports enabled and mapped
           to the host.
        :param use_aliases: Use the service's network aliases in the network(s) the
           container connects to.
        :param volume: Bind mount a volume (default [])
        :param T: Disable pseudo-tty allocation. By default `docker-compose run`
           allocates a TTY.
        :param workdir: Working directory inside the container
        """
        runner = docker_composer.runner.cmd.run.DockerComposeRun(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def scale(
        self, timeout: Optional[int] = None
    ) -> docker_composer.runner.cmd.scale.DockerComposeScale:
        """
        Set number of containers to run for a service.

        Numbers are specified in the form `service=num` as arguments.
        For example:

            $ docker-compose scale web=2 worker=3

        This command is deprecated. Use the up command with the `--scale` flag
        instead.

        Usage: scale [options] [SERVICE=NUM...]


        :param timeout: Specify a shutdown timeout in seconds.
           (default: 10)
        """
        runner = docker_composer.runner.cmd.scale.DockerComposeScale(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def start(
        self,
    ) -> docker_composer.runner.cmd.start.DockerComposeStart:
        """
        Start existing containers.

        Usage: start [SERVICE...]



        """
        runner = docker_composer.runner.cmd.start.DockerComposeStart(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def stop(
        self, timeout: Optional[int] = None
    ) -> docker_composer.runner.cmd.stop.DockerComposeStop:
        """
        Stop running containers without removing them.

        They can be started again with `docker-compose start`.

        Usage: stop [options] [SERVICE...]


        :param timeout: Specify a shutdown timeout in seconds.
           (default: 10)
        """
        runner = docker_composer.runner.cmd.stop.DockerComposeStop(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def top(
        self,
    ) -> docker_composer.runner.cmd.top.DockerComposeTop:
        """
        Display the running processes

        Usage: top [SERVICE...]



        """
        runner = docker_composer.runner.cmd.top.DockerComposeTop(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def unpause(
        self,
    ) -> docker_composer.runner.cmd.unpause.DockerComposeUnpause:
        """
        Unpause services.

        Usage: unpause [SERVICE...]



        """
        runner = docker_composer.runner.cmd.unpause.DockerComposeUnpause(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def up(
        self,
        detach: Optional[bool] = None,
        no_color: Optional[bool] = None,
        quiet_pull: Optional[bool] = None,
        no_deps: Optional[bool] = None,
        force_recreate: Optional[bool] = None,
        always_recreate_deps: Optional[bool] = None,
        no_recreate: Optional[bool] = None,
        no_build: Optional[bool] = None,
        no_start: Optional[bool] = None,
        build: Optional[bool] = None,
        abort_on_container_exit: Optional[bool] = None,
        timeout: Optional[int] = None,
        renew_anon_volumes: Optional[bool] = None,
        remove_orphans: Optional[bool] = None,
        exit_code_from: Optional[str] = None,
        scale: Optional[dict] = None,
    ) -> docker_composer.runner.cmd.up.DockerComposeUp:
        """
        Builds, (re)creates, starts, and attaches to containers for a service.

        Unless they are already running, this command also starts any linked services.

        The `docker-compose up` command aggregates the output of each container. When
        the command exits, all containers are stopped. Running `docker-compose up -d`
        starts the containers in the background and leaves them running.

        If there are existing containers for a service, and the service's configuration
        or image was changed after the container's creation, `docker-compose up` picks
        up the changes by stopping and recreating the containers (preserving mounted
        volumes). To prevent Compose from picking up changes, use the `--no-recreate`
        flag.

        If you want to force Compose to stop and recreate all containers, use the
        `--force-recreate` flag.

        Usage: up [options] [--scale SERVICE=NUM...] [SERVICE...]


        :param detach: Detached mode: Run containers in the background,
           print new container names. Incompatible with
           --abort-on-container-exit.
        :param no_color: Produce monochrome output.
        :param quiet_pull: Pull without printing progress information
        :param no_deps: Don't start linked services.
        :param force_recreate: Recreate containers even if their configuration
           and image haven't changed.
        :param always_recreate_deps: Recreate dependent containers.
           Incompatible with --no-recreate.
        :param no_recreate: If containers already exist, don't recreate
           them. Incompatible with --force-recreate and -V.
        :param no_build: Don't build an image, even if it's missing.
        :param no_start: Don't start the services after creating them.
        :param build: Build images before starting containers.
        :param abort_on_container_exit: Stops all containers if any container was
           stopped. Incompatible with -d.
        :param timeout: Use this timeout in seconds for container
           shutdown when attached or when containers are
           already running. (default: 10)
        :param renew_anon_volumes: Recreate anonymous volumes instead of retrieving
           data from the previous containers.
        :param remove_orphans: Remove containers for services not defined
           in the Compose file.
        :param exit_code_from: Return the exit code of the selected service
           container. Implies --abort-on-container-exit.
        :param scale: Scale SERVICE to NUM instances. Overrides the
           `scale` setting in the Compose file if present.
        """
        runner = docker_composer.runner.cmd.up.DockerComposeUp(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner

    def version(
        self, short: Optional[bool] = None
    ) -> docker_composer.runner.cmd.version.DockerComposeVersion:
        """
        Show version information

        Usage: version [--short]


        :param short: Shows only Compose's version number.
        """
        runner = docker_composer.runner.cmd.version.DockerComposeVersion(
            **{k: v for k, v in locals().items() if k != "self"}
        )
        runner._parent_cmd = self._call_cmd()
        return runner
