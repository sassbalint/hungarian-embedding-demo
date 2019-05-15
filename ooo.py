# coding: utf-8

from gensim.models import KeyedVectors
# key = one side of the mapping (i.e. word)
# the other side of the mapping is the vector

#import logging
#logging.basicConfig(level=logging.INFO, format='%(levelname)-8s [%(lineno)d] %(message)s')

model = KeyedVectors.load('data/glove-hu_152.gensim')

puzzles = [
  ['vacsora', 'gabona', 'reggeli', 'ebéd'],
  ['tengeri', 'ipari', 'technológiai', 'hősies'],
  ['fürdőszoba', 'szekrény', 'tetőtér', 'erkély', 'pálya', 'WC'],
  #['kék', 'piros', 'sárga', 'megcsinál'], # XXX ez miért 'sárga'?
  ['kék', 'piros', 'sárga', 'csinál'],
  ['zongorázik', 'hegedül', 'fuvolázik', 'főz']
]

# XXX jobb embeddinget csinálni
# XXX ragozott szavak vannak az embeddingben vagy lemmák?
# XXX mi történik az OOV szavakkal?

for p in puzzles:
  res = model.doesnt_match( p )
  print( res )

