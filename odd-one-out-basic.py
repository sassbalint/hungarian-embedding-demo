# coding: utf-8

from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask( __name__ )
cors = CORS( app )
app.config['CORS_HEADERS'] = 'Content-Type'

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

ERR_MIN_THREE = "[Please, give at least three comma separated words.]"

@app.route( '/<string:s>', methods = ['GET','POST'] )
@cross_origin()
def solve_ooo( s ):
  """
  Solves an 'odd one out' puzzle using a word embedding.
  :param s: words delimited by comma.
  :returns: the word which is the 'odd one out'.
  """
  words = list( map( str.strip, s.split( "," ) ) )
  if len(words) < 3:
    return ERR_MIN_THREE
  return( model.doesnt_match( words ) )
  
@app.route( '/', methods = ['GET','POST'] )
@cross_origin()
def no_param():
  return ERR_MIN_THREE

# from github/danni/linux-conf-au-flask-tute...
if __name__ == '__main__':
  app.run( debug=True )

# run this for development (!) by:
# export FLASK_APP=kkkt.py ; export FLASK_ENV=development ; flask run

