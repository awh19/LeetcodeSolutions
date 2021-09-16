class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,1]
        
        for i in range(n-1):
            temp = dp[0]
            dp[0] = dp[0]+dp[1]
            dp[1] = temp
            
        return dp[0]
        
        #NOTES LEARNED FROM THIS:
        # Bottom-Up Approach: Start at base case (last number) and work your way up using solutions of subproblems to figure out other problems
        # If you draw out on tree this will show you all you need to know based on number that you are on
        