class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        satisfied_cus = 0
        additional_sat_cus = 0
                for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied_cus += customers[i]
        
        curr_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                curr_sum += customers[i]
        
        additional_sat_cus = curr_sum
        
        for left in range(1, len(customers) - minutes + 1):
            if grumpy[left - 1] == 1:
                curr_sum -= customers[left - 1]
            if grumpy[left + minutes - 1] == 1:
                curr_sum += customers[left + minutes - 1]
            
            additional_sat_cus = max(additional_sat_cus, curr_sum)
        
        return satisfied_cus + additional_sat_cus
