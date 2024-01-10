import math
import matplotlib.pyplot as plt
from .generaldistribution import GeneralDistribution


class Gaussian(GeneralDistribution):
    def __init__(self, mu=0, sigma=1):
        GeneralDistribution.__init__(self,mu, sigma)

    def calculate_mean(self):
        avg=float(sum(self.data)/len(self.data))
        self.mean=avg
        return avg
    
    def calculate_stdev(self, sample=True):
        if sample:
            size=len(self.data)-1
        else:
            size=len(self.data)
            
        sum_diff=0
        
        for x in self.data:
            sum_diff+=(x-self.mean)**2
            
        st_dev=math.sqrt(sum_diff/size)
        self.stdev=st_dev
        
        return self.stdev

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using 
        matplotlib pyplot library."""
        
        plt.hist(self.data)
        plt.xlabel("Data")
        plt.ylabel("Frequency")
        plt.title("Data-Frequency Histogram")
    
    def pdf(self, x):
        pdf=(1.0/math.sqrt(2*math.pi*self.stdev**2))*(math.exp(-0.5*((x-self.mean)/self.stdev)**2))
        return pdf
    
    def plot_histogram_pdf(self, n_spaces = 50):

        """Method to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """   
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
    
    def __add__(self, other):
        result = Gaussian()
        result.mean = self.mean+other.mean
        result.stdev = math.sqrt(self.stdev**2 + other.stdev**2)
        return result
    
    def __repr__(self):
        return "mean {}, standard deviation {}".format(self.mean,self.stdev)