# dbt-lint

A simple linter for dbt (Data Build Tool) projects, designed to help you maintain clean and consistent SQL code in your dbt models. `dbt-lint` focuses on enforcing SQL style guidelines such as using leading commas, uppercase SQL keywords, and lowercase for everything else, ensuring your dbt project adheres to your business's specific coding standards.

## Installation

`dbt-lint` is built with Python and can be easily installed using Poetry. Ensure you have Poetry installed; if not, follow the installation instructions on the [Poetry website](https://python-poetry.org/docs/).

To install `dbt-lint`, clone the repository and run the following command within the cloned directory:

```bash
poetry install
```

This command creates a virtual environment and installs all necessary dependencies.

## Usage

After installation, you can run `dbt-lint` to lint your dbt project files. Here's a basic example:

```bash
poetry run dbt-lint --file path/to/your/model.sql
```

Replace `path/to/your/model.sql` with the actual path to the SQL file you want to lint.

### Options

- `--file`: Specify the SQL file to lint.
- `--uppercase`: Enable or disable uppercase SQL keywords. Default is enabled.
- `--leading-comma`: Enable or disable leading commas. Default is enabled.

## Contributing

We welcome contributions to `dbt-lint`! If you have suggestions for improvements or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Develop your changes and ensure they adhere to the project's coding standards.
4. Submit a pull request with a clear description of your changes.

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more detailed information on contributing.

## Reporting Issues

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/your-github-username/dbt-lint/issues) on GitHub with a detailed description of the problem or suggestion. Include any relevant details that could help us understand or reproduce the issue.

## License

`dbt-lint` is open source and available under the [MIT License](LICENSE).
