from timeit import default_timer



# ===========================================================
# FUNCTION: MaxLeaves
# ===========================================================
#
#  Input:
#       *   triangle:   the "triangle" of data modeled as a
#                       single-dimensional array
#       *   index:      current node index being examined
#       *   rowLen:     the "row length", or the number of
#                       nodes in the row
#
#  Output:  sum of the maximum path length below the current
#           node added to the current node's value.
#
#  Task:    recursively traverse down the "tree" to the leaves,
#           adding the maximum path length below to the current node,
#           up until the initial index parameter (0 to be the entire
#           tree)
#
# ===========================================================
def get_max_leaf_sum( triangle , index , rowLen ):
    # Escape Condition for Recursion (bottom level of tree [modeled as 2d array])
    if ( index + rowLen + 1 ) > len( triangle ):
        return triangle[ index ]

    # Get longest path on left and right branches
    left   =  get_max_leaf_sum( triangle , ( index + rowLen ) , rowLen )
    right  =  get_max_leaf_sum( triangle , ( index + rowLen + 1 ) , rowLen )

    # Return the sum of the current leaf and the longest left/right path
    return triangle[ index ] + max( left , right )



# ===========================================================
# PROBLEM 18 -- Maximum Path Sum I
# ===========================================================
#
#  By starting at the top of the triangle below and moving to
#  adjacent numbers on a row, by the maximum total from the top
#  to the bottom is 23
#                   *3
#                 *7   4
#                2  *4   6
#              8   5  *9   3
#
#  That is, 3 + 7 + 4 + 9 = 23
#
#  Find the maximum total from top to bottom of the triangle in
#  "Problem18_triangle.txt"
#
#  NOTE:
#  As there are only 16384 routes, it is possible to solve this
#  problem by trying every route. However, Problem 67, is the
#  same challenge with a triangle containing one-hundred rows;
#  it cannot be solved by brute force and requires a clever method
#
#  PROGRAM NOTES:
#    *  Data is stored in the following format
#       3
#       7 4
#       2 4 6
#       8 5 9 3
#       Because of this, "same row" means down one, or
#       down one and right one.
#
# ===========================================================
def problem_18( ):
    # Print Problem Context
    print( "Project Euler Problem 18 -- Maximum Path Sum I")

    # Start Timer
    start_time  =  default_timer( )

    # Retrieve Data From File
    file      =  open( "Problem18_Triangle.txt" , 'r' )
    triangle  =  [ int( x ) for x in file.read( ).split( ) ]
    file.close( )

    # Compute Result
    result  =  get_max_leaf_sum( triangle , 0 , 15 )

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Maximum Sum of any Pathway:   %d"      %  result )
    print( "   Computation Time:             %.3fms"  %  execution_time )
    return



if __name__ == '__main__':
    problem_18( )