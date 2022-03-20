import math

def concatenation(a):
  
    basis = 0
    bagian_eksponen = 1
    con_num = 0
    
    if isinstance(a, list):
        
        for i in range(len(a)):
            if a[i] != a[-1]:
                bagian_basis = basis + a[i]
             
                
                for j in range(1, len(a)):
                    try:
                        bagian_eksponen = bagian_eksponen*(10**(math.floor(math.log10(a[i+j])+1)))
                    except ValueError:
                        bagian_eksponen = bagian_eksponen*(10**1)
                    except IndexError:
                        continue
                
                con_num = con_num + bagian_basis*bagian_eksponen
                bagian_eksponen = 1
                
            else:
                con_num = con_num + a[-1]
                
        return con_num
        
    else:
        return "Error: Mohon masukkan list"
        
