![alt text](https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/2952/2018/01/31185708/CNX_UPhysics_04_03_Soccer.jpg)

# 3D-Projectile

## Table of contents
* [General info](#general-info)
* [Libraries](#libraries)
* [Working](#working)
* [Installation](#installation)

## General info
A Python Project to visualize the motion of a body as a projectile in 3D Space with in an ideal environment with no air resistance. This project is small script that takes in the following parameters into consideration before doing the necessary computation :

Input Parameters | Meaning
------------ | -------------
Initial Velcoity, `u`| Decides the speed at which the projectile is shot
Polar Angle, `θ` | Throwing Angle with respect to `x-axis`
Polar Angle, `φ` | Throwing Angle with respect to `z-axis`

> The parameters specififed above are according to the Spherical Coordinate System

## Libraries
Project is created in `Python 3.8.7` with the following libraries:
* `Matplotlib                3.3.1`
* `Numpy                     1.18.5`
* `Mplcursors                0.3`
	
	
## Working 
### Libraries and their uses 
This project uses the aforementioned libraries for :
* `Matplotlib-3.3.1` is used for plotting the coordinates of the projectile in the 3d Space.
* `Numpy-1.18.5` is used for doing several computations required in the equations such as angle conversions (radian-to-degree & vice-versa) , initializing empty arrays of float type etc. 
* `Mplcursors-0.3` is used to connect the data-points to the annotations in the matplotlib plot which can be accessed on clicking any point over the line.

### Program Cycle 
The script starts with the driver code that initailises an instance of the `Projectile` class and then executes the `Projectile.mainplot()` method.


## Installation
To install the libraries required to run the project :

```git
$ pip install matplotlib
$ pip install numpy
$ pip install mplcursors
$ git clone https://github.com/Suryansh-23/3D-Projectile/
$ python "3D Projectile.py"
```

![alt text](https://matplotlib.org/_static/logo2_compressed.svg)  ![alt text](https://1000logos.net/wp-content/uploads/2020/08/Python-Logo.png)

![alt text](https://www.freecodecamp.org/news/content/images/2020/07/numpy.png)
