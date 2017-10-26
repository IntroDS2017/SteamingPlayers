# Traffic accidents in Helsinki

Source code for (DATA11001) Introduction to Data Science-mini project.

Logs in the `./logs` directory and `process_log.txt` describe the changes in the data sets, and what methods are used to produce new output.

Output is intended to be saved to `./data`-directory.

To run all the intended data transformations, run either `process_data_pipenv.sh` or `process_data.sh` bash-script.

## Website

[Helsinki Traffic Research](https://helsinki-traffic-research.herokuapp.com)

## Data-source

- Traffic amounts in Helsinki: [Liikennemäärät Helsingissä](https://www.avoindata.fi/data/fi/dataset/liikennemaarat-helsingissa)

- Finnish traffic accidents: [Tieliikenneonnettomuudet](https://www.avoindata.fi/data/fi/dataset/tieliikenneonnettomuudet)

## Pipenv instructions

Also found [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
Some of the packages I was not able to install via pipenv, and should be installed individually with pip.

1. Have Pip for python 3 installed
    - Google if uncertaion how to do it in your OS
2. Install Pipenv with command: `pip install --user pipenv`
3. Run command: `pipenv install`
    - Now you have environment set up


To run a python file, run it with command `pipenv run python <name of the file>.py`


To install a new dependency, run command: `pipenv install <module name>`


To run shell with pipenv's dependencies, you can run `pipenv shell`
