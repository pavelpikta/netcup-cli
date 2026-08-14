"""Maintenance and ping CLI commands."""

import click

from ..api.maintenance import get_maintenance, ping
from ..exceptions import APIError, ConfigError
from ..output import print_json


@click.group("maintenance", help="Maintenance info (deprecated) and API ping.")
def maintenance_group():
    pass


@maintenance_group.command("ping", help="Check if SCP API is available.")
def ping_cmd() -> None:
    try:
        result = ping()
    except Exception as e:
        click.echo(click.style(str(e), fg="red"), err=True)
        raise SystemExit(1) from e
    click.echo(result)


@maintenance_group.command(
    "info",
    help="Get maintenance window information. Deprecated; API removal by 31.12.2026.",
)
def info() -> None:
    click.echo(
        click.style(
            "Warning: GET /api/v1/maintenance is deprecated and will be removed by 31.12.2026.",
            fg="yellow",
        ),
        err=True,
    )
    try:
        data = get_maintenance()
    except (APIError, ConfigError) as e:
        click.echo(click.style(str(e), fg="red"), err=True)
        raise SystemExit(1) from e
    print_json(data)
