# Python Tech Challenge

The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000.

## Requirements

The `DataCapture` object accepts numbers and returns an object for the querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.

Here's the program skeleton in python to explain the structure:

```
datacapture = DataCapture()
datacapture.add(3)
datacapture.add(9)
datacapture.add(3)
datacapture.add(4)
datacapture.add(6)
stats = datacapture.build_stats()
stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and  9 are the only two values greater than 4)
```

## Challenge Conditions
 
* You cannot import a library that solves it instantly.
* The methods `add()`, `less()`, `greater()`, and `between()` should have a constant time O(1)
* The method `build_stats()` can be at most linear O(n)
* Apply the best practices you know
* Share a public repo with your project

## Solution

I've proposed a solution that involves the following

### DataCapture

A class that allows you to add numbers to the list and compute the statistics through the `build_stats` method.

#### add

Add a number to the list of numbers to evaluate

#### build_stats

Iterates over the internal `_counts` property, . At the same time, it creates an object for each number in it.
the internal dictionary contains the following keys:

- `less`: Since the internal dict is supposed to be in order, we add to less the current number’s counter `less += self._counts[number]`
- `greater`: Since the internal dict is supposed to be in order, we subtract to greater the current number’s counter `greater -= self._counts[number]`
- `count`: We make it equals to the current number’s count inside the internal counter self._counts (dict) `stats._counts[number]['count'] = self._counts[number]`

### Stats

A class that makes the computations

This class contains the following methods:

#### less

Returns the number of items in the list that are less than the number passed in.

#### greater

Returns the number of items in the list that are greater than the number passed in.

#### between

Returns the number of items in the list that are between the lower and upper bounds passed in.

## Setup

> This project uses Python 3.10, other python versions may work, but it is not guaranteed.

- Clone the repo.
- cd to the folder.
- Create a virtual environment.
- Activate it.

## Usage

If you want to see the driver_code running run the command: `python driver_code.py`
Also you can start your own shell with the `.env` file, import the `DataCapture` class and execute your own code.

## Testing

Run the command: `PYTHONPATH=./src python tests/test_data_capture.py`
