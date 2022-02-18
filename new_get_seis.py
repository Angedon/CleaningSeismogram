#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#import segyio
#import numpy as np
#from tensorboard.plugins.hparams import keras


def get_seis(in_file, out_file):
    seis = segyio.open(in_file, ignore_geometry=True)
    model = keras.models.load_model("new_СDNN.hdf5")
    trace = []
    for i in range(len(seis.trace)):
        trace.append(seis.trace[i])

    matrix = np.stack(trace,axis = 0)

    new_matrix = np.ndarray(matrix.shape)

    for i in range(len(matrix[:,0])):
        trace = matrix[i, :]
        trace = np.reshape(trace, trace.shape + (1,))
        trace = trace.T
        trace = np.reshape(trace, trace.shape + (1,))
        result = model.predict(x = trace, verbose = 1)
        new_matrix[i, :] = result[0, :].flatten()

    a,b = matrix.shape
    spec = segyio.spec()
    spec.sorting = 1
    spec.format = 5
    spec.tracecount = a
    spec.samples = np.arange(1,b+1,1)
    spec.iline = 1
    spec.xline = 1

    seg2 = segyio.create(out_file,spec)

    for i in range(a):
        seg2.trace[i] = np.float32(new_matrix[i,:]) 

    seg2.header = seis.header
    seg2.flush()
    
    return seg2

