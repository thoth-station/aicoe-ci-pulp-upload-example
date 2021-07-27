#!/usr/bin/env python3
# aicoe-hello-world
# Copyright(C) 2021 Red Hat, Inc.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Hello World CLI to send greeting to the world."""

import logging
import click as cli
from aicoe.hello_world import __version__


_LOGGER = logging.getLogger("aicoe.hello_world")
_LOGGER.info(f"This is AICoE Hello World CLI v{__version__}")


@cli.command()
def hello_world():
    """Run hello world cli."""
    cli.echo("Hello World!")


if __name__ == "__main__":
    hello_world()
