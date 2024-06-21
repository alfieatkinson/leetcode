class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        @param customers (list[int]): the amount of customers each minute.
        @param grumpy (list[int]): whether the shopkeeper is grumpy or not each minute.
        @param minutes (int): the number of minutes the shopkeeper's ability lasts.
        @return satisfied (int): the highest possible number of satisfied customers.
        """
        n = len(customers)

        # Invert grumpy list so that grumpy is 0 to cancel out customers on grumpy days
        grumpy = [1 if i == 0 else 0 for i in grumpy]

        # Cancel out customers on grumpy days and get sum of customers on non grumpy days
        satisfied = sum([customers[i] * grumpy[i] for i in range(0, n)]) 
        max_sat = satisfied

        print(f"Satisfied customers with no ability used: {satisfied}.")

        for i in range(0, minutes):
            if grumpy[i] == 0:
                satisfied += customers[i]
        
        if satisfied > max_sat: max_sat = satisfied

        print(f"Satisfied customers with ability used in minute 1: {satisfied}.")

        for i in range(1, n - minutes + 1):
            print(f"Customers: {customers[i:i+minutes]}")
            if grumpy[i - 1] == 0:
                satisfied -= customers[i - 1]
            if grumpy[i + minutes - 1] == 0:
                satisfied += customers[i + minutes - 1]

            if satisfied > max_sat: max_sat = satisfied
            print(f"Satisfied customers with ability used in minute {i + 1}: {satisfied}.")

        return max_sat
    
S = Solution()

customers = [1,0,1,2,1,1,7,5]
grumpy =    [0,1,0,1,0,1,0,1]
minutes = 3

print(S.maxSatisfied(customers, grumpy, minutes))