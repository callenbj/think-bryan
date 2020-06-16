import pylab as pl
#import scipy.integrate as spi
import math
import csv
import random
import numpy as np
import time
from datetime import datetime
from numpy import exp, cos, linspace
#import matplotlib.pyplot as plt
import os, time, glob
my_path = os.path.abspath(__file__)

from numpy import zeros, linspace
import matplotlib.pyplot as plt


def social_dist(contacts, population):
    # 25% of the population reduces contact to 50% of normal then (1-(1-.5^2)*.25))
    social_outcome = (1 - (1-contacts*contacts)*population)
    return social_outcome



#def sir_method(gamma, beta, days, cases, pop, recovered, county):
def sir_method(population, recovered, days, days_to_recovery, rate_of_reproduction, deaths, cases):

    pop = population - (deaths + cases)

    gamma = 1/days_to_recovery
    beta = rate_of_reproduction*gamma
    S = 1 - cases / pop
    R = recovered / pop
    I = cases / pop
    T = days #days/10
    dt = 1 # .1
    ii = 1

    NN = T/dt
    #ii = 1
    N = S + I + R



    AA = []

    AA.append([ii, S, I, R])


    while ii < NN:
        dR = gamma * I
        dI = beta * S * I - gamma * I
        dS = -beta * S * I

        S = S + dS*dt
        I = I + dI*dt
        R = R + dR*dt

        ii = ii + 1
        AA.append([ii, S, I, R])




    headers = ['day', 'S', 'I', 'R']

    # This block is for graphing and will most likely not be in the final product

    RES = None
    pl.clf()

    RES = np.array(AA)
    pl.plot(RES[:, 1], '-g', label='Susceptibles')
    pl.plot(RES[:, 3], '-k', label='Recovereds')
    pl.plot(RES[:, 2], '-r', label='Infectious')
    pl.legend(loc=0)
    pl.title('Projected Spread')
    pl.xlabel('Time (days)')
    pl.ylabel('Proportion of Population')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    pl.savefig(plotfile)
    return plotfile


def sir_method_contact(population, recovered, days, days_to_recovery, rate_of_reproduction, deaths, cases, contacts, parpop):


    pop = population - (deaths + cases)


    gamma = 1/days_to_recovery

    gammaC = gamma

    basic_repo = rate_of_reproduction

    beta = rate_of_reproduction*gamma

    iso_ratio = social_dist(contacts, parpop)

    effective_repo = iso_ratio*basic_repo

    betaC = effective_repo * gamma


    S = 1 - cases / pop
    R = recovered / pop
    I = cases / pop
    T = days #days/10
    dt = 1 # .1
    ii = 1

    SC = S
    RC = R
    IC = I

    NN = T/dt
    #ii = 1
    N = S + I + R



    AA = []
    AAC = []
    AACC = []

    AA.append([ii, S, I, R])

    AACC.append([ii, I, IC])

    AAC.append([ii, SC, IC, RC])


    while ii < NN:
        dR = gamma * I
        dRC = gammaC * IC

        dI = beta * S * I - gamma * I
        dIC = betaC * SC * IC - gammaC * IC

        dS = -beta * S * I
        dSC = -betaC * SC * IC

        S = S + dS*dt
        I = I + dI*dt
        R = R + dR*dt

        SC = SC + dSC*dt
        IC = IC + dIC*dt
        RC = RC + dRC*dt


        ii = ii + 1
        AA.append([ii, S, I, R])


        AAC.append([ii, SC, IC, RC])

        AACC.append([ii, I, IC])



    headers = ['day', 'S', 'I', 'R']

    headers2 = ['day', 'IC', 'I']

    # This block is for graphing and will most likely not be in the final product

    RES = None
    pl.clf()

    RES = np.array(AACC)
    pl.plot(RES[:, 1], '-r', label='Infected')
    pl.plot(RES[:, 2], '-b', label='Infected with Distancing')
    pl.legend(loc=0)
    pl.title('Projected Spread')
    pl.xlabel('Time (days)')
    pl.ylabel('Proportion of Population')
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)
    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    plotfile = os.path.join('static', str(time.time()) + '.png')
    pl.savefig(plotfile)
    return plotfile