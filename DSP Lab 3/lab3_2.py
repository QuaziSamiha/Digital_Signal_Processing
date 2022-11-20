from asyncio import StreamReaderProtocol
from sre_constants import SRE_FLAG_TEMPLATE
import numpy as np
import matplotlib.pyplot as plt

N = 100

fwhm = 50
# Gtime = 1000*np.arange(-N,N)/srate