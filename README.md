# cartesian product

## General Info

Evaluation project for Vee interview.

The goal of the task is to create a formula of cartesian product for nested words lists. Data is given as a list of dictionaries, where first key is a name, and second key is a words list. Example data: [{'name': '#x', 'words': ['x', 'xx']}, {'name': '#y', 'words': ['y', 'yy', '#x #y']}]

## Installation

* Code was written in Python 3.10.

* Clone the repository with: git clone https://github.com/mkuleczka/cartesian.git

* Navigate to the project directory.


## Usage

* To start program use command in terminal: python3 vee_monika.py

* Then write input as a list in terminal.

Example:

Input: [{'name': '#not', 'words': ['not']}, {'name': '#interested', 'words': ['interested']}, {'name': '#not_interested', 'words': ['#not #interested', 'i\\'am #not_interested']}]

Expected output: [{'name': '#not', 'words': ['not']}, {'name': '#interested', 'words': ['interested']}, {'name': '#not_interested', 'words': ['not interested', "i'am not interested"]}]
