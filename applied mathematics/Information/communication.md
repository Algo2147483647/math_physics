# Communication

[TOC]

## Channel

### Channel Capacity

Channel Capacity is the theoretical maximum rate at which information can be reliably transmitted over a communication channel. Channel Capacity is given by the maximum of the mutual information between the input and output of the channel, where the maximization is with respect to the input distribution.
$$
C = \max_{\mathbb P(x)} I(X;Y)
$$

**Shannon–Hartley theorem**
$$
C = B \log_2(1 + \frac{S}{N})
$$

- $C$ is the channel capacity in bits per second, a theoretical upper bound on the net bit rate (information rate, sometimes denoted  $I$) excluding error-correction codes
- $B$ is the bandwidth of the channel in hertz (passband bandwidth in case of a bandpass signal)
- $\frac{S}{N}$ is the signal-to-noise ratio (SNR) or the carrier-to-noise ratio (CNR) of the communication signal to the noise and interference at the receiver (expressed as a linear power ratio, not as logarithmic decibels)