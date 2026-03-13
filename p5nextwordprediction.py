from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,LSTM,Dense
import numpy as np

corpus=["how are you","i am fine","how is day"]

tk=Tokenizer()
tk.fit_on_texts(corpus)
total_words=len(tk.word_index)+1

seqs=[]
for line in corpus:
    tok=tk.texts_to_sequences([line])[0]
    for i in range(1,len(tok)):
        seqs.append(tok[:i+1])

max_len=max(len(x) for x in seqs)
seqs=pad_sequences(seqs,maxlen=max_len,padding="pre")

X=seqs[:,:-1]
y=seqs[:,-1]

model=Sequential([
Embedding(total_words,10,input_length=max_len-1),
LSTM(100),
Dense(total_words,activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy",optimizer="adam")
model.fit(X,y,epochs=100)

def predict(text):
    tok=pad_sequences(tk.texts_to_sequences([text]),maxlen=max_len-1,padding="pre")
    pred=np.argmax(model.predict(tok))
    return list(tk.word_index.keys())[pred]

print(predict("how are"))