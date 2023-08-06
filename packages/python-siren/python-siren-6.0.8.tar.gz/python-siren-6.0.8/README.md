# Siren --- Interactive Redescription Mining

Siren is a graphical user interface for interactive mining and visualization of redescriptions.


### Installation

#### Dependencies
`python-siren` requires several other Python utilities, including wxPython Phoenix (for the GUI), Numpy, Scipy, Scikit-learn, Matplotlib, and Cartopy.

* python-dateutil (>= 2.7.3)
* shapely (>= 1.7.0)
* numpy (>= 1.13.0)
* scipy (>= 0.19.0)
* scikit-learn (>= 0.19.0)
* wxPython (>= 4.0.0)
* matplotlib (>= 2.1.0)
* cartopy (>= 0.14)

#### PIP
with pip, installation should be as easy as running 
`pip install python-siren`

this should provide the following commands:

* `exec_siren` to launch the interface for interactively mining and visualizing redescriptions
* `exec_clired` to run the command-line redescription mining algorithms
* `exec_server` to launch the server for off-loading computations
* `exec_client` to run the command-line client allowing to send computations to server

### More information
See http://cs.uef.fi/siren/

### License
Siren is licensed under Apache License v2.0. See attached file "LICENSE".

(c) Esther Galbrun and Pauli Miettinen, 2012
