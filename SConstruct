import os
import glob
from nbflow.scons import setup

env = Environment(ENV=os.environ)
setup(env,["notebooks"])

#round up all the figures/files that are changing
results = sorted(glob.glob('results/*.tex'))
figures = sorted(glob.glob('results/*.pdf'))

#build PDF and tell scons about the dependencies
env.PDF('tex/paper.pdf','tex/paper.tex')
env.Depends('tex/paper.pdf',results + figures)
