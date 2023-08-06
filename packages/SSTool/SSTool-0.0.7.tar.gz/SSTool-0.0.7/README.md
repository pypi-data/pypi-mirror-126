# State Space Tool 
This open source tool builds and analyzes the state space representation of power systems. The goal is to offer a flexible and robust package written in Python that can manage realistic grids. It focuses on stability studies. 

Developed by CITCEA-UPC and distributed under the MIT License.

## Installation
Install the software by using the code provided in this repository. There are several options:

   1. Clone the [State Space Tool repository from GitHub][1]:
   
   *Use this option if you are familiar with Git*
   
    - From the command line:
        - `git clone https://github.com/JosepFanals/Hyosung`
    - Or from the [State Space Tool repository page][1]:
        - Click the green **Clone or download** button, then **Open in Desktop**.

   2. Download the repository as a .zip file from the GitHub page.
    - Go to the [State Space Tool GitHub repository page][1].
    - Click the green **Clone or download** button, then **Download ZIP**.

   3. Install with pip (may not be updated to the latest version):
      - `pip install SSTool`


## Supported elements
It allows the modelling of the following components:

- Resistances
- Inductances
- Capacitors
- Ideal grids
- Voltage source converters (VSC)
- Synchronous generators (SG)

## Analysis
Stability tools have been included to verify the dynamic performance of the system:

- Nyquist
- Bode
- Eigenvalues
- Poles and zeros

## Images

![](https://github.com/JosepFanals/Hyosung/blob/main/pics/nyquist_2vsc.png)

![](https://github.com/JosepFanals/Hyosung/blob/main/pics/eigens1.png)

[1]: https://github.com/JosepFanals/Hyosung


