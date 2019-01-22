ny_temp1= [53.9, 46.3, 36.4,33.4,14.5,65.8,46.8,25.0,15.3,24.0,26.7]
ny_temp2= [43.9, 56.3, 56.4,23.4,24.5,75.8,26.8,45.0,45.3,54.0,46.7]
ny_temp3= [33.9, 66.3, 46.4,53.4,34.5,35.8,36.8,35.0,35.3,84.0,6.7]
years = range(2000,2011)
from pylab import plot, show
plot(years,ny_temp1, years,ny_temp2,years,ny_temp3,marker='o')
show()