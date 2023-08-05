# Pip Venv Sure

Prevents the installation of packages into you base installation of python

## usage and setup

```commandline
pip3 install pip-venv-sure
alias pip3=pip-venv-sure
```

## motivation

I don't like installing packages directly into my base installation. But as a mere human being I sometimes forget to activate my venv, so this prevent these kinds to accidents from happening.

### installing packages to base installation.

Some times there is a need to install package directly to the base installation of python in that case you can use the following command.

```commandline
pip3 install any-template --allow-no-venv
```
