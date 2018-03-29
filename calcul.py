class Triangle(object):
    def __init__(self, *args):
        super(Triangle, self).__init__(*args))
        
def findmatch(n):
    """Find the bell numbers in the Stirling triangle of the second kind.
    
    Arguments:
        n {int} -- The top range of the Bell number B_n.
    
    Returns:
        list -- list of matchs.
    """

    res=[]
    for i in range(2,n):
        bell=bell_number(i)
        for u in range(n):
            for w in range(u+1):
                if (stirling_number2(u,w)==bell):
                    res.append([i,u,w])
    return res
