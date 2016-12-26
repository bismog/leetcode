import numpy as np

stack_width = 3
copy_length = 5

v_0 = np.zeros(stack_width)
v_0[0] = 1
v_1 = np.zeros(stack_width)
v_1[1] = 1
v_2 = np.zeros(stack_width)
v_2[2] = 1

# INIT
V = list() # stack states
s = list() # stack strengths 
d = list() # push strengths
u = list() # pop strengths

def r_t(t):
    r_t_out = np.zeros(stack_width)
    for i in xrange(0,t+1):
        temp = min(s[t][i],max(0,1 - sum(s[t][i+1:t+1])))
        r_t_out += temp * V[t][i]
    return r_t_out
    
def s_t(i,t,u,d):
    if(i >= 0 and i < t):
        inner_sum = s[t-1][i+1:t]
        return max(0,s[t-1][i] - max(0,u[t] - sum(inner_sum)))
    elif(i == t):
        return d[t]
    else:
        print "Undefined i -> t relationship"

def pushAndPop(v_t,d_t,u_t,t=len(V)):

  d.append(d_t)
  u.append(u_t)

  new_s = np.zeros(t+1)
  for i in xrange(t+1):
      new_s[i] = s_t(i,t,u,d)
  s.append(new_s)
  
  if(len(V) == 0):
      V_t = np.zeros((1,stack_width))
      V_t += v_t
  else:
      depth = len(V[-1])
      V_t = np.zeros((depth+1,stack_width))
      for i in xrange(depth):
        V_t[i] += V[-1][i]
      V_t[depth] += v_t
  
  V.append(V_t)
  return r_t(t)

print str(pushAndPop(v_0,0.8,0.0,0))
print str(pushAndPop(v_1,0.5,0.1,1))
print str(pushAndPop(v_2,0.9,0.9,2))

# Stack is empty again
V = list() # stack states
s = list() # stack strengths 
d = list() # push strengths
u = list() # pop strengths

assert str(pushAndPop(v_0,0.8,0.0,0)) == str((0.8 * v_0))
assert str(pushAndPop(v_1,0.5,0.1,1)) == str((0.5 * v_0) + (0.5 * v_1))
assert str(pushAndPop(v_2,0.9,0.9,2)) == str((0.9 * v_2) + (0 * v_1) + (0.1 * v_0))

print "\nFinal Value of S:"
for i in range(3):
  print s_t(2-i,2,u,d)

print "\nPassed All Assertions!!!"

