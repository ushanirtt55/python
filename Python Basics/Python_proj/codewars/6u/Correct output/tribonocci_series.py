"""def tribonacci(signature,n):
        a1=[]
        if n==1:
            a=signature[0]
            a1.append(a)
            return a1
        if n==0:
            return []
        if n==2:
            return signature[:2]
        for i in range(n-len(signature),0,-1):
            sum=0
            a=[j for j in signature[::-1]]
            for i in a[:3]:
                sum=sum+i
            signature.append(sum)
        return signature  """
        
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

a=tribonacci([1,1,1],4)
print a

            