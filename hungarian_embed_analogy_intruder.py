
# coding: utf-8

# In[1]:


from gensim.models import KeyedVectors

import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)-8s [%(lineno)d] %(message)s')


# In[2]:


model = KeyedVectors.load('data/glove-hu_152.gensim')
                                              


# # Hasonló

# In[3]:


model.most_similar('intelligens')


# Az `intelligens` helyére más szót beírva kiszámíthatod annak szomszédait a szemantikai térben, és hasonlóan ennek a jegyzetnek a későbbi celláiban.

# In[4]:


model.most_similar('Berlin')


# ## De néha csak kapcsolódó:

# In[5]:


model.most_similar('kerék', restrict_vocab=10000)


# # Analógia: Az _amerikai_hoz úgy viszonyul a _dollár_, mint az _angol_hoz a...

# In[6]:


model.most_similar(positive=['angol', 'dollár'], negative=['amerikai'])


# In[7]:


model.most_similar_cosmul(positive=['francia', 'London'], negative=['angol'])


# In[8]:


model.most_similar(positive=['kutya', 'ravasz'], negative=['róka'])


# In[9]:


model.most_similar(positive=['pók', 'fészek'], negative=['madár'])


# # Kakukktojás (_intruder, odd-man-out_)

# In[10]:


model.doesnt_match(['vacsora', 'gabona', 'reggeli', 'ebéd'])


# In[11]:


model.doesnt_match(["tengeri", "ipari", "technológiai", "hősies"])


# In[12]:


model.doesnt_match(["fürdőszoba", "szekrény", "tetőtér", "erkély", "pálya", "WC"])


# # Köszönetnyilvánítás és ,,olvass tovább"
# 
# * https://rare-technologies.com/word2vec-tutorial/#bonus_app
# * http://bionlp-www.utu.fi/wv_demo/
# * https://compositional-distributional-semantics.fandom.com/wiki/Word_intrusion_detection_task
