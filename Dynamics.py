import numpy as np
import matplotlib.pyplot as plt

# Dynamics() takes a list of input functions and a list of initial states and evaluates the dynamics of the system

class Dynamics():
    def __init__(self,
                 functions, # as a list e.g. [f,g,h]
                 initial_conditions # as a list e.g. [1,.5,.6]
                 ):

        try:
            assert len(functions) == len(initial_conditions)
        except:
            raise ValueError()

        self.functions = functions
        self.X = [[value] for value in initial_conditions]
    
    # evaluates each function inputting the previous value until convergence or divergence
    
    def recurse(self,
                divergent_length=100,
                accuracy = 0.1
               ):
        
        while True:

            deltas = [[0] for i in range(len(self.X))]

            for i,function in enumerate(self.functions):
                
                args = [path[-1] for path in self.X]
                val = function(*args)
                delta = abs(val - self.X[i][-1])

                self.X[i].append(val)
                deltas[i].append(delta)
            
            convergence = []
            divergence = []
            oscillating = []

            for i, path in enumerate(self.X):

                if abs(path[-1] - path[-2]) <= accuracy:
                    convergence.append(round(path[-1],4))

                if deltas[i][-1] >= deltas[i][-2]:
                    if len(self.X[0]) > divergent_length:
                        divergence.append(deltas[-1])
                        
                if abs(path[-1]) == abs(path[-2]):
                    oscillating.append(round(path[-1],4))
                    
            if len(convergence) == len(self.X):
                break
                
            if len(oscillating) == len(self.X):
                break
                
            if len(divergence) == len(self.X):
                break
                
    # univariate_plot() for a single input function 

    def univariate_plot(self,
                       figsize = (20,20)
                       ):
        
        dynamic_path = self.X[0]

        fig, axes = plt.subplots(2,1,figsize=figsize)

        start = min(dynamic_path)
        end = max(dynamic_path)

        ax = axes[0]
        ax.set_title('Phase Portrait');

        ax.plot([i for i in np.arange(start,end+.1, .1)], 
                [self.functions[0](i) for i in np.arange(start,end+.1, .1)], 
                color = 'b'
               );

        ax.plot([i for i in np.arange(start,end+.1, .1)], 
                [i for i in np.arange(start,end+.1, .1)], 
                color = 'black'
               );

        ax.vlines(x = dynamic_path[0], 
                  ymin = start, 
                  ymax = self.functions[0](dynamic_path[0]), 
                  color = 'orange'
                 );

        for i, init in enumerate(dynamic_path):

            ax.vlines(x = init, 
                      ymin = init, 
                      ymax = self.functions[0](init), 
                      color = 'orange'
                     )

            try:
                ax.hlines(y = self.functions[0](init), 
                          xmin = dynamic_path[i], 
                          xmax = dynamic_path[i+1], 
                          color = 'orange'
                         );
            except:
                pass

        ax = axes[1]
        ax.set_title('Dynamic Path');
        ax.plot(dynamic_path, color = 'orange');

    # bivariate_plot() for two input functions

    def bivariate_plot(self,
                      figsize = (20,20)
                      ):
        
        x_path = self.X[0]
        y_path = self.X[1]

        fig, axes = plt.subplots(2,1, figsize = figsize)

        ax = axes[0]

        ax.plot(x_path, y_path, color = 'orange');

        ax.vlines(x=0,
                  ymin = min(y_path), 
                  ymax = max(y_path)
                 );

        ax.hlines(y=0, 
                  xmin = min(x_path), 
                  xmax = max(x_path)
                 );

        ax.set_title('Phase Portrait');

        ax = axes[1]

        ax.plot(x_path, 
                color = 'b'
               );

        ax.plot(y_path, 
                color = 'orange'
               );

        ax.set_title('Dynamic Path');

    # trivariate_plot() for three input functions
    
    def trivariate_plot(self, 
                       figsize = (20,20)
                       ):
       
        x_path = self.X[0]
        y_path = self.X[1]
        z_path = self.X[2]

        fig = plt.figure(figsize=figsize)
        
        ax = plt.axes(projection='3d');
        ax.set_title('Phase Portrait');
        ax.plot3D(x_path, y_path, z_path, 'b');

        fig = plt.figure(figsize=(15, 7)) 
        ax = plt.axes()
        
        ax.plot(x_path, color = 'b');
        ax.plot(y_path, color = 'orange');
        ax.plot(z_path, color = 'r');
        ax.set_title('Dynamic Path');
