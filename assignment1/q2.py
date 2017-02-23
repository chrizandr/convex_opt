from cvxopt import matrix, solvers
import pdb
'''
The following inequalities are to be used while computing the function min{ 2(x1) + 3(x2) }
-1(x1) + 0(x2) <= 0;
0(x1) + -1(x2) <= 0;
-1(x1) + -1(x2) <= -1;
1(x1) + 1(x2) <= 2;
-1(x1) + -2(x2) <= -2;
'''
# inequalities equations
A = matrix([
        [-1.0 , 0.0, -1.0, 1.0, -1.0 ],
        [0.0 , -1.0, -1.0, 1.0, -2.0 ]
          ])
# bounds
B = matrix([ 0.0,
             0.0,
            -1.0,
             2.0,
            -2.0 ])
# Cost function
C = matrix([ 2.0,
             3.0 ])

sol = solvers.lp(C,A,B)
print( 'The solution for the inequalities is')
print( 'x1' , sol['x'][0])
print( 'x2' , sol['x'][1])
