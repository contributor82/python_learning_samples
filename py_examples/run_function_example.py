"""Module for running function example."""


class RunFunc:
    """Class for running function example."""

    def __init__(self):
        """Initialize class."""
        pass

    def generate_report(self, main_tank: int, external_tank: int, hydrogen_tank: int):
        """Generate report."""
        output: str = f"""Fuel Report:
        Main tank: {main_tank}
        External tank: {external_tank}
        Hydrogen tank: {hydrogen_tank}
        """
        print(output)


if __name__ == "__main__":
    run_func = RunFunc()
    run_func.generate_report(100, 200, 300)
