class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        if lena != lenb:
            return False
        if lena == 0:
            return True
        big = "" + A + A
        length = len(big)
        # KMP
        for i in range(length-lena):
            if big[i:i+lena] == B:
                return True
        return False
