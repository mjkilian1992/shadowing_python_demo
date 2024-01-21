# Newsletter site
## Description
This is the beginning of a site for brand that allows users to subscribe to a newsletter. 

## Installation & Setup
### Backend
The backend runs in Docker and uses Poetry to manage dependencies. 

Install the following systems before starting
 - Poetry:  follow the instructions [here](https://python-poetry.org/docs/#system-requirements)
 - [Docker](https://docs.docker.com/desktop/?_gl=1*bnza71*_ga*MTkwODkzNDI0Mi4xNzA0NTUwMTg2*_ga_XJWPQMJYHQ*MTcwNTg1MTY1OS42LjEuMTcwNTg1MTY2Mi41Ny4wLjA.) if you don't already have it

Now to start the system:
- `poetry install` -- install dependencies locally
- `docker compose build` -- Build the docker image for the web server
- `docker compose up` -- Start the web server

And for development:
- `pre-commit install` -- Install the pre-commit hooks
- `poetry shell` -- Start the poetry shell

### Frontend
The frontend uses TailwindCSS, which watches for changes in Django templates and automatically recompiles the CSS.

To start the CSS watcher:
- `make watch-css`

### Other commands
- See the `Makefile` for other commands, such as `make test` to run the tests.