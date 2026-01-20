# Goal: Save a pithon object(class) to file.

import pickle
pickle.dump([1,2],open('o.pkl','wb'))
with open('o.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data)
