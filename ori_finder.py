def find_ori(sequence, window=1000):
    """
    Predicts the origin of replication using GC skew analysis.
    Returns a subsequence around the predicted ORI.
    """
    max_skew = float("-inf")
    ori_index = 0

    for i in range(0, len(sequence) - window, window):
        window_seq = sequence[i:i+window]
        g = window_seq.count("G")
        c = window_seq.count("C")
        skew = g - c

        if skew > max_skew:
            max_skew = skew
            ori_index = i

    return sequence[ori_index:ori_index + window]
