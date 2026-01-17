import click

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2021, type=int, help='Year of the data')
@click.option('--month', default=1, type=int, help='Month of the data')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for ingestion')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, chunksize, target_table):
    """
    Ingest taxi data into PostgreSQL in chunks.
    """
    # Example logic for handling chunks (100,000 rows by default)
    click.echo(f"Connecting to {pg_db} at {pg_host}:{pg_port} as {pg_user}...")
    click.echo(f"Ingesting {year}-{month:02d} data into {target_table} in chunks of {chunksize}...")

def main():
    print("Hello from data-engineering-zoomcamp!")


if __name__ == "__main__":
    main()
