from subprocess import call
import config


def generate_mysql_models(
        connector: str,
        filename: str
        ) -> None:
    connection_string = str(connector)
    output_file = f"{filename}.py"

    call(f"sqlacodegen {connection_string} > {output_file}", shell=True)


if __name__ == "__main__":
    generate_mysql_models(
        connector=str(config.connection_mysql),
        filename="mysql_models"
    )
