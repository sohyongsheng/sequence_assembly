# Sequence Assembly

![CI/CD pipeline](https://github.com/sohyongsheng/sequence_assembly/workflows/CI/CD%20pipeline/badge.svg)

This is a [sequence assembler](https://en.wikipedia.org/wiki/Sequence_assembly) written in Python 3. The motivation of this project is to show my fiancee Yan Ting some best practices and my coding style, so that she can choose to use these practices depending on the scenario.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3.6 and above.

### Installing

It's recommended that you use a virtual environment to install Python packages. One way to do this is

```
# Create a virtual environment in a directory called env.
python3 -m venv env

# Activate virtual environment.
source env/bin/activate

# Upgrade basic essentials.
pip3 install -U pip setuptools wheel
```

Then install package requirements by running

```
pip3 install -r requirements.txt
```


## Running the tests

We use [pytest](https://docs.pytest.org/en/stable/), and the tests are stored in the `tests` directory. You can run the tests by running

```
pytest tests
```

## Deployment

Add additional notes about how to deploy this on a live system

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags](https://github.com/sohyongsheng/sequence_assembly/tags) on this repository. 

## Authors

- [Soh Yong Sheng](https://github.com/sohyongsheng)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [PurpleBooth](https://github.com/PurpleBooth) for providing the [template](https://github.com/PurpleBooth/a-good-readme-template) to this README.

