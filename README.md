# TODO console app

An example for "Dependency Injection (DI) with dependency-injector" talk.

Tools:
- [poetry](https://python-poetry.org/)
- [typer](https://typer.tiangolo.com/)
- [pydantic](https://docs.pydantic.dev/)
- [dependency-injector](https://python-dependency-injector.ets-labs.org/)
- [black](https://black.readthedocs.io/)

## Setup

```shell
poetry install
poetry shell

todopy --help
todopy set-priority --help

todopy create 'Example todo'
TEXT_COLOR=red todopy print
```
