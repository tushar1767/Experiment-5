# Longest Common Subsequence (LCS)
# Using Dynamic Programming

def build_lcs_table(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create a DP table filled with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    return dp


def reconstruct_lcs(seq1, seq2, dp):
    i = len(seq1)
    j = len(seq2)
    result = []

    # Trace backward through the DP table
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            result.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return "".join(result)


def print_dp_table(seq1, seq2, dp):
    print("\nDP Table:")

    print("    ", end="")
    for ch in seq2:
        print(ch, end=" ")
    print()

    for i, row in enumerate(dp):
        if i == 0:
            label = "-"
        else:
            label = seq1[i - 1]

        print(label, row)


def lcs(seq1, seq2):
    dp = build_lcs_table(seq1, seq2)
    subsequence = reconstruct_lcs(seq1, seq2, dp)

    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)

    print_dp_table(seq1, seq2, dp)

    print("\nLongest Common Subsequence:", subsequence)
    print("Length of LCS:", dp[len(seq1)][len(seq2)])

    return subsequence


# Brute Force Approach
def brute_force_lcs(seq1, seq2, i=None, j=None):
    if i is None:
        i = len(seq1)
    if j is None:
        j = len(seq2)

    if i == 0 or j == 0:
        return 0

    if seq1[i - 1] == seq2[j - 1]:
        return 1 + brute_force_lcs(seq1, seq2, i - 1, j - 1)

    return max(
        brute_force_lcs(seq1, seq2, i - 1, j),
        brute_force_lcs(seq1, seq2, i, j - 1)
    )


# Memoization Approach
def memoized_lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)
    memo = {}

    def helper(i, j):
        if i == 0 or j == 0:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if seq1[i - 1] == seq2[j - 1]:
            memo[(i, j)] = 1 + helper(i - 1, j - 1)
        else:
            memo[(i, j)] = max(
                helper(i - 1, j),
                helper(i, j - 1)
            )

        return memo[(i, j)]

    return helper(m, n)


# Main Program
if __name__ == "__main__":
    seq1 = "ABCBDAB"
    seq2 = "BDCABA"

    lcs(seq1, seq2)

    print("\nBrute Force LCS Length:",
          brute_force_lcs(seq1, seq2))

    print("Memoized LCS Length:",
          memoized_lcs(seq1, seq2))