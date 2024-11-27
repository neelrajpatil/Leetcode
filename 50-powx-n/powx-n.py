class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        returns x ^ n

        constraints
            -100 < x < 100.0
            -2^31 <= n <= 2^31 -1
            either x!= 0 or n > 0
            -10000 <= x^n <= 10000

        Test cases
            x = 2.0 n = 10 -> 1024
            x = 4.0 n = 2 -> 16
            x = -2.0 n = -2 -> -0.25
            x = 0 n = 1 -> 1
            x = 53 n = 0 -> 0
        """

        # handle edge cases
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x

        
        if n%2 == 0:
            return self.myPow(x*x,n//2)
        else:
            return x * self.myPow(x*x,(n-1)//2)
        
