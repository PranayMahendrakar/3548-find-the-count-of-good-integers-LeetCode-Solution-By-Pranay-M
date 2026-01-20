class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        from math import factorial
        from collections import Counter
        
        # Generate all n-digit palindromes divisible by k
        # An n-digit palindrome is determined by its first ceil(n/2) digits
        
        half = (n + 1) // 2
        seen_digit_multisets = set()
        
        # Generate all half-length prefixes
        start = 10 ** (half - 1) if half > 1 else 0
        end = 10 ** half
        
        for prefix in range(max(1, start), end):  # First digit can't be 0
            # Build palindrome from prefix
            s = str(prefix)
            if n % 2 == 1:
                palindrome_str = s + s[-2::-1]
            else:
                palindrome_str = s + s[::-1]
            
            palindrome = int(palindrome_str)
            
            # Check if divisible by k
            if palindrome % k == 0:
                # Get sorted digit multiset as a key
                digit_multiset = tuple(sorted(palindrome_str))
                seen_digit_multisets.add(digit_multiset)
        
        # For each unique digit multiset, count how many n-digit numbers can be formed
        total = 0
        
        for digit_multiset in seen_digit_multisets:
            # Count permutations of digits that form valid n-digit numbers (no leading zero)
            digits = list(digit_multiset)
            digit_counts = Counter(digits)
            
            # Total permutations
            total_perms = factorial(n)
            for cnt in digit_counts.values():
                total_perms //= factorial(cnt)
            
            # Subtract permutations with leading zero
            if '0' in digit_counts and digit_counts['0'] > 0:
                # Fix 0 at first position, count remaining permutations
                digit_counts['0'] -= 1
                leading_zero_perms = factorial(n - 1)
                for cnt in digit_counts.values():
                    leading_zero_perms //= factorial(cnt)
                digit_counts['0'] += 1
                total_perms -= leading_zero_perms
            
            total += total_perms
        
        return total