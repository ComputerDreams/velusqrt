from framework import *

if setting.style == 'wd1':
    # Using one torsion point and dummy isogeny constructions
    from csidh.gae_wd1 import *
    delta = 1
elif setting.style == 'wd2':
    # Using two torsion points and dummy isogeny constructions
    from csidh.gae_wd2 import *
    delta = 2
elif setting.style == 'df':
    # Dummy-free approach by using two torsion points
    from csidh.gae_df import *
    delta = 1
else:

    print("  ,-~~-.___.          ")
    print(" / |  '     \\          SYNTAX ERROR ..., run python3 main.py -h for help") 
    print("(  )         0        ")  
    print(" \_/-, ,----'         ")         
    print("    ====           // ")
    print("   /  \-'~;    /~~~(O)")
    print("  /  __/~|   /       |")   
    print("=(  _____| (_________|")
    exit(7)

''' -------------------------------------------------------------------------------------
    Number of degree-(l_i) isogeny constructions to be performed: m_i
    ------------------------------------------------------------------------------------- '''

# ==========================================================================

if( setting.prime == 'p512' ):                                                                                                                                                                                                                
                                                                                                                                                                                                                                            
    if(setting.style == 'wd1'):                                                                                                                                                                                                                      
        # ====== [MCR style, CSIDH-512] each m_i corresponds with the given in MCR18                                                                                                                                                        
        #m = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5]                                                                                                                                                                                               
                                                                                                                                                                                                                                            
        # ===== Suitable bounds for this work                                                                                                                                                                                               
        m = [15, 18, 20, 21, 21, 22, 22, 22, 22, 22, 22, 19, 20, 22, 23, 23, 23, 23, 23, 23, 23, 21, 23, 20, 16, 16, 16, 15, 14, 12, 13, 12, 11, 11, 10, 10, 9, 9, 9, 8, 8, 8, 8, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]

        # ====== [MCR style, CSIDH-512] case when each m_i is equal to 10, and it implies a key space of (10 + 1)^74 ~ 2^256 ~ p^1/4
        #m = [10] * n
        
        #sigma, kappa = 1, 10 # when only one strategy is required; that is, m = (10, 10, ..., 10)
        sigma, kappa = 5, 11 # MCR & dummy-free [The given one in MCR18] CSIDH-512
    
    if(setting.style == 'wd2'):
        # ====== [OAYT style, CSIDH-512] each m_i corresponds with the given in OAYT19
        #m = [5, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 10, 10, 9, 9, 9, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1]

        # ===== Suitable bounds for this work
        m = [7, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 9, 11, 9, 8, 8, 8, 7, 7, 7, 7, 6, 6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]

        # ====== [OAYT style, CSIDH-512] case when each m_i is equal to 5, and it implies a key space of (2*5 + 1)^74 ~ 2^256 ~ p^1/4
        #m = [5] * n
        
        #sigma, kappa = 1, 5 # when only one strategy is required; that is, m = (5, 5, ..., 5)
        sigma, kappa = 3, 8 # OAYT [The given one in OAYT19] CSIDH-512
    
    if(setting.style == 'df'):
        # ====== [dummy-free style, CSIDH-512] each m_i corresponds with the given in MCR18 (it is the same as MCR style)
        #m = [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5]

        # ===== Suitable bounds for this work
        m = [15, 18, 20, 21, 21, 22, 22, 22, 22, 22, 22, 19, 20, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 19, 16, 16, 16, 15, 14, 12, 13, 12, 11, 11, 11, 9, 9, 9, 9, 8, 8, 8, 8, 7, 8, 6, 6, 6, 6, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3]

        # ====== [dummy-free style, CSIDH-512] case when each m_i is equal to 10, and it implies a key space of (10 + 1)^74 ~ 2^256 ~ p^1/4
        #m = [10] * n
        
        #sigma, kappa = 1, 10 # when only one strategy is required; that is, m = (10, 10, ..., 10)
        sigma, kappa = 5, 11 # MCR & dummy-free [The given one in MCR18] CSIDH-512

elif( setting.prime == 'p1024'):
    # Ths branch corresponds with the proposal CSIDH-1024 of https://csidh.isogeny.org/index.html
    # Simba parameters should be optimized(?)

    if(setting.style == 'wd1'):

        # ===== MCR style (key-space size is 4^130 = 2^260 >= 2^256)
        #m = [3] * n

        # ===== Suitable bounds for this work
        m = [4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

    if(setting.style == 'wd2'):

        # ===== OAYT style (using the proposal bounds given in https://csidh.isogeny.org/index.html)
        #m = [2] * n
        
        # ===== Suitable bounds for this work
        m = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 3, 5

    if(setting.style == 'df'):

        # ===== dummy-free style (key-space size is 4^130 = 2^260 >= 2^256)
        #m = [3] * n

        # ===== Suitable bounds for this work
        m = [4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

elif( setting.prime == 'p1792'):
    # Ths branch corresponds with the proposal CSIDH-1024 of https://csidh.isogeny.org/index.html
    # Simba parameters should be optimized(?)

    if(setting.style == 'wd1'):

        # ===== MCR style (key-space size is 3^207 > 2^256)
        #m = [2] * n

        # ===== Suitable bounds for this work
        m = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

    if(setting.style == 'wd2'):

        # ===== OAYT style (using the proposal bounds given in https://csidh.isogeny.org/index.html)
        m = [1] * n
        
        # ===== Suitable bounds for this work
        sigma, kappa = 3, 5

    if(setting.style == 'df'):

        # ===== dummy-free style (key-space size is 3^207 > 2^256)
        #m = [2] * n

        # ===== Suitable bounds for this work
        m = [3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sigma, kappa = 5, 4

else:
    print("[ERROR]\tMissing bound. To set the maximum number of isogeny constructions, and sigma and kappa from SIMBA method (to add they in ELSE statement in line 147 of file csidh.py)")
    exit(11)

# ==========================================================================

if len(set(m)) > 1:
    # Maximum number of degree-(l_i) isogeny constructions is m_i (different for each l_i)
    LABEL_m = 'different_bounds'
else:
    # Maximum number of degree-(l_i) isogeny constructions is m (the same for each l_i)
    LABEL_m = 'with_same_bounds'

if setting.verbose:
    verb = '-suitable'
else:
    verb = '-classical'

try:

    # List of Small Odd Primes, L := [l_0, ..., l_{n-1}]
    m_prime = [ geometric_serie(m[k], L[k]) for k in range(n) ]
    r_out, L_out, R_out = rounds(m_prime[::-1], n)
    for j in range(0, len(r_out), 1):

        R_out[j] = list([L[::-1][k] for k in R_out[j]])
        L_out[j] = list([L[::-1][k] for k in L_out[j]])

    f = open('./strategies/' + setting.algorithm + '-' + setting.prime  + '-' + setting.style + '-' + setting.formulaes + '-' + LABEL_m + verb)
    #print("// Strategies to be read from a file")
    S_out = []
    for i in range(0, len(r_out), 1):

        tmp = f.readline()
        tmp = [ int(b) for b in tmp.split() ]
        S_out.append(tmp)

    f.close()

except IOError:

    #print("// Strategies to be computed")
    C_out, L_out, R_out, S_out, r_out = strategy_block_cost(L[::-1], m[::-1])
    f = open('./strategies/' + setting.algorithm + '-' + setting.prime  + '-' + setting.style + '-' + setting.formulaes + '-' + LABEL_m + verb,'w')
    for i in range(0, len(r_out)):

        f.writelines(' '.join([ str(tmp) for tmp in S_out[i]]) + '\n')

    f.close()

# ---
k = 3   # Number of rows (format of the list)
# ---

print("#ifndef _STRATEGIES_H_")
print("#define _STRATEGIES_H_")
print("\n// Recall, this script assumes the C-code implementation has the list of Small Odd Primes stored such that l_0 > l_1 > ... > l_{n-1}\n")
for i in range(len(r_out)):
    print("// -----------------------------------------------------------------------------------------------------------------------------------");
    print("// Strategy number %d\n" % (i))
    L_string = "static uint8_t L%d[] " % (i)
    R_string = "static uint8_t W%d[] " % (i)
    S_string = "static uint8_t S%d[] " % (i)
    
    printl(L_string, [ L.index(l_i) for l_i in L_out[i]][::-1], len(L_out[i]) // k + 1)
    if(R_out[i] != []):
        printl(R_string, [ L.index(r_i) for r_i in R_out[i]][::-1], len(R_out[i]) // k + 1)
    else:
        print(R_string +  " = {};")
    if(S_out[i] != []):
        printl(S_string, S_out[i], len(S_out[i]) // k + 1)
    else:
        print(S_string +  " = {};")
    

print("\n")
print("// -----------------------------------------------------------------------------------------------------------------------------------");
print("// -----------------------------------------------------------------------------------------------------------------------------------");
print("#define NUMBER_OF_DIFFERENT_STRATEGIES  %d" % len(L_out))
print("")
L_string = "static uint8_t *L_STRATEGY[NUMBER_OF_DIFFERENT_STRATEGIES] = {\n\t"
R_string = "static uint8_t *W_STRATEGY[NUMBER_OF_DIFFERENT_STRATEGIES] = {\n\t"
S_string = "static uint8_t *S[NUMBER_OF_DIFFERENT_STRATEGIES] = {\n\t"

tmp_sizes = "static uint8_t NUMBER_OF_PRIMES[] = {\n\t"
tmp_round = "static uint8_t ROUNDS[] = {\n\t"

for i in range(len(L_out) - 1):

    L_string = L_string + "L%d, " % (i)
    R_string = R_string + "W%d, " % (i)
    S_string = S_string + "S%d, " % (i)

    tmp_sizes = tmp_sizes + "%3d," % (len(L_out[i]))
    tmp_round = tmp_round + "%3d," % (r_out[i])

L_string = L_string + "L%d\n\t};" % (len(L_out) - 1)
R_string = R_string + "W%d\n\t};" % (len(L_out) - 1)
S_string = S_string + "S%d\n\t};" % (len(L_out) - 1)

tmp_sizes = tmp_sizes + "%3d\n\t};" % (len(L_out[len(L_out) - 1]))
tmp_round = tmp_round + "%3d\n\t};" % (r_out[len(L_out) - 1])

print("// L_STRATEGY[i] determines the small odd primes l_i per each strategy")
print(L_string)
print("\n// W_STRATEGY[i] determines L \ L_STRATEGY[i]")
print(R_string)
print("\n// S_STRATEGY[i] determines the optimal strategy for L_STRATEGY[i]")
print(S_string)

print("\n// Number of primes for each strategy")
print(tmp_sizes)
print("")
print("// Number of rounds per each different strategy")
print(tmp_round)

print("")
print("// Maximum number of degree-(l_i) isogeny constructions")
printl("static uint8_t B[]", [ m[L[::-1].index(l)] for l in L ], n // k + 1)

STYLE_NAME = {'wd2':'OAYT-style', 'wd1':'MCR-style', 'df':'dummy-free-style'}[setting.style]
print("\n#endif /* required framework for the strategies to be used in CSIDH-%s using %s */" % (setting.prime[1:], STYLE_NAME) )

