import copy

# https://rabeeaa.wordpress.com/2015/06/11/top-coder-solution-2-dynamic-programming-most-charitable-option/

# Complexity is O(n) in time and O(n) in space, where n is the number of residents/houses 

def best_donation_possible( residents ):
   
    if(len(residents) == 0):
        return 0
    elif(len(residents) == 1):
        return residents[0]
    elif(len(residents) == 2):
        return max(residents)
    elif(len(residents) == 3):
        return max(residents)

    withFirst = [0 for i in range(len(residents) - 3 )] 
    withoutFirst = [0 for i in range(len(residents) -1 )]
    
    residentsWithFirst = copy.deepcopy(residents)
    residentsWithoutFirst = copy.deepcopy(residents)

    helper( residentsWithFirst[2:-1], withFirst )
    helper( residentsWithoutFirst[1:], withoutFirst ) 
   
    
    return max( withFirst[0] + residents[0], withoutFirst[0] )

def helper( residents, DP ):
    j = len(residents) -1 
    i = j 
    while( i >= 0 ):
        if( i == j ):
            DP[j] = residents[j]
        elif i == j - 1:
            DP[i] = max( residents[i], residents[j] )
        else:
            DP[i] = max( DP[i+2] + residents[i], DP[i+1] )
        i = i - 1


def main():
    tests =  [[1],[1,2],[1,2,3],[1,2,3,4], [ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
             6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
             52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 ]]
    
    for t in tests:
        print best_donation_possible( t )


if __name__ == "__main__":
    main()

