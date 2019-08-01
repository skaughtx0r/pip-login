# pip-login
Command line interface for logging into a private python repository
by configuring pip.conf and storing credentials with python keyring.

This utilizes the new python keyring feature in pip 19.2.1

# Usage

To install:

```
pip install pip-login
```

Then just run the following:

```
pip-login
```

By default pip login will prompt for `url`, `username` and `password`.
The url is what you'd normally pass as an `--extra-index-url`.
The username and password will be stored using python keyring and the
url will be added to your pip.conf or pip.ini. If run in a virtualenv
it will store the pip.conf in the virtualenv, otherwise it stores it
to the per-user location. See the
[pip config user guide](https://pip.pypa.io/en/stable/user_guide/#config-file)
for more information.

Additionally, although not recommended, you can set all of the parameters
via command line arguments (See --help) or by setting the following
environment variables.

```
PIP_LOGIN_REPOSITORY
PIP_LOGIN_USERNAME
PIP_LOGIN_PASSWORD
```
