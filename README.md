# learn_sort_speed.py

Simple python script to compare search speeds for Sets, Lists and binary search

## Installation

### 1. Download the script and names file

* Go to [https://github.com/mjbundschuh/learn_sort_speed] 
* Select the script
* Select the download button

<img src="images/learn_imap_yahoo1.png" alt="Download Speed Script" height="200"/>

* Select a destination. 

<img src="images/learn_imap_yahoo2.png" alt="Select Download Location" height="200"/>

*Repeat for the names.txt file*

_In this example, I chose my $HOME/Applications folder to store the script. This folder is in my $PATH_

### 2. Run the script

Go to your Applications folder and run python on the script

```bash
% cd ~/Applications
% python learn_sort_speed.py

Set search speed: average 5000x
	good list: 0.0004
	 bad list: 0.0004

List search speed: average 5000x
	good list: 0.2446
	 bad list: 0.5182

Binary search speed: average 5000x
	good list: 0.0109
	 bad list: 0.0114

```

## Learning Notes
* Sets are extremely fast and was 33x faster than binary search
* Lists are slower by 2 orders of magnitude

## Testing and Assumptions

* This program was tested on a Macbook Air using iTerm2 (a better alternative to the terminal)
* You should be using Python3 and it should be in your PATH when you run this program
* You know how to use a terminal and command-line commands
* names.txt database started with data from Data World, then supplemented with additional first names (mostly non-European). It has 7000+ first names.

```bash
% cd ~/Applications
% head -n 15 names.txt
Aaden
Aaliyah
Aarav
Aaron
Aarthi
Aarthy
Ab
Abagail
Abb
Abbey
Abbie
Abbigail
Abbott
Abby
Abdiel
% cat names.txt | wc -l
    7069
```

## Supporting Documentation

* [Python Sets](https://realpython.com/python-sets/)
* [Python Lists](https://realpython.com/python-list/#appending-a-single-item-at-once-append)
* [Data World - Names][https://data.world/alexandra/baby-names]

## License

[MIT](https://choosealicense.com/licenses/mit/)
