# pyvjoy

pyvjoy is a set of python binding for <a href='vjoystick.sourceforge.net'>vJoy</a>. This repository is based off <a href="https://github.com/tidzo/pyvjoy">tidzo</a>'s package.


### Requirements

Install vJoy from http://vjoystick.sourceforge.net/site/. It is recommended to also install the vJoy Monitor and Configure vJoy programs. These should be an option during installation.


### Installation

Simple! This package is installable by pip

`pip install pyvjoy`

After vJoy and pyvjoy have been installed, you may need to copy the vJoyInterface.dll file from your installation location to the location of the python package.


### Usage

With this library you can easily set Axis and Button values on any vJoy device. Low-level bindings are provided in `pyvjoy._sdk`.

See examples for simple use cases.
