# Parsec Cloud (https://parsec.cloud) Copyright (c) AGPLv3 2016-2021 Scille SAS

import trio
import click
from urllib.request import urlopen, Request

from parsec.api.protocol import OrganizationID
from parsec.api.rest import organization_create_req_serializer, organization_create_rep_serializer
from parsec.utils import trio_run
from parsec.cli_utils import spinner, cli_exception_handler
from parsec.core.types import BackendAddr, BackendOrganizationBootstrapAddr
from parsec.core.cli.utils import cli_command_base_options


async def create_organization_req(
    organization_id: OrganizationID, backend_addr: BackendAddr, administration_token: str
) -> str:
    url = backend_addr.to_http_domain_url("/administration/organizations")
    data = organization_create_req_serializer.dumps({"organization_id": organization_id})

    def _do_req():
        req = Request(
            url=url,
            method="POST",
            headers={"authorization": f"Bearer {administration_token}"},
            data=data,
        )
        with urlopen(req) as rep:
            return rep.read()

    rep_data = await trio.to_thread.run_sync(_do_req)

    cooked_rep_data = organization_create_rep_serializer.loads(rep_data)
    return cooked_rep_data["bootstrap_token"]


async def _create_organization(
    organization_id: OrganizationID, backend_addr: BackendAddr, administration_token: str
) -> None:
    async with spinner("Creating organization in backend"):
        bootstrap_token = await create_organization_req(
            organization_id, backend_addr, administration_token
        )

    organization_addr = BackendOrganizationBootstrapAddr.build(
        backend_addr, organization_id, bootstrap_token
    )
    organization_addr_display = click.style(organization_addr.to_url(), fg="yellow")
    click.echo(f"Bootstrap organization url: {organization_addr_display}")


@click.command(short_help="create new organization")
@click.argument("organization_id", required=True, type=OrganizationID)
@click.option("--addr", "-B", required=True, type=BackendAddr.from_url, envvar="PARSEC_ADDR")
@click.option("--administration-token", "-T", required=True, envvar="PARSEC_ADMINISTRATION_TOKEN")
@cli_command_base_options
def create_organization(organization_id, addr, administration_token, debug, **kwargs):
    with cli_exception_handler(debug):
        trio_run(_create_organization, organization_id, addr, administration_token)
