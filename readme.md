# Azure Cosmos DB for Table client library samples for Apache Gremlin


## Getting started

This repo has a [devcontainer](https://containers.dev) environment making it easy to get started.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/cosmos-db-table-python-samples?quickstart=1)

### Run the app

Configure your Azure Cosmos DB credentials as environment variables.

```bash
export COSMOS_ENDPOINT="<cosmos-account-URI>"
export COSMOS_KEY="<cosmos-account-PRIMARY-KEY>"
```

> **💡 TIP**: If you don't have an Azure Cosmos DB account, [create a free account](https://cosmos.azure.com/try/).

Run the quickstart sample app using the [`azure-data-tables`](https://pypi.org/project/azure-data-tables/) package from PyPI.

```bash
pip install azure-data-tables
python 001-quickstart/app.py
```

### Validate any changes you make

If you change the code, run the linter and code formatter.

```bash
pip install flake8
flake8 --verbose 001-quickstart/app.py
```

```bash
pip install black
black --verbose 001-quickstart/app.py
```
