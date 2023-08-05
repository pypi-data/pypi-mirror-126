# QR Code for NetDrones

Sample package that reads in QR code data, writes them into files for printing.
It also reads in a set of image files and looks for QR Codes.

## Python PIP Packaging Notes

The package layout has the source code in [src/netpy](src/netpy) and note the
critical files there are:

- py.typed. Must be an attribute in [setup.py](setup.py) which configures the
    python package.
- __init__.py. This must be there to denote the package and import all
    the modules.
- setup.py. The file that drives the packaging, it tells the build system where
    to find the components when you do a `python -m build`
- pip install -e. This is used for development and does an "editable"
    installation
