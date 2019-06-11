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

ERR_MIN_THREE_TRUE = 'Please, give at least three (frequent) words separated by commas. :)'

@app.route( '/<string:s>', methods = ['GET','POST'] )
@cross_origin()
def solve_( s ):
  """
  Solves an 'odd one out' puzzle using a word embedding.
  :param s: words delimited by comma.
  :returns: the word which is the 'odd one out'.
  """
  words = list( map( str.strip, s.split( "," ) ) )

  msg = [] # message
  ooo = "" # odd-one-out word (result)

  true_words = []
  oov_words = []

  # XXX filter()-rel esetleg lehetne vhogy? :)
  for w in words:
    if w in model:
      true_words.append( w )
    else:
      oov_words.append( w )

  if oov_words:
    msg.append ( 'Omitted non-frequent words: ' + ', '.join(oov_words) + '.' )

  if len(true_words) < 3:
    msg.append ( ERR_MIN_THREE_TRUE )
  else:
    ooo = model.doesnt_match( true_words )

  res = (
    '<html><head><title>odd one out by embedding</title></head><body><div style="width: 320px">' +
    ', '.join( words ) + '<br/>' +
    ( ( ', '.join( true_words ) + '<br/>' ) if words != true_words else "" ) + 
    '<i>' + '<br/>'.join( msg ) + '</i>' +
    ( ( '<br/><br/><b style="font-size: 200%">&rarr; ' + ooo + '</b>' ) if ooo else '' ) +
    '</div></body></html>'
  )

  return( res )

@app.route( '/', methods = ['GET','POST'] )
@cross_origin()
def no_param():
  return ERR_MIN_THREE_TRUE

# from github/danni/linux-conf-au-flask-tute...
if __name__ == '__main__':
  app.run( debug=True )

# run this for development (!) by:
# export FLASK_APP=kkkt.py ; export FLASK_ENV=development ; flask run

