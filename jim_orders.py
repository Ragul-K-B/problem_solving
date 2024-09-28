"""
Jim has a line of customers, and each customer places an order that takes a certain amount of time to prepare. Each order is identified by a number (the customer's position in line) and a preparation time.

Task:
You need to determine the order in which customers will receive their food based on the total time taken to prepare their orders.

Steps to Solve:
Calculate Total Time: For each customer, calculate the total time as the sum of their order number and the preparation time.

Sort by Delivery Time: Sort the customers based on their total time. If two customers have the same total time, the one who comes first in line (the one with the smaller order number) should be served first.

Return the Order: Finally, return the order in which customers receive their food.

Example:
Customer 1: Order #1, Prep time 3 → Total time = 1 + 3 = 4
Customer 2: Order #2, Prep time 2 → Total time = 2 + 2 = 4
Customer 3: Order #3, Prep time 1 → Total time = 3 + 1 = 4
Since all customers have the same total time, they are served in the order they appear: 1, 2, 3.

The output should reflect the order in which the customers receive their food.
"""
def jimOrders(orders):
    serve_times = [(sum(order), index + 1) for index, order in enumerate(orders)]

    # Sort by serve time first, and then by customer number in case of tie
    serve_times.sort()

    # Return the order of customer numbers based on the sorted serve times
    return [customer[1] for customer in serve_times]
    # Write your code here