from setuptools import setup

setup(
   name='Xgression_tk',
   version='2.6',
   description='The Algorithm that find any relationship between data in equation form',
   author='Thaphon Chinnakornsakul',
   author_email='osunchizaza@gmail.com',
   packages=['xgression_tk'],  #same as name
   install_requires=['numpy', 'sympy', 'scipy', 'matplotlib','xgression'],
   long_description="""
# Xgression
## The Dynamic and Explainable Regression/Classification Solution
## Author : Thaphon Chinnakornsakul

Xgression is the solution to find relationships between data to an equation by constructing computational tree that represent the steps of calculation from inputs to an output of algorithm then modify the tree with various operator to find the optimal solution. As the result Xgression can perform many forms of regression without setting initial equations or parameters

Keywords : Theoretical Computer Science, Artificial Intelligence and Machine Learning, Computational Mathematics, Regression, Optimization, Algorithm, Explainable Machine Learning, Computational Tree, Predictive Modelling, Classification

DOI: https://doi.org/10.21203/rs.3.rs-2390968/v1


Reference:
[1]	Nocedal, Jorge; Wright, Stephen J. (2006), Numerical Optimization (2nd ed.), Berlin, New York: Springer-Verlag, ISBN 978-0-387-30303-1
[2]	Python Software Foundation. Python Language Reference, version 3.11. Available at http://www.python.org
[3]	Meurer A, Smith CP, Paprocki M, Čertík O, Kirpichev SB, Rocklin M, Kumar A, Ivanov S, Moore JK, Singh S, Rathnayake T, Vig S, Granger BE, Muller RP,
Bonazzi F, Gupta H, Vats S, Johansson F, Pedregosa F, Curry MJ, Terrel AR, Roučka Š, Saboo A, Fernando I, Kulal S, Cimrman R, Scopatz A. (2017) SymPy:
symbolic computing in Python. *PeerJ Computer Science* 3:e103https://doi.org/10.7717/peerj-cs.103
[4]	Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, Matt Haberland, Tyler Reddy, David Cournapeau, Evgeni Burovski, Pearu Peterson, Warren Weckesser, Jonathan Bright, Stéfan J. van der Walt, Matthew Brett, Joshua Wilson, K. Jarrod Millman, Nikolay Mayorov, Andrew R. J. Nelson, Eric Jones, Robert Kern, Eric Larson, CJ Carey, İlhan Polat, Yu Feng, Eric W. Moore, Jake VanderPlas, Denis Laxalde, Josef Perktold, Robert Cimrman, Ian Henriksen, E.A. Quintero, Charles R Harris, Anne M. Archibald, Antônio H. Ribeiro, Fabian Pedregosa, Paul van Mulbregt, and SciPy 1.0 Contributors. (2020) SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. Nature Methods, 17(3), 261-272.4
[5]	Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).
[6] Visit This [Predict Diabetes Kaggle](https://www.kaggle.com/datasets/whenamancodes/predict-diabities) for testing data

# Note; The Code is still Unclear and unrefactored. i just wrote what i think
# I will definitely refactor this after i pass the university interviewing!!
   """,
   long_description_content_type='text/markdown',
)