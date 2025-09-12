import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5, 6])

#sales data for three products
product_a = np.array([10, 15, 13, 17, 20, 22])
product_b = np.array([12, 14, 16, 18, 21, 23])
product_c = np.array([14, 13, 15, 19, 22, 24])

#plotting sales data
plt.plot(x, product_a, marker='o', label='Product A')
plt.plot(x, product_b, marker='s', label='Product B')   
plt.plot(x, product_c, marker='^', label='Product C')
plt.title('Sales Data Over 6 Months')
plt.xlabel('Month')
plt.ylabel('Sales(in units)')
plt.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
plt.legend()
plt.grid(True)
plt.savefig('sales_data_chart.png')
plt.show()