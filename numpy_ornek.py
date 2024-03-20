import numpy as np
dizi=np.array((3,4,5,6,7,8,9,10,11,12,13))

#np.random.random(-2,2,15) //rastgele matris yazar
#np.arange(1,7)  //aralık yazar
#np.where(arr%2==0)  //arama yapar
#arr.ndim //dizi bouyutunu öğrenme
#arr.reshape(9,3)  //matrisi şekillendirme  //devamı daha sonra yazılacak.


print(np.where(dizi%2==1))
