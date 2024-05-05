import numpy as np
from DWC_F import eig_e_corr
import matplotlib.pyplot as plt
from collections import Counter

def TVQC_prob(bias, amplitude, phase, sample_rate, N_samples, freq=1, d=2):
    '''
    Sampling the probability distribution of time-varying Pauli channels.

    Parameters
    ----------
    bias : Double.
        mean of coefficient of exponential correlatoon.
    amplitude : Double
        amplitude of variation in coefficient of exponential correlation.
        0 <= bias - amplitude, bias + amplitude <= 1
    sample_rate : Double
        sampling rate from quantum channel.
    N_samples : integer
        number of samples to gather from quantum channel.
    freq : double
        frequency of time variation.
    d : integer, optional
        Dimension of Pauli channel. The default is 2.

    Returns
    -------
    N_sample time-varying pmfs of d^2 alphabet.

    '''
    gamma = [bias + amplitude * np.sin(phase + 2 * np.pi * freq * time / sample_rate) \
             for time in range(N_samples)]
    time_v = [tt / sample_rate for tt in range(N_samples)]
    probs = [np.sort(eig_e_corr(2, gg))[::-1] for gg in gamma]
    return probs, time_v


def fix_channel_estimate(k, p):
    '''1-repetition code for time-varying BSC with cross-over probability
    1 - p. p is time-varying vector. Message known to receiver = direct
    tomography'''
    N = len(p)  # total channel uses
    k = 1

    mess_bits = int(np.floor(N / k))  # message length
    if mess_bits == 0:
        print(k, mess_bits, N)
        print("XXXXXX k too large for available channel uses XXXXXX")
    #### Using channel only for k x mess_bits uses for first
    # k = 1 since no message encoding
    p = p[0:k * mess_bits]
    mess = np.random.choice(2, mess_bits)  # binary message of len N/k
    enc = np.matlib.repmat(mess, k, 1).T
    err = np.reshape(np.random.choice([0, 1], N, p=p[-1]), [k, mess_bits]).T
    # err = np.reshape([np.random.choice([0,1], 1, p=prob) \
    #                  for prob in p], [k, mess_bits]).T
    # err = np.reshape(np.random.choice([0,1], len(p), p=p), [k, N]).T
    rx = np.mod(enc + err, 2)
    maj_vote = [Counter(m).most_common() for m in rx]
    dec = mess  # message known to receiver
    symb_err_rate = (mess_bits - np.sum(mess == dec)) / mess_bits
    # print(mess,"\n", enc, "\n\n", err, "\n\n", rx, "\n\n", maj_vote, "\n\n", dec, "\n\n", symb_err_rate)
    # print(symb_err_rate)
    ### Now estimating the probabilities
    dec_rep = np.matlib.repmat(dec, k, 1).T
    err_est = np.mod(rx - dec_rep, 2)
    rx_hamm_weight = np.sum(rx, axis=1)  # since binary
    free_bits = np.abs(k / 2 - rx_hamm_weight) - 0.5
    # print(np.mean(free_bits), Counter(free_bits).most_common()[0:2])
    # print(Counter(err_est.reshape([1, k*N])[0]).most_common())
    err_counts = Counter(err_est.reshape([1, k * mess_bits])[0]).most_common()
    est_prob = np.zeros(2)
    for kk in err_counts:
        est_prob[kk[0]] = kk[1] / (k * mess_bits)
    # print(p, "\n\n", est_prob)
    return (symb_err_rate, est_prob, Counter(free_bits).most_common())


# %%
#

def fixed_tomography(N_tomo, freq, k, bias, amplitude, sample_rate, phase):
    #N_tomo = 1000  # number of channel uses in each estimate
    #tot_exp = 20  # total number of times we want estimation
    N_samples = N_tomo
    #freq = 1
    k_curr_x, k_curr_y, k_curr_z = k[0], k[1], k[2]
    k_x, k_y, k_z = [], [], []
    #ch_estimates = []
    #DN_distance = []
    #bias, amplitude, phase, sample_rate \
    #    = 0.8, 0.2, np.pi / 2, 10_000
    #phase = 0
    probs, time_v = TVQC_prob(bias, amplitude, phase, sample_rate, N_samples, \
                              freq=freq)

    #time_snaps = np.round(np.arange(0, N_samples + 1, \
    #                                int(np.round(N_samples / tot_exp))))


    N_basis = int(N_samples / 3)  # number of samples for each basis
    ch_varying = probs
    ch_varying_for_x = ch_varying[:N_basis]
    ch_varying_for_y = ch_varying[N_basis + 1:2 * N_basis]
    ch_varying_for_z = ch_varying[2 * N_basis:]
    ch_varying_x = [[prob[0] + prob[1], 1 - prob[0] - prob[1]] \
                    for prob in ch_varying_for_x]
    ch_varying_y = [[prob[0] + prob[2], 1 - prob[0] - prob[2]] \
                    for prob in ch_varying_for_y]
    ch_varying_z = [[prob[0] + prob[3], 1 - prob[0] - prob[3]] \
                    for prob in ch_varying_for_z]
    # simulating the corresponding BSCs
    err_x, prob_x, free_b_x = fix_channel_estimate(k_curr_x, ch_varying_x)
    free_b_m_x = min(free_b_x, key=lambda t: t[0])  # min free bits
    #
    err_y, prob_y, free_b_y = fix_channel_estimate(k_curr_y, ch_varying_y)
    free_b_m_y = min(free_b_y, key=lambda t: t[0])  # min free bits
    #
    err_z, prob_z, free_b_z = fix_channel_estimate(k_curr_z, ch_varying_z)
    free_b_m_z = min(free_b_z, key=lambda t: t[0])  # min free bits
    # Estimating the full Pauli channel
    est_Pauli = [0.5 * (prob_x[0] + prob_y[0] + prob_z[0] - 1), \
                 0.5 * (prob_x[0] - prob_y[0] - prob_z[0] + 1), \
                 0.5 * (-prob_x[0] + prob_y[0] - prob_z[0] + 1), \
                 0.5 * (-prob_x[0] - prob_y[0] + prob_z[0] + 1)]
    #ch_estimates.append(est_Pauli)
    # Calculating the diamond norm distance
    DN_distance = np.sum(np.abs(est_Pauli - ch_varying[-1]))
    #DN_distance.append(np.sum(np.abs(est_Pauli - ch_varying[-1])))
    # print(est_Pauli)
    # print(DN_distance)
    return est_Pauli, ch_varying,  DN_distance

##################### Fixed k Start
def rep_code_adaptive(k, p):
    '''k-repetition code for time-varying BSC with cross-over probability
    1 - p. p is time-varying vector.'''
    N = len(p)  # total channel uses

    mess_bits = int(np.floor(N / k))  # message length
    if mess_bits == 0:
        print(k, mess_bits, N)
        print("XXXXXX k too large for available channel uses XXXXXX")
    #### Using channel only for k x mess_bits uses for first
    p = p[0:k * mess_bits]
    mess = np.random.choice(2, mess_bits)  # binary message of len N/k
    enc = np.matlib.repmat(mess, k, 1).T
    err = np.reshape([np.random.choice([0, 1], 1, p=prob) \
                      for prob in p], [k, mess_bits]).T
    # err = np.reshape(np.random.choice([0,1], len(p), p=p), [k, N]).T
    rx = np.mod(enc + err, 2)
    maj_vote = [Counter(m).most_common() for m in rx]
    dec = np.array([c[0][0] for c in maj_vote])
    symb_err_rate = (mess_bits - np.sum(mess == dec)) / mess_bits
    # print(mess,"\n", enc, "\n\n", err, "\n\n", rx, "\n\n", maj_vote, "\n\n", dec, "\n\n", symb_err_rate)
    # print(symb_err_rate)
    ### Now estimating the probabilities
    dec_rep = np.matlib.repmat(dec, k, 1).T
    err_est = np.mod(rx - dec_rep, 2)
    rx_hamm_weight = np.sum(rx, axis=1)  # since binary
    free_bits = np.abs(k / 2 - rx_hamm_weight) - 0.5
    # print(np.mean(free_bits), Counter(free_bits).most_common()[0:2])
    # print(Counter(err_est.reshape([1, k*N])[0]).most_common())
    err_counts = Counter(err_est.reshape([1, k * mess_bits])[0]).most_common()
    est_prob = np.zeros(2)
    for kk in err_counts:
        est_prob[kk[0]] = kk[1] / (k * mess_bits)
    # print(p, "\n\n", est_prob)
    return (symb_err_rate, est_prob, Counter(free_bits).most_common())


# %%
#

def SCAPE_tomography(N_tomo, freq, k, bias, amplitude, sample_rate, phase):
    #N_tomo = 500  # number of channel uses in each estimate
    #tot_exp = 40  # total number of times we want estimation
    N_samples = N_tomo
    #freq = 1
    k_curr_x, k_curr_y, k_curr_z = k[0], k[1], k[2]
    k_x, k_y, k_z = [], [], []
    #ch_estimates = []
    #DN_distance = []
    #bias, amplitude, phase, sample_rate \
    #    = 0.7, 0.3, np.pi / 2, 10_000
    probs, time_v = TVQC_prob(bias, amplitude, phase, sample_rate, N_samples, \
                              freq=freq)

    #time_snaps = np.round(np.arange(0, N_samples + 1, \
    #                                int(np.round(N_samples / tot_exp))))

    #for ii in range(len(time_snaps) - 1):
        # picking channel probabilities for current time period
    ch_varying = probs
    N_basis = int(N_tomo / 3)  # number of samples for each basis
    ch_varying_for_x = ch_varying[:N_basis]
    ch_varying_for_y = ch_varying[N_basis + 1:2 * N_basis]
    ch_varying_for_z = ch_varying[2 * N_basis:]
    ch_varying_x = [[prob[0] + prob[1], 1 - prob[0] - prob[1]] \
                    for prob in ch_varying_for_x]
    ch_varying_y = [[prob[0] + prob[2], 1 - prob[0] - prob[2]] \
                    for prob in ch_varying_for_y]
    ch_varying_z = [[prob[0] + prob[3], 1 - prob[0] - prob[3]] \
                    for prob in ch_varying_for_z]
    # simulating the corresponding BSCs
    err_x, prob_x, free_b_x = rep_code_adaptive(k_curr_x, ch_varying_x)
    free_b_m_x = min(free_b_x, key=lambda t: t[0])  # min free bits
    #
    err_y, prob_y, free_b_y = rep_code_adaptive(k_curr_y, ch_varying_y)
    free_b_m_y = min(free_b_y, key=lambda t: t[0])  # min free bits
    #
    err_z, prob_z, free_b_z = rep_code_adaptive(k_curr_z, ch_varying_z)
    free_b_m_z = min(free_b_z, key=lambda t: t[0])  # min free bits
    # Estimating the full Pauli channel
    est_Pauli = [0.5 * (prob_x[0] + prob_y[0] + prob_z[0] - 1), \
                 0.5 * (prob_x[0] - prob_y[0] - prob_z[0] + 1), \
                 0.5 * (-prob_x[0] + prob_y[0] - prob_z[0] + 1), \
                 0.5 * (-prob_x[0] - prob_y[0] + prob_z[0] + 1)]
    #ch_estimates.append(est_Pauli)
    # Calculating the diamond norm distance
    DN_distance = np.sum(np.abs(est_Pauli - ch_varying[-1]))
    return est_Pauli, ch_varying, DN_distance, [free_b_m_x[0], free_b_m_y[0], free_b_m_z[0]], [err_x, err_y, err_z]

    # plt.plot(time_v, probs, '--')
    # plt.plot(time_v[-1]*np.array(time_snaps[1:])/N_samples, ch_estimates)
    # plt.show()

    # fig, ax1 = plt.subplots(figsize=(8, 4))
    # ax2 = ax1.twinx()
    #
    # ax1.plot(time_v, probs, '--')
    # ax1.plot(time_v[-1] * np.array(time_snaps[1:]) / N_samples, ch_estimates)
    # #
    # ax2.plot(time_v[-1] * np.array(time_snaps[1:]) / N_samples, DN_distance, 'y')
    # ax2.set_ylim(0, 0.4)
    # fig.show()
#################### Fixed k End