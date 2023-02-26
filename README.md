# IF2211 Algorithm Strategies Course Project
## Closest Pair of Points in $R^n$ Euclidean Space with Divide and Conquer

This repository contains a program written in Python to find the closest pair of points in $R^n$ Euclidean space using divide and conquer technique. This program is a part of [Bandung Institute of Technology](https://www.itb.ac.id/) IF2211 Algorithm Strategies course project.

## Getting Started
To use this program, you need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

A few external dependencies also needs to be installed. Below listed are the libraries used in this project:
- Matplotlib
- Tkinter
- Numpy
- Math
- Time

## Setup
1. Clone the repository to your local machine
    ``` bash
        $ git clone https://github.com/AlifioDitya/Tucil2_13521142_13521124.git 
    ```
2. Change directory to the `src` folder
    ``` bash
        $ cd src
    ```
3. Run `main.py`
    ``` bash
        $ python3 main.py
    ```

## Usage
To use the program, you need to run the `main.py` file located in the `src` folder. The program will prompt you to enter the number of points you want to generate randomly and the $n$ dimension of the points. After receiving the input, the program will generate random points in $R^n$ Euclidean space and find the closest pair of points using the divide and conquer technique. The program will then display the two closest points and their distance.

## Algorithm
The algorithm used in this program is the divide and conquer algorithm for finding the closest pair of points in $R^n$ Euclidean space. The algorithm works as follows:

1. Sort the points according to their x-coordinates.
2. Divide the set of points into two halves.
3. Recursively find the closest pair of points in each half.
4. Find the closest pair of points that have one point in each half. This can be done in O(n) time by checking the points that are within a distance of delta from the dividing line, where delta is the minimum distance found in the recursive calls.
5. Return the closest pair of points.

The time complexity of the algorithm is $O(n \log(n))^{d-1}$ where $n$ is the number of points and $d$ is the dimension.

## Repository Structure
```
│ .gitignore
│ README.md
│ LICENSE
│
├─── doc
│       │ Tucil2_K2_13521142_13521124.pdf
│
├─── src
│       │ main.py
│       │ 
│       ├─── module
│                  │ bruteforce.py
│                  │ divideconquer.py
│                  │ Point.py
│
├─── test
        │ test1.jpg
        │ test2.jpg
        │ test3.jpg
        │ test4.jpg
        │ test5.jpg
        │ test6.jpg
        │ test7.jpg
        │ test8.jpg
        │ test9.jpg
```

## Author
- [Enrique Alifio Ditya - 13521142](https://github.com/AlifioDitya) 
- [Michael Jonathan Halim - 13521124](https://github.com/maikeljh) 

## Made with
[![Python 3.10](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)