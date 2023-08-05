"""Paquete que contiene los algoritmos con las metaheristicas de simulated annealing y algoritmo genetico"""

import csv
import math
from datetime import datetime
from pathlib import Path
import statistics as stats
from timeit import default_timer as timer

from TSPF.Algorithms.Population import Population
from TSPF.Algorithms.GeneticAlgorithm import GeneticAlgorithm
from TSPF.Algorithms.SimulatedAnnealing import SimulatedAnnealing