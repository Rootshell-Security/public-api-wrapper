
A project to access Rootshell's Public API built with [poetry](https://python-poetry.org/)

---

## Installation

Install poetry with the [link](https://python-poetry.org/docs/#installing-with-pipx)

When poetry has been installed, inside the folder run `poetry install` which
will install the dependencies for the project. 

This will also run a virtual environment
which is solely set up for this project. Run `poetry shell` to go into the environment
and use the project.

Copy the .env-example to .env and fill in the two variables. 

The `BEARER_TOKEN` can be obtained from The Platform's connected accounts.

The `API_ENDPOINT` is the endpoint for your specific tenant, for example `https://my-company.uk.vulnerability-platform.com`

---

## Usage

You can run commands using the `rootshell_platform` prefix. Running this on it's own will give
you a list of options to run. 

For example, running `rootshell_platfor projects get-paginated` 
will give you a list of paginated projects for your tenant.


---

## Copyright and License

The rootshell/public-api-wrapper library is copyright © [Rootshell Security LTD](https://www.rootshellsecurity.net/) and licensed for use under the MIT License (MIT). 

Please see [LICENSE](https://github.com/Rootshell-Security/public-api-wrapper?tab=MIT-1-ov-file) for more information.