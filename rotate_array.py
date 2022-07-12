#Monk and Rotation(https://www.hackerearth.com/)
#Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

#Video approach to solve this question: here

#Input:
#The first line will consists of one integer T denoting the number of test cases.
#For each test case:
#1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
#2) The next line consists of N space separated integers , denoting the elements of the array A.

#Output:
#Print the required array.
# 1 <=T <= 20
# 1 <= N <= 10^5
# 0 <= K <= 10^6
# 0 <= A[i] <= 10^6

#Constraints:


#Sample Input
#1
#5 2
#1 2 3 4 5
#Sample Output
#4 5 1 2 3
#Explanation
#Here T is 1, which means one test case.
# denoting the number of elements in the array and , denoting the number of steps of rotations.
#The initial array is: 
#In first rotation, 5 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be 
#In second rotation, 4 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be 

T = int(input( "Enter integer T, the number of test cases, between 1 and 20, inclusive: "))
i = 1
while i <= T:
    print(i,'. TEST:')
    N, K = map(int, input("Enter an integers N, number of elements in the array between 1 and 10^5 and K, number of steps of rotation between 0 and 10^6, separated by single spaces: ").split())
    A = list(map(int, input("Enter space-separated " + str(N) + " integers , between 0 and 10^6 : ").split()))
    j = int()
    l = 1
    while l <= K:
        E = A[N-1]
        A.pop(N-1)
        A.insert(0, E)
        l +=1
    print(K, 'times rotate array: ',*A,'\n')
    i +=1

   # SHORT VESRION nefunguje
   #
   # t = int(raw_input())
   # while t!=0:
   #    n.k = map(int, raw_input().split())
   #    arr = map(int, raw_input().split())
   #    index = n- (k%n)
   #    for i in range(index,n)
   #        print arr[i],
   #    for i in range(index):
   #        print arr [i], 
   #    print ""
   #    t-=1
    


