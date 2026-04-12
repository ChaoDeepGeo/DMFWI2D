###this is the patch function for tensor
import torch
import matplotlib.pyplot as plt
import numpy as np
import sys
def patch2dt(A,l1=8,l2=8,s1=4,s2=4,mode=1):
	"""
	patch2d: decompose the image into patches:
	
	INPUT
	D: input image
	l1: first patch size
	l2: second patch size
	s1: first shifting size
	s2: second shifting size
	mode: patching mode
	
	OUTPUT
	X: patches

	"""
	
	[n1,n2]=A.shape;
	
	if mode==1: 	#possible for other patching options
		
		tmp=np.mod(n1-l1,s1);
		if tmp!=0:
			#A=np.concatenate((A,np.zeros([s1-tmp,n2])),axis=0); 
			A=torch.cat((A,torch.zeros([s1-tmp,n2],dtype=A.dtype, device=A.device)),axis=0)
		tmp=np.mod(n2-l2,s2);
		if tmp!=0:
			#A=np.concatenate((A,np.zeros([A.shape[0],s2-tmp])),axis=1); 
			A=torch.cat((A,torch.zeros([A.shape[0],s2-tmp],dtype=A.dtype, device=A.device)),axis=1)
		
		[N1,N2]=A.shape;
		X=[]
		for i1 in range(0,N1-l1+1,s1):
			for i2 in range(0,N2-l2+1,s2):
						#tmp=np.reshape(A[i1:i1+l1,i2:i2+l2],(l1*l2,1),order='F');
						sub = A[i1:i1+l1, i2:i2+l2].T  
						tmp = sub.reshape(l1 * l2, 1) 
						X.append(tmp)
		#X = np.array(X)
		X = torch.stack(X, dim=0) 
	else:
		#not written yet
		pass;
	
	return X[:,:,0]
	
def patch2dt_inv(X,n1,n2,l1=8,l2=8,s1=4,s2=4,mode=1):
	"""
	patch2d_inv: insert patches into the image
	
	INPUT
	D: input patches (sample,patchsize)
	mode: patching mode
	l1: first patch size
	l2: second patch size
	s1: first shifting size
	s2: second shifting size
	
	OUTPUT
	X: patches

	"""

	if mode==1: 	#possible for other patching options

		tmp1=np.mod(n1-l1,s1);
		tmp2=np.mod(n2-l2,s2);
		if tmp1!=0 and tmp2!=0:
			#A=np.zeros([n1+s1-tmp1,n2+s2-tmp2]); 
			#mask=np.zeros([n1+s1-tmp1,n2+s2-tmp2]); 
			A=torch.zeros([n1+s1-tmp1,n2+s2-tmp2],dtype=X.dtype, device=X.device)
			mask=torch.zeros([n1+s1-tmp1,n2+s2-tmp2],dtype=X.dtype, device=X.device)

		if tmp1!=0 and tmp2==0:
			A=torch.zeros([n1+s1-tmp1,n2],dtype=X.dtype, device=X.device)
			mask=torch.zeros([n1+s1-tmp1,n2],dtype=X.dtype, device=X.device)

		if tmp1==0 and tmp2!=0:
			A=torch.zeros([n1,n2+s2-tmp2],dtype=X.dtype, device=X.device)
			mask=torch.zeros([n1,n2+s2-tmp2],dtype=X.dtype, device=X.device)


		if tmp1==0 and tmp2==0:
			A=torch.zeros([n1,n2],dtype=X.dtype, device=X.device)
			mask=torch.zeros([n1,n2],dtype=X.dtype, device=X.device)

		[N1,N2]=A.shape;
		id=-1;
		for i1 in range(0,N1-l1+1,s1):
			for i2 in range(0,N2-l2+1,s2):
				id=id+1;
				#A[i1:i1+l1,i2:i2+l2]=A[i1:i1+l1,i2:i2+l2]+np.reshape(X[id,:],[l1,l2],order='F');
				#mask[i1:i1+l1,i2:i2+l2]=mask[i1:i1+l1,i2:i2+l2]+np.ones([l1,l2]);
				patch = X[id, :].reshape(l2, l1).T
				A[i1:i1+l1, i2:i2+l2] += patch
				mask[i1:i1+l1, i2:i2+l2] += torch.ones((l1, l2), dtype=mask.dtype, device=X.device)
		A=(A/mask)
		A=A[0:n1,0:n2]
	else:
		#not written yet
		pass;
	return A
	

	

	
	
