# git-credential-pass
A git credential helper to integrate with pass

# Requirements
* python 2
* pass

# Installation
Copy git-credential-pass.py into a location into a directory included in $PATH e.g. /usr/local/bin

# Usage
You can set git's credential helper on a per repo basis repository using:
```shell
git config credential.helper git-credential-pass.py
```
Or globally using:
```shell
git config --global credential.helper git-credential-pass.py
```

# Notes:
* Only the get operation is supported
* It will return the first set of credentials found
* Minimal testing has been performed
