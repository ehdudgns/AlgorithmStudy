import sys

def inputData() :
    N = int(sys.stdin.readline())
    consultingSchedule = []
    for _ in range(N):
        consultingSchedule.append([int(i) for i in sys.stdin.readline().split(" ")])
    return consultingSchedule

def run(consultingSchedule):
    n = len(consultingSchedule)
    dp = [0] * (n+6)
    for i in range(n):
        idx = i + consultingSchedule[i][0]
        tmp = max(max(dp[:i+1])+consultingSchedule[i][1], dp[idx])
        for j in range(idx,n+1):
            dp[j] = max(tmp,dp[j])
    print(max(dp[:n+2]))
    

if __name__ == "__main__":
    consultingSchedule = inputData()
    run(consultingSchedule)
