import click
import json
from rootshell_platform_api.adapters.IssuesAPIClient import IssuesAPIClient
from rootshell_platform_api.services.paginators.paginator import APIPaginator
from rootshell_platform_api.services.exporters.exporter import CsvExporter
from rootshell_platform_api.services.exporters.exporter import JsonExporter

@click.command()
@click.option("-l", "--limit", type=int, default=10, help="Pagination limit")
@click.option("-p", "--page", type=int, default=1, help="Pagination page")
@click.option("-s", "--search", type=str, help="Pagination search")
@click.option("-c", "--orderByColumn", default="name", type=str, help="Pagination order by column")
@click.option(
    "-d",
    "--orderByDirection",
    type=click.Choice(["asc", "desc"]),
    help="Pagination order by direction",
    default="asc"
)
@click.option(
    "-e",
    "--export",
    type=click.Choice(["json", "csv"]),
    help="Export format"
)
@click.option(
    "-f",
    "--file",
    type=str,
    help="File path for export"
)
def get_paginated(limit, page, search, orderbycolumn, orderbydirection, export, file):
    api_client = IssuesAPIClient()

    try:
        if export and file:
            paginator = APIPaginator()
            all_data = paginator.fetch_all(
                client=api_client,
                limit=limit,
                page=page,
                search=search,
                orderByColumn=orderbycolumn,
                orderByDirection=orderbydirection
            )

            if export == "json":
                export_strategy = JsonExporter()
            elif export == "csv":
                export_strategy = CsvExporter()
            else:
                raise ValueError("Unsupported export format")

            export_strategy.export(all_data, file)
            click.echo(f"Data exported to {file}")
        else:
            response = api_client.get_entities(
                limit=limit,
                page=page,
                search=search,
                orderByColumn=orderbycolumn,
                orderByDirection=orderbydirection,
            )
            click.echo(json.dumps(response["data"], indent=4))

    except Exception as e:
        click.echo(f"Error occurred: {e}")

if __name__ == "__main__":
    get_paginated()
