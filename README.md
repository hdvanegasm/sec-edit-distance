# Secure Edit Distance

This is an implementation of privacy-preserving edit distance using MPC protocols. Here you will find an implementation of a dynamic programming approach to compute the edit distance in both Python and [MP-SPDZ framework](https://github.com/data61/MP-SPDZ).

## Implementations

### Naïve implementation

The naïve implementation uses a natural encoding for the nucleotids in a DNA chain. The nucleotids are encoded in the set {0, 1, 2, 3}. This implementation compares all the nucleotids in the natural way.

### Optimized implementation

#### Preamble optimization

This implementation encodes the nucleotids as pairs of binary elements, that is, we encode the nucleotids as (0, 0), (0, 1), (1, 0) and (1, 1). The computation of the comparison between nucleotids is performed using bit-wise operators like XOR and OR. This allows us to use the advantage of mixed circuits for computing the edit-distance privately. There are sections of the algorithm that computes comparisons using bit-wise computations, and then the result of these comparisons are transformed to integer shares using daBits/edaBits.

#### Optimization in minimum computation

Additionally, the comparison of the minimum inside the main iteration can be performed in such a way that the number of rounds is reduced with respect to the naïve implementation. Specifically, I reduce the number of rounds by expressing the positions of the matrix `D` as a minimum of more arguments. With this approach I take advantage of the fact that compute the minimum of $k$ elements can be performed in $O(\log_2(k))$ rounds.

