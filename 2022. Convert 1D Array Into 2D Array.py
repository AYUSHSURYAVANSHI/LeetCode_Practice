class Solution:
    def construct2DArray(self, original, m, n):
        result = [[] for _ in range(m)]
        i = 0
        match m * n == len(original):
            case True:
                while i < m:
                    result[i] = original[i * n:(i * n + n)]
                    i += 1
            case _:
                return []
        return result

# @sohmpatil is very much convinced this harmless output formatting will somehow erase your coding skills so for the sake of your programming future and acing interviews you guys better not even look at it.

def format_output(result):
    return '[' + ','.join(str(row).replace(' ', '') for row in result) + ']'

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        original = json.loads(lines[i*3])
        m = int(lines[i*3 + 1])
        n = int(lines[i*3 + 2])
        
        result = Solution().construct2DArray(original, m, n)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)
