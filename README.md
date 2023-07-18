# On the generation of Metric TSP instances with a large integrality gap by branch-and-cut

In our paper "[On the generation of Metric TSP instances with a large integrality gap by branch-and-cut](https://link.springer.com/article/10.1007/s12532-023-00235-7)  we introduce the `HardTSPLIB`, a family of 41 metric TSP instances hard to solve for `concorde` [1]

In this README, we provide a brief description of how to test the complexity of our code.
Such instances are divided as follows:

#### Instances derived from TSPLIB [2]
These are 14 instances from the TSPLIB, with less than 100 vertices, which are used to produce the results in Tables 1, 2, and 3:
```
att48, bayg29, bays29, berlin52, brazil58, dantzig42, eil51,
eil76, gr24, gr48, hk48, pr76, st70, swiss42
```

#### Instances derived from sampling
These are 21 instances used for the results presented in Table 5:
```
10007, 10008, 10010, 15002, 15005, 15007,
20007, 20009, 25001, 25004, 25006,
30001, 30003, 30005, 35002, 35003, 35009
40003, 40004, 40008
```

#### Instances derived from sampling until we are competitive with [3]
These are 7 instances used to produce the results in Figure 2:

```
10001, 11675, 12290, 14850, 16038, 20181, 33001
```


### Structure of the directory HardTSPLIB

The folder HardTSPLIB has the following structure:

```
├──instances
├──solve.py
├──README.md
```

The script `solve.py` allows you to test our instances using `concorde`.

The help returns:
```
usage: solve.py [-h] [-concorde_path CONCORDE_PATH] [-instance INSTANCE] [-seed SEED]

options:
  -h, --help            show this help message and exit
  -concorde_path CONCORDE_PATH
                        Specify the path of the concorde executable
  -instance INSTANCE    TSP instance in TSPLIB format
  -seed SEED            Seed
```

To do so, run something like
```
python solve.py -concorde_path your/concorde/path -instance ./instances/10001_hard.tsp
```

Where `your/concorde/path` stands for the directory where you have the executable of `concorde`.
This script creates a folder `run`, where it saves all the intermediate files of `concorde`, and a folder `sol`
where it saves the optimal tour.

[1] [Applegate, D., Bixby, R., Cook, W., & Chvátal, V. (1998). On the solution of traveling salesman problems.](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=c69d85c8a62d7ec79a4c77cef0824828d99aedbe)

[2] [Reinelt, G. (1991). TSPLIB—A traveling salesman problem library. ORSA journal on computing, 3(4), 376-384.](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.3.4.376)

[3] [Zhong, X. (2021). Lower Bounds on the Integraliy Ratio of the Subtour LP for the Traveling Salesman Problem. arXiv preprint arXiv:2102.04765.](https://arxiv.org/abs/2102.04765)
