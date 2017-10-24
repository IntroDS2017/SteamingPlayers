# Website:
- https://helsinki-traffic-research.herokuapp.com


# Comparing amounts and accidents in traffic in Helsinki

## B

We intend to analyse open data on traffic of Helsinki. We use two datasets of which one contains information about annual traffic on different streets of Helsinki, and the other one data about traffic accidents all over Finland. We would like to identify patterns on which time of the day traffic accidents occur on different streets, and find out, if changes occur in amounts of accidents annually.

### C

The dataset that has information about annual traffic of different streets of Helsinki at different times of day is a CSV-file containing around 28000 rows. The other dataset about Finland's traffic accidents comprises of annual CSV-files of around a million rows a piece. Our plan is to combine the data from these two datasets based on location data like coordinates and street names.

### D

The work will be centered around statistics.

### E

We will communicate our results with a report containing graphical presentations of the processed data.

### F

The purpose of our project is to examine, which streets are more prone to accidents than others.


## Source

- Traffic amounts in Helsinki: [Liikennemäärät Helsingissä](https://www.avoindata.fi/data/fi/dataset/liikennemaarat-helsingissa)

- Finnish traffic accidents: [Tieliikenneonnettomuudet](https://www.avoindata.fi/data/fi/dataset/tieliikenneonnettomuudet)

## Pipenv instructions 

Also found [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

1. Have Pip for python 3 installed
    - Google if uncertaion how to do it in your OS
2. Install Pipenv with command: `pip install --user pipenv`
3. Run command: `pipenv install`
    - Now you have environment set up


To run a python file, run it with command `pipenv run python <name of the file>.py`


To install a new dependency, run command: `pipenv install <module name>`


To run shell with pipenv's dependencies, you can run `pipenv shell`
