# aproc - for asynchronous multiprocessing
`aproc` extends the multiprocessing library by combining a multiprocessing pool with a multiprocessing queue.

[![Python package](https://github.com/pyiron/aproc/workflows/Python%20package/badge.svg)](https://github.com/pyiron/aproc/actions)
[![Coverage Status](https://coveralls.io/repos/github/pyiron/aproc/badge.svg?branch=master)](https://coveralls.io/github/pyiron/aproc?branch=master)

# Installation
aproc can either be installed via pip using:

    pip install aproc

Or via anaconda from the conda-forge channel

    conda install -c conda-forge aproc

# Usage 

    from aproc import Pool
    
    # Define function to be executed in subprocess 
    def print_function(args):
        print(args)
    
    # Dynamically extend the list of objects to be processed by placing them in the pool
    with Pool(processes=2, initializer=print_function) as pool:
        pool.put(1)
        pool.put("two")
        pool.put({"three": 3})
        pool.put([4])

In addition `aproc` also supports bidirectional communication: 

    from aproc import Pool
    
    # Define function to be executed in subprocess, which returns a response
    def both_way(args):
        return args
    
    # Dynamically extend the list of objects to be processed by placing them in the pool
    with Pool(processes=2, initializer=print_function, bidirectional=True) as pool:
        pool.put(1)
        print(pool.get())
        pool.put("two")
        pool.put({"three": 3})
        pool.put([4])
        print(pool.get())
        print(pool.get())
        print(pool.get())

# License
aproc is released under the BSD license https://github.com/pyiron/aproc/blob/master/LICENSE . It is a spin-off of the pyiron project https://github.com/pyiron/pyiron therefore if you use aproc for your publication, please cite: 

    @article{pyiron-paper,
      title = {pyiron: An integrated development environment for computational materials science},
      journal = {Computational Materials Science},
      volume = {163},
      pages = {24 - 36},
      year = {2019},
      issn = {0927-0256},
      doi = {https://doi.org/10.1016/j.commatsci.2018.07.043},
      url = {http://www.sciencedirect.com/science/article/pii/S0927025618304786},
      author = {Jan Janssen and Sudarsan Surendralal and Yury Lysogorskiy and Mira Todorova and Tilmann Hickel and Ralf Drautz and Jörg Neugebauer},
      keywords = {Modelling workflow, Integrated development environment, Complex simulation protocols},
    }
