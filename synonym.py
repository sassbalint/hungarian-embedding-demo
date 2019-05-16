# coding: utf-8

from gensim.models import KeyedVectors

model = KeyedVectors.load('data/glove-hu_152.gensim')

words = [
  'intelligens',
  'Berlin',
  'kerék',
  'pofátlan',
  'szemtelen',
  'azt',
  'megragaszjuk' # nincs benne XXX
]

for w in words:
  print( " *** {}".format( w ) )
  res = model.most_similar( w, topn=10 )
  #res = model.most_similar( w, topn=20 )
  #res = model.most_similar( w, restrict_vocab=10000 )
  for sy, fq in res:
    print( "{0}\t{1:5.2f}".format( sy, fq ) )
  print()

