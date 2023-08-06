Creation date: 20.10.2020, 12:50  
Last modification: 10.03.2021, 12:52  
Authors: Lukas Bromig, Nikolas von den Eichen, Valeryia Sidarava, Jose Jesus de Pina Torres 

# sila2lib_implementations

This repository contains SiLA2 drivers for a variety of device that are being used at the [Chair of Biochemical Engineering](https://www.mw.tum.de/en/biovt/home/) at TUM. The repository is setup in a way that it can be installed as python package. Client files can be imported. 

The following devices are supported:
- **BlueVary Offgas-analytics**
- **DASGIP 4xParallel Reactor System**
- **LAUDA LOOP 250**
- **LAUDA LOOP 500**
- **Presens sensor bars**
- **Reglo ICC peristaltic pump**
- **Flowmeter Bronkhorst**

SiLA version of drivers may vary. In case of incompatibilities, please reach out to:   
*lukas.bromig@tum.de* 

## Installation

After cloning the repository, run the update_package.bat to create the installation files (distribution).  
The distribution process will create the respective tar.gz and wheel file in the dist folder.   
``````

Installation of the package files:  
Using pip:
```pip install sila2lib_implementations/dist/sila2lib_implementations-Lukas-Bromig-0.0.1.tar.gz``` 

Using pipenv:
pipenv install sila2lib_implementations/dist/sila2lib_implementations-Lukas-Bromig-0.0.1.tar.gz

Requires sila2lib, sila2comlib and [optional] sila2codegenerator for unit tests. 
Further requirements include:
- InfluxDB, csv, numpy, persistent, opcua, pyserial, cryptography  
These packages can be installed via the pypi index using pip/pipenv install <package_name>.
Make sure that protobuf is installed with the PIP_NO_BINARY option. This is more complicated when using pipenv. An
environmental variable for PIP_NO_BINARY has to be used. [Refer to documentation](link).
