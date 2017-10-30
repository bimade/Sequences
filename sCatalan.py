def sBinomial_number(n,k,s):
	l=Compositions(k,length=s,min_part=0)
	sum=0
	for e in l:
		prod= binomial(n,e[0])
		for i in range(1,s):
			prod=prod * binomial(e[i-1],e[i])
		sum=sum + prod
	return sum

def sBinomial_list(n,s):
	l=[0 for i in range((s*n)/2)]
	l.insert(0,1)
	k=0
	while k<n:
		for i in reversed(range((s*n)/2+1)):
			j=i-1
			sum=l[i]
			while (i-j<=s)&(j>=0):
				sum=sum+l[j]
				j=j-1
			l[i]=sum
		k=k+1
	return l

def sBinomial_number_2(n,k,s):
	l=sBinomial_list(n,s)
	k=min(k,n*s-k)
	return l[k]


def sCatalan_number(n,s):
	return( sBinomial_number(2*n,s*n,s)-sBinomial_number(2*n,s*n-1,s) )

def sCatalan_number_2(n,s):
	l=sBinomial_list(2*n,s)
	return (l[s*n]-l[s*n-1])

def sCatalan_prety(s,k):
	i=1
	l=[]
	com=0
	while com<k:
		if (sCatalan_number_2(i,s) % 2 == 1):
			l.append(i)
			com=com+1
		i=i+1
	return l

def sCatalan_prety_2(n,s):
	l=[0 for i in range((s*n))]
	res=[]
	l.insert(0,1)
	k=0
	while k<2*n:
		for i in reversed(range((s*n)+1)):
			j=i-1
			sum=l[i]
			while (i-j<=s)&(j>=0):
				sum=sum+l[j]
				j=j-1
			l[i]=sum
		if k%2==0:
			C=l[s*k/2]-l[s*(k/2)-1]
			if (C%2==1):
				res.append(k/2+1)
		k=k+1
	return res