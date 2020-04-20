# git-credential-pass
A git credential helper to integrate with pass

# Requirements
* Python 2.7/3.7+
* pass

# Installation
Copy git-credential-pass.py into a location into a directory included in $PATH e.g. /usr/local/bin

# Usage
You can set git's credential helper on a per repo basis repository using:
```shell
git config credential.helper /usr/local/bin/git-credential-pass.py
```
Or globally using:
```shell
git config --global credential.helper /usr/local/bin/git-credential-pass.py
```

# Notes:
* Only the get operation is supported
* It will return the first set of credentials found
* Minimal testing has been performed
