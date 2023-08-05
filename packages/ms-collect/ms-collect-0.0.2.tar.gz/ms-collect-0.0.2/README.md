# ms-collect
A series of modules that provide easy storage/accesss to Mass Spec related Raw Data / Groupings of Data.

### Note this package is under active development.

## Installation
```sh
pip install ms-collect
```

### Local Development
As you make changes, In repository:
pip install .

Then in tests/ directory, you can run all the tests, test out development versions and so on

### Upcoming features
Automated testing using unittest


### Publishing a new version of ms-collect
Note, if you are not marked as a collaborator in the package registry, you will not be allowed to
publish a new version.

First ensure that you build:
```sh
python -m build
```

Then use twine to upload the archives under dist:
```sh
python -m twine upload dist/*
```

When prompted for credentials, enter your pypi creds or access token.
