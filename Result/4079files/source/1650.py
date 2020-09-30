import numpy as np
import matplotlib.pyplot as plt

class Plots:
    @staticmethod
    def plot(x:np.ndarray, D:np.ndarray=None, label:str='y[n]', title:str=None, 
            legend:str=None, place:int=111):
        """ plots the array x over the definition range D
            
            Uses a stem-Plot to display the values of x[n] over all n in D
            :param x: {numpy.ndarray} Array containing the values of the Signal
            :param D: {numpy.ndarray} Array containing all indices (the definition range of the signal) (optional, if not given, a suitable array will be generated)
            :param label: {str} A label for the y Axis (optional)
            :param title: {str} A title for the figure (optional)
            :param legend: {str} The Legend for the plot
            :param place: {int} Integer describing the place of the subplot
            :returns: The Axes Object of the figure
        """
        if not isinstance(D, np.ndarray) or len(D) == 0:
            D = np.array([np.arange(0, len(x))]).T
        if(place == None):
            fig, axes = plt.subplots()
        else:
            axes = plt.subplot(place)
        axes.stem(D, x, basefmt='k-')
        axes.set_xticks(D)
        axes.set_xlabel('n')
        axes.set_ylabel(label)
        if title != None: axes.set_title(title)
        if legend == None or len(legend) < 1:
            legend = label
        axes.legend([legend])
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        return axes
        
    @staticmethod
    def plotRealAndImag(vector:np.ndarray, n:np.ndarray, title:str = None, 
                        place:int=111, label:str=None):
        """ plots the array vector over all values of n, splitted into real and 
            imaginary part
            
            Uses a stem-Plot to display the real and imaginary values of x[n] over all n
            The real part is in blue, the imaginary in red
            :param vector: {numpy.ndarray} Array containing the values of the complex Signal
            :param n: {numpy.ndarray} Array containing all indices (the definition range of the signal) (optional, if not given, a suitable array will be generated)
            :param label: {str} A label for the y Axis (optional)
            :param title: {str} A title for the figure (optional)
            :param place: {int} Integer describing the place of the subplot
            :returns: The Axes Object of the figure
        """
        axes = plt.subplot(place)
        axes.stem(n, np.real(vector), markerfmt='bo', linefmt='b-', basefmt='k-') # in blue
        axes.stem(n, np.imag(vector), markerfmt='ro', linefmt='r-', basefmt='k-')# in red
        axes.set_xlabel("n")
        axes.set_xticks(n)
        if label != None: axes.set_ylabel(label)
        if title != None: axes.set_title(title) 
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        axes.legend(['$\Re{('+title.strip('$')+')}$','$\Im{('+title.strip('$')+')}$'])
        return axes

class FPlots:
    @staticmethod
    def plot(func, D, ylabel:str,legend:str=None):
        """ plots the function func over the definition range D
            
            Uses a stem-Plot to display the values of func(n) over all n in D
            :param func: {callable} Function for creating the values x[n] to be plotted
            :param D: {numpy.ndarray or list} Array containing all indices (the definition range of the signal)
            :param label: {str} A label for the y Axis (optional)
            :param legend: {str} The Legend for the plot
            :returns: The Axes Object of the figure
        """
        y = [func(n) for n in D]
        fig, axes = plt.subplots()
        axes.stem(D, y, basefmt='k-')
        axes.set_xticks(D)
        axes.set_xlabel('n')
        axes.set_ylabel(ylabel)
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        if legend == None or len(legend) < 1:
            legend = ylabel
        axes.legend([legend])
        return axes
    
    @staticmethod
    def Magnitude(x, ylabel:str, legend:str=None, place:int=111):
        """ plots the magnitude of the function x over -2pi : 2pi
        
            :param x: {callable} the function to be plotted
            :param ylabel: {str} label for the y axis
            :param legend: {str} Text for the legend
            :param place: {int} placement of the subplot
            :returns: The Axes Object
        """
        thetax = np.linspace(-2*np.pi, 2*np.pi, 10000)
        axes = plt.subplot(place)
        axes.plot(thetax, abs(x(thetax)))
        axes.set_xlabel('$\Theta$')
        axes.set_ylabel(ylabel)
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi/2),
                        ('$-2\pi$','$-3\pi/2$','$-\pi$','$-\pi/2$','0',
                         '$\pi/2$','$\pi$','$3\pi/2$','$2\pi$'));
        #axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        if legend == None or len(legend) < 1:
            legend = ylabel
        axes.legend([legend])
        return axes
    
    @staticmethod
    def Phase(x, ylabel:str, legend:str=None, place:int=111):
        """ plots the phase of the function x over -2pi : 2pi
        
            :param x: {callable} the function to be plotted
            :param ylabel: {str} label for the y axis
            :param legend: {str} Text for the legend
            :param place: {int} placement of the subplot
            :returns: The Axes Object
        """
        thetax = np.linspace(-2*np.pi, 2*np.pi, 10000)
        axes = plt.subplot(place)
        axes.plot(thetax, np.angle(x(thetax)) * (180.0/np.pi))
        axes.set_xlabel('$\Theta$')
        axes.set_ylabel(ylabel)
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi/2),
                        ('$-2\pi$','$-3\pi/2$','$-\pi$','$-\pi/2$','0',
                         '$\pi/2$','$\pi$','$3\pi/2$','$2\pi$'));
        if legend == None or len(legend) < 1:
            legend = ylabel
        axes.legend([legend])
        return axes
    
    @staticmethod
    def X(x, ylabel:str, legend:str=None, place:int=111):
        """ plots the function x over -2pi : 2pi
        
            :param x: {callable} the function to be plotted
            :param ylabel: {str} label for the y axis
            :param legend: {str} Text for the legend
            :param place: {int} placement of the subplot
            :returns: The Axes Object
        """
        thetax = np.linspace(-2*np.pi, 2*np.pi, 10000)
        axes = plt.subplot(place)
        axes.plot(thetax, x(thetax))
        axes.set_xlabel('$\Theta$')
        axes.set_ylabel(ylabel)
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi/2),
                        ('$-2\pi$','$-3\pi/2$','$-\pi$','$-\pi/2$','0',
                         '$\pi/2$','$\pi$','$3\pi/2$','$2\pi$'));
        if legend == None or len(legend) < 1:
            legend = ylabel
        axes.legend([legend])
        return axes
    
    @staticmethod
    def Real(x, ylabel:str, legend:str=None, place:int=111):
        """ plots the real part of the function x over -2pi : 2pi
        
            :param x: {callable} the function to be plotted
            :param ylabel: {str} label for the y axis
            :param legend: {str} Text for the legend
            :param place: {int} placement of the subplot
            :returns: The Axes Object
        """
        thetax = np.linspace(-2*np.pi, 2*np.pi, 10000)
        axes = plt.subplot(place)
        axes.plot(thetax, np.real(x(thetax)))
        axes.set_xlabel('$\Theta$')
        axes.set_ylabel(ylabel)
        axes.grid(b = None, which = 'both', axis = 'both', linestyle = '--')
        plt.xticks(np.arange(-2*np.pi,2*np.pi+1,np.pi/2),
                        ('$-2\pi$','$-3\pi/2$','$-\pi$','$-\pi/2$','0',
                         '$\pi/2$','$\pi$','$3\pi/2$','$2\pi$'));
        if legend == None or len(legend) < 1:
            legend = ylabel
        axes.legend([legend])
        return axes
    
class Transforms:
    @staticmethod
    def convolute(x, y, n:int, D) -> int:
        """ Convolute the two functions x and y at n, using all elements in D
            
            :param x: Function for the signal x
            :param y: Function for the signal y
            :param n: specific index n for which to evaluate
            :param D: definition range of the functions
            :returns: int for the specified index
        """
        return sum([x(k) * y(n-k) for k in D])
    
    #@staticmethod
    #def dtft(x, D, theta):
    #    """ Seems to be not working
    #    """
    #    return sum([x(n) * np.exp(-1j*theta*n) for n in D])

class Signal:  
    # UNIT STEP
    @staticmethod
    def u(n: int) -> int:
        """ unit step function,
            returns 1 if n equals or is larger than 0
            for vector inputs, use VectorSignal.u !
            
            :param n: {int} Indexarray
            :returns: int
        """
        if n >= 0: return 1
        else: return 0
    
    # KRONECKER DELTA
    @staticmethod
    def d(n: int) -> int:
        """ kronecker delta function
            returns 1 if n equals 0
            for vector inputs, use VectorSignal.d !
            
            :param n: {int} index
            :returns: 1 / 0
        """
        if n == 0: return 1
        else: return 0

    # CONJUGATE TRANSPOSED
    @staticmethod
    def hermitianTransposed(x):
        return np.conj(x).T
        
    def create(func, D):
        ary = np.array([[func(ni) for ni in D[:,0]]])
        if(ary.shape[1] > 1):
          ary = ary.T
        return ary
        
class VectorSignal:
    # UNIT STEP
    @staticmethod
    def u(n:np.ndarray, n1:int=0) -> np.ndarray:
        """ unit step function
            returns an np.array which contains a 1 at each index, where n equals or is larger than n1
            
            :param n: {np.ndarray} Indexarray
            :param n1: {int} offset (optional)
            :returns: np.array
        """
        ary = np.zeros(n.shape);
        ary[n >= n1] = 1;
        return ary;
    
    # KRONECKER DELTA
    @staticmethod
    def d(n:np.ndarray, n1:int=0) -> np.ndarray:
        """ kronecker delta function
            returns an np.array which contains a 1 at each index, where n equals to n1
            
            :param n: {np.ndarray} Indexarray
            :param n1: {int} offset (optional)
            :returns: np.array
        """
        ary = np.zeros(n.shape);
        ary[n == n1] = 1;
        return ary;