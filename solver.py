from itertools import permutations 

def allPermutations(str): 
     
     permList = permutations(str) 

     for i in list(permList): 
         print (''.join(perm)) 

if __name__ == "__main__": 
	
    str = 'Imagine Dragons'
    allPermutations(str)
       