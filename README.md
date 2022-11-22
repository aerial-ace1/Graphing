# Graphing

## Pre-Requisites
#### Python is installed on the system and then run
```
pip install -r requirements.txt 
```

## Running
To run a custom test input in any file comment the line ```runner()``` and uncomment the line ```test()``` and give custom input in
```
if __name__ == "__main__":
    runner()
    # test()
``` 
and update the graph data in 
```
def test():
    list = 
    adj_mat = 
```

#### Utility Functions can be checked in ```utils.py```
# Prims and Kruskals
```
python3 part1.py
```
The given code implements both Prim's and Kruskal's algorithm and displays it's cost.
# Approximation of Minimum Hamiltonian Cycle
```
python3 part2.py
```
The given code implements approximation of min Hamiltonian Cycle algorithm and displays it's cost.

