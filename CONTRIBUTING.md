# Contribution Guide

## Guides

### Configure TestPyPi

1. Configure TestPyPi: `poetry config repositories.test-pypi https://test.pypi.org/legacy/`
2. Grab your token from TestPyPi.
3. Configure the TestPyPi token: `poetry config pypi-token.test-pypi <token>`

### Test a new package version through TestPyPi

1. If TestPyPi is not configured, follow the corresponding guide.
2. Update the version in `pyproject.toml`.
3. Build the new version: `poetry build`
4. Publish: `poetry publish -r test-pypi -u <username>`
5. Install the package through TestPyPi: `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ semgrep-rules-manager`
6. Execute your tests by leveraging the `semgrep-rules-manager` command.

### Configure PyPi

1. Grab your token from PyPi.
2. Configure the TestPyPi token: `poetry config pypi-token.pypi  <token>`

### Publish a new package version in PyPi

1. If PyPi is not configured, follow the corresponding guide.
2. Update the version in `pyproject.toml`.
3. Build the new version: `poetry build`
4. Publish: `poetry publish -u <username>`
5. Install the package: `pip install semgrep-rules-manager`
