from functools import reduce

class Solution:
    def window_check(self, customers: list[int], grumpy: list[int], minutes: int, start: int) -> int:
        """
        @param customers (list[int]): the amount of customers each minute.
        @param grumpy (list[int]): whether the shopkeeper is grumpy or not each minute.
        @param minutes (int): the number of minutes the shopkeeper's ability lasts.
        @param start (int): the start of the ability window.
        @return satisfied (int): the amount of satisfied customers with the ability activated in this window.
        """
        n = len(customers)

        grumpy_ability = [i for i in grumpy]

        pointers = ['^' if i == start or i == start + minutes - 1 else ' ' for i in range(0, n)]

        for i in range(start, start + minutes):
            grumpy_ability[i] = 1

        satisfied_customers = [customers[i] * grumpy_ability[i] for i in range(0, n)]

        print(f"""
Customers:           {customers}
Grumpy:              {[1 if i == 0 else 0 for i in grumpy]}
Grumpy with window:  {[1 if i == 0 else 0 for i in grumpy_ability]}
                     {f" {'  '.join(pointers)} "}
Satisfied customers: {satisfied_customers}
""")

        satisfied = sum(satisfied_customers)

        return satisfied

    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        @param customers (list[int]): the amount of customers each minute.
        @param grumpy (list[int]): whether the shopkeeper is grumpy or not each minute.
        @param minutes (int): the number of minutes the shopkeeper's ability lasts.
        @return satisfied (int): the highest possible number of satisfied customers.
        """
        n = len(customers)

        # Invert grumpy list so that grumpy is 0 to cancel out customers on grumpy days
        inverted_grumpy = [1 if i == 0 else 0 for i in grumpy] 

        # Cancel out customers on grumpy days and get sum of customers on non grumpy days
        satisfied = sum([customers[i] * inverted_grumpy[i] for i in range(0, n)]) 

        window = 0
        for i in range(0, n - minutes + 1):
            window_sat = self.window_check(customers, inverted_grumpy, minutes, i)
            if window_sat > satisfied: satisfied = window_sat

        return satisfied
    
S = Solution()

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

print(S.maxSatisfied(customers, grumpy, minutes))