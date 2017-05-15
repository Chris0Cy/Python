from numpy import *

def compute_error_for_current_points(b, m, points):

    #starting out error
    totalError = 0

    #runs for total points we have
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))


def step_gradient_function(b_current_value, m_current_value, points, learningrate):
    b_gradient = 0
    m_gradient = 0

    # N equals the number of points
    N = float(len(points))

    #gradient calculation
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        b_gradient += -(2/N) * (y - ((m_current_value * x) + b_current_value))
        m_gradient += -(2/N) * x * (y - ((m_current_value * x) + b_current_value))

    #updated the actual value of the gradient
    new_b = b_current_value - (learningrate * b_gradient)
    new_m = m_current_value - (learningrate * m_gradient)
    return [new_b, new_m]


#defining gradient descent function
def gradient_descent_function(points, starting_b, starting_m,learning_rate,num_run):

    #data initialization 
    b = starting_b
    m = starting_m

    #
    for i in range (num_run):
        b, m = step_gradient_function(b,m, array(points), learning_rate)
    return [b, m]

def run():
    points = genfromtxt('data.csv', delimiter =',') 

    #defines how fast the machine learns
    learning_rate = 0.00001
    
    #defining the y = mx+b slope functions
    starting_b = 0
    starting_m = 0

    #how many times should we run training
    num_run = 1000

    #set the best value for b and m from gradient decsent function
    [b,m] = gradient_descent_function(points, starting_b, starting_m, learning_rate, num_run)
    
    #prints out the best value of b and m
    print("The best value for b is")
    print(b)
    print("The best value m is")
    print(m)

if __name__ == '__main__':
    run()