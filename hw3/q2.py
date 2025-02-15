"""
def has_subseq(n,seq):
    n_str = str(n)
    if len(n_str)<len(seq_str):
        return False
    for i in range(len(seq_str)):
        judge = True
        for j in range(i,len(n_str)):
            if n_str[j] == seq_str[i]:
                judge = False
                break
        if judge:
            return False
    return True
"""

def has_subseq(n,seq):
    n_str = str(n)
    seq_str = str(seq)
    if len(n_str) < len(seq_str):
        return False
    seq_set = 0
    for char in seq_str:
        if char == n_str[seq_set]:
            seq_set+=1
            if seq_set == len(seq_str):
                return True
    return False

if __name__=='__main__':
    print(has_subseq(123, 12))
    print(has_subseq(141, 11))
    print(has_subseq(144, 12))
    print(has_subseq(144, 1441))
    print(has_subseq(1343412, 134))