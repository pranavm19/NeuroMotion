import sys
sys.path.append('.')

import os
import numpy as np
import matplotlib.pyplot as plt
from easydict import EasyDict as edict

from NeuroMotion.MNPoollib.MNPool import MotoneuronPool
from NeuroMotion.MNPoollib.mn_params import mn_default_settings


if __name__ == '__main__':
    # Test example with dummy muscle
    num_mu = 186
    muscle = "dummy"
    mn_pool = MotoneuronPool(num_mu, muscle, **mn_default_settings)

    # Excitation
    fs = 2048           # Hz
    duration = 30       # s
    times = np.linspace(0, duration, duration * fs)
    ext = np.concatenate((
        np.zeros(round(fs * 2)),
        np.linspace(0, 0.4, round(fs * 3)),
        np.ones(round(fs * 20)) * 0.4,
        np.linspace(0.4, 0, round(fs * 3)),
        np.zeros(round(fs * 2))
    ))

    # Force and Twitches
    mn_pool.init_twitches(fs)
    mn_pool.init_quisistatic_ef_model()
    _, spikes, fr, ipis = mn_pool.generate_spike_trains(ext)

    # Visualisation using eventplot
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    
    # Convert spike times to seconds for plotting
    spike_times_list = []
    for mu in range(len(spikes)):
        spike_times = np.array(spikes[mu]) / fs  # Convert sample indices to seconds
        spike_times_list.append(spike_times)
    
    # Use eventplot to plot spikes
    ax.eventplot(spike_times_list, colors='black', linewidths=0.5, linelengths=0.8)
    
    ax.set_xticks(range(0, duration + 1, 2))
    ax.set_xticklabels([str(i) for i in range(0, duration + 1, 2)])
    ax.set_ylabel('Discharge Patterns (MU index)', fontsize=14)
    ax.set_xlabel('Time (s)', fontsize=14)
    ax.xaxis.set_tick_params(labelsize=11)
    ax.yaxis.set_tick_params(labelsize=11)
    ax.set_ylim(-0.5, len(spikes) - 0.5)

    # Add excitation signal on secondary y-axis
    ax2 = ax.twinx()
    ax2.plot(times, ext, linewidth=4, c='#003366', alpha=0.3)
    ax2.tick_params(axis='y')
    ax2.set_ylabel('Neural input', fontsize=14)
    ax2.set_yticks([0, 0.3])
    ax2.set_yticklabels(['0.0', '0.3'])
    ax2.xaxis.set_tick_params(labelsize=11)
    ax2.yaxis.set_tick_params(labelsize=11)
    plt.show()

    mn_pool.display_onion_skin_theory(spikes, duration, fs)