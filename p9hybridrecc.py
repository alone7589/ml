import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

posts=pd.DataFrame({
'id':[1,2,3],
'content':["AI healthcare","stock market","deep learning"]
})

interactions=pd.DataFrame({
'user':[1,1,2],
'post':[1,3,2]
})

tfidf=TfidfVectorizer()
sim=cosine_similarity(tfidf.fit_transform(posts["content"]))

def recommend(user):
 seen=interactions[interactions.user==user]["post"]
 scores=sim.sum(axis=0)

 posts["score"]=scores
 return posts[~posts.id.isin(seen)].sort_values("score",ascending=False)

print(recommend(1))