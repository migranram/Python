# Genetic Algorithm for the Salesman problem

## Route
The salesman has to travel between these cities:
- London
- Dunedin
- Beijing
- Tokyo
- Venice
- Singapore
- Phoenix
- Albacete 

It is necessary to get the distances between them. That info is obtaine using the webpage:
- https://www.distancecalculator.net/

| \         | London   | Dunedin  | Beijing  | Tokyo    | Venice   | Singapore | Phoenix  | Albacete |
|-----------|----------|----------|----------|----------|----------|-----------|----------|----------|
| London    | 0        | 19086.73 | 8138.09  | 9561.70  | 1137.47  | 10855.47  | 8481.56  | 1396.72  |
| Dunedin   | 19086.73 | 0        | 10952.79 | 9578.98  | 18322.68 | 8334.00   | 11743.67 | 19027.48 |
| Beijing   | 8138.09  | 10952.79 | 0        | 2099.47  | 7887.33  | 4479.94   | 10457.19 | 9229.15  |
| Tokyo     | 9561.70  | 9578.98  | 2099.47  | 0        | 9565.36  | 5322.22   | 9304.58  | 10823.08 |
| Venice    | 1137.47  | 18322.68 | 7887.33  | 9565.36  | 0        | 10023.28  | 9613.57  | 1367.99  |
| Singapore | 10855.47 | 8334.00  | 4479.94  | 5322.22  | 10023.28 | 0         | 14626.38 | 11265.83 |
| Phoenix   | 8481.56  | 11743.67 | 10457.19 | 9304.58  | 9613.57  | 14626.38  | 0        | 9223.15  |
| Albacete  | 1396.72  | 19027.48 | 9229.15  | 10823.08 | 1367.99  | 11265.83  | 9223.15  | 0        |


## Algorithm
The genes contain the city order to follow by the salesman. The total distance to cover in this order is the performance measure of the genome sequence. The data structure `Genes` contains all the necessary information and functions to encode the genomes.
- **Crossover**: In this case the crossover of genes doesn't result in a better perfomance, since swapping two cities may have a great impact in the cost of the travel. Therefore the best genes are kept untouched.
<br><br>
- **Mutation**: The rest of the genes mutate with a probability of 80% (can be changed). This mutation consists of a swap between two cities in their genome sequence.

## How to use
Just run `geneticAlgorithm.py`. Some libraries are necessary:
- Numpy
- Pandas

You can install them by running:
```
pip install -r requirements.txt
```

## Results
The best city order found by the algorithm is:
```
Best oder:  ['Phoenix', 'London', 'Albacete', 'Venice', 'Beijing', 'Tokyo', 'Singapore', 'Dunedin']  - With cost:  34889.29
```