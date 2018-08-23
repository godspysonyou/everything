class Finder:
    def findX(self, mat, n, m, x):
        start_n = 0
        start_m = m-1
        while start_n<=n-1 and start_m>=0:
            if mat[start_n][start_m]>x:
                start_m-=1
            elif mat[start_n][start_m]<x:
                start_n+=1
            else:
                return True
        return False

