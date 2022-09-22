import numpy as np
import matplotlib.pyplot as plt

#############################################################

def univariate_dynamics(f, 
                        init,
                        dynamic_path = [],
                        deltas = [],
                        delta_len = 10
                        ):
    
    # passing through our lists
    dynamic_path = dynamic_path
    deltas = deltas
    
    # evaluating our function and seeing the change
    val = f(init)   
    delta = abs(abs(val) - abs(init))
    
    # updating our lists
    dynamic_path.append(init)
    deltas.append(delta)
    
    
    # checking if we have converged - avoiding recursive depth
    if delta < 0.001:
        
        dynamic_path[-1] = round(val, 4)
        
        # returning our lists and convergence value
        return round(val, 4), dynamic_path
    
    
    if len(deltas) > delta_len:
    
        if deltas[-1] > deltas[-2]:
            print('divergent')
            return None, dynamic_path
        
    return univariate_dynamics(f, 
                               val, 
                               dynamic_path = dynamic_path, 
                               deltas = deltas, 
                              )

#############################################################

def univariate_plot(f, 
                    dynamic_path
                   ):

    fig, axes = plt.subplots(2,1,figsize=(20,20))

    start = min(dynamic_path) - min(dynamic_path)*.25
    end = max(dynamic_path) + max(dynamic_path)*.25
    
    ax = axes[0]
    
    ax.set_title('Phase Portrait');
    
    ax.plot([i for i in np.arange(start,end, .1)], 
            [f(i) for i in np.arange(start,end, .1)], 
            color = 'b'
           );

    ax.plot([i for i in np.arange(start,end, .1)], 
            [i for i in np.arange(start,end, .1)], 
            color = 'black'
           );

    ax.vlines(x = dynamic_path[0], 
              ymin = start, 
              ymax = f(dynamic_path[0]), 
              color = 'orange'
             );

    for i, init in enumerate(dynamic_path):

        ax.vlines(x = init, 
                  ymin = init, 
                  ymax = f(init), 
                  color = 'orange'
                 )

        try:
            ax.hlines(y = f(init), 
                      xmin = dynamic_path[i], 
                      xmax = dynamic_path[i+1], 
                      color = 'orange'
                     );
        except:
            pass
        
    ax = axes[1]
    
    ax.set_title('Dynamic Path');

    start = min(dynamic_path) - min(dynamic_path)*.25
    end = max(dynamic_path)*1.25

    ax.plot(dynamic_path, color = 'orange');

######################################################

def bivariate_dynamics(f,
                        g,
                        x_init,
                        y_init,
                        x_path = [],
                        y_path = [],
                        x_deltas = [],
                        y_deltas = [],
                        accuracy = 0.00001,
                       length = 10
                        ):
    
    # passing through our lists
    x_path = x_path
    y_path = y_path
    x_deltas = x_deltas
    y_deltas = y_deltas
    
    
    # evaluating our functions
    x_val = f(x_init, y_init)
    y_val = g(x_init, y_init)
    
    # finding the change
    x_delta = abs(abs(x_val) - abs(x_init))
    y_delta = abs(abs(y_val) - abs(y_init))
    
    # updating our lists
    x_path.append(x_init)
    y_path.append(y_init)
    
    x_deltas.append(x_delta)
    y_deltas.append(y_delta)
    
    # checking if we have converged
    
    if x_delta < accuracy:
        
        x_path[-1] = round(x_val, 4)
        
        if y_delta < accuracy:
        
            y_path[-1] = round(y_val, 4)
            
            return round(x_val, 4), round(y_val, 4), x_path, y_path
            
    if y_delta < accuracy:

        y_path[-1] = round(y_val, 4)
        
        if x_delta < accuracy:
        
            x_path[-1] = round(x_val, 4)
            
            return round(x_val, 4), round(y_val, 4), x_path, y_path
        
    # checking if we have diverged    
        
    if len(x_deltas) > 10:
        
        if x_deltas[-1] > x_deltas[-2]:
            print('x is divergent')

            if y_deltas[-1] > y_deltas[-2]:
                print('y is divergent')
                return None, None, x_path, y_path
            else:
                return None, round(y_val, 4), x_path, y_path

    if len(y_deltas) > length:
        
        if y_deltas[-1] > y_deltas[-2]:
            print('y is divergent')

            if x_deltas[-1] > x_deltas[-2]:
                print('x is divergent')
                return None, None, x_path, y_path
            else:
                return round(x_val,4), None, x_path, y_path

    return bivariate_dynamics(f, 
                              g, 
                              x_val,
                              y_val,
                              x_path = x_path,
                              y_path = y_path,
                                accuracy = 0.00001,
                               length = 10
                              
                               )

#############################################################



#############################################################

def bivariate_plot(x_path, y_path):
    
    fig, axes = plt.subplots(2,1, figsize = (20,20))

    ax = axes[0]

    ax.plot(x_path, y_path, color = 'orange');
    ax.vlines(x=0, ymin = min(y_path), ymax = max(y_path));
    ax.hlines(y=0, xmin = min(x_path), xmax = max(x_path));
    ax.set_title('Phase Portrait');

    ax = axes[1]

    ax.plot(x_path, color = 'b');
    ax.plot(y_path, color = 'orange');
    ax.set_title('Dynamic Path');

#############################################################

def trivariate_dynamics(f,
                       g,
                       h,
                       x_init,
                       y_init,
                       z_init,
                       x_path = [],
                       y_path = [],
                       z_path = [],
                       x_deltas = [],
                       y_deltas = [],
                       z_deltas = [],
                       accuracy = 0.00001,
                       length = 10
                        ):
    
    # passing through our lists
    x_path = x_path
    y_path = y_path
    z_path = z_path
    x_deltas = x_deltas
    y_deltas = y_deltas
    z_deltas = z_deltas
    
    # evaluating our functions
    x_val = f(x_init, y_init, z_init)
    y_val = g(x_init, y_init, z_init)
    z_val = h(x_init, y_init, z_init)
    
    # finding the change
    x_delta = abs(abs(x_val) - abs(x_init))
    y_delta = abs(abs(y_val) - abs(y_init))
    z_delta = abs(abs(z_val) - abs(z_init))
    
    # updating our lists
    x_path.append(x_init)
    y_path.append(y_init)
    z_path.append(z_init)
    
    x_deltas.append(x_delta)
    y_deltas.append(y_delta)
    z_deltas.append(z_delta)
    
    # checking if we have converged
    
    if x_delta < accuracy:
        
        x_path[-1] = round(x_val, 4)
        
        if y_delta < accuracy:
        
            y_path[-1] = round(y_val, 4)
            
            if z_delta < accuracy:
                
                z_path[-1] = round(z_val,4)
            
                return round(x_val, 4), round(y_val, 4),round(z_val, 4), x_path, y_path, z_path
            
    if y_delta < accuracy:

        y_path[-1] = round(y_val, 4)
        
        if x_delta < accuracy:
        
            x_path[-1] = round(x_val, 4)
            
            if z_delta < accuracy:
                
                z_path[-1] = round(z_val,4)
            
                return round(x_val, 4), round(y_val, 4),round(z_val, 4), x_path, y_path, z_path
            
    if z_delta < accuracy:

        z_path[-1] = round(z_val,4)
        
        if x_delta < accuracy:
        
            x_path[-1] = round(x_val, 4)

            if y_delta < accuracy:

                y_path[-1] = round(y_val, 4)
                
                return round(x_val, 4), round(y_val, 4),round(z_val, 4), x_path, y_path, z_path
        
    # checking if we have diverged
    
    if len(x_deltas) > 10:
        
        if x_deltas[-1] > x_deltas[-2]:
            print('x is divergent')

            if y_deltas[-1] > y_deltas[-2]:
                print('y is divergent')
            
                if z_deltas[-1] > z_deltas[-2]:
                    print('z is divergent')
                    return None, None, None, x_path, y_path, z_path
                
                else:
                    return None, None, round(z_val,4), x_path, y_path, z_path
                
            elif z_deltas[-1] > z_deltas[-2]:
                print('z is divergent')
                return None, round(y_val,4), None,  x_path, y_path, z_path
            
            else:
                return None, round(y_val,4), round(z_val, 4), x_path, y_path, z_path
            
        elif y_deltas[-1] > y_deltas[-2]:
            print('y is divergent')
            
            if z_deltas[-1] > z_deltas[-2]:
                print('z is divergent')
                return round(x_val, 4), None, None,  x_path, y_path, z_path
            else:
                return round(x_val, 4), None, round(z_val, 4),  x_path, y_path, z_path
        elif z_deltas[-1] > z_deltas[-2]:
            print('z is divergent')
            return round(x_val, 4), round(y_val, 4), None, x_path, y_path, z_path

    return trivariate_dynamics(f, 
                               g, 
                               h,
                               x_val,
                               y_val,
                               z_val,
                               x_path = x_path,
                               y_path = y_path,
                               z_path = z_path,
                               accuracy = 0.00001,
                               length = 10
                               )

#############################################################

def trivariate_plot(x_path, y_path, z_path):
    
    fig = plt.figure(figsize=(12, 12)) 
    ax = plt.axes(projection='3d') 
    ax.set_title('Phase Portrait');
    ax.plot3D(x_path, y_path, z_path, 'b');

    fig = plt.figure(figsize=(15, 7)) 
    ax = plt.axes()

    ax.plot(x_path, color = 'b');
    ax.plot(y_path, color = 'orange');
    ax.plot(z_path, color = 'r');
    ax.set_title('Dynamic Path');