# coding: utf-8

from flask import Flask
from flask_cors import CORS, cross_origin
from gensim.models import KeyedVectors
import os
import psycopg2
import sys

app = Flask( __name__ )
cors = CORS( app )
app.config['CORS_HEADERS'] = 'Content-Type'

model = KeyedVectors.load('data/glove-hu_152.gensim')

# ez itten a postgres csatlakozás :)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

puzzles = [
  ['vacsora', 'gabona', 'reggeli', 'ebéd'],
  ['tengeri', 'ipari', 'technológiai', 'hősies'],
  ['fürdőszoba', 'szekrény', 'tetőtér', 'erkély', 'pálya', 'WC'],
  ['kék', 'piros', 'sárga', 'csinál'],
  ['zongorázik', 'hegedül', 'fuvolázik', 'főz']
]

ERR_MIN_THREE_TRUE = 'Adjon meg legalább három (gyakori) szót, vesszővel elválasztva. :)'
#ERR_MIN_THREE_TRUE = 'Please, give at least three (frequent) words separated by commas. :)'
VERBOSE_COMMAND = 'verbose'
GETID_COMMAND = 'getid'

@app.route( '/<string:s>', methods = ['GET','POST'] )
@cross_origin()
def process( s ):
  """
  Solve an 'odd one out' puzzle using a word embedding.
  :param s: words delimited by comma.
  :returns: the word which is the 'odd one out'.
  """

  msg = [] # message

  words_set = set( map( str.strip, s.split( "," ) ) )

  VERBOSE = False
  if VERBOSE_COMMAND in words_set:
    VERBOSE = True
    words_set.remove( VERBOSE_COMMAND ) 
    msg.append( 'Szószátyár (' + VERBOSE_COMMAND + ') mód bekapcs.' )
  words = sorted( list( words_set ) ) # magyar szerini sorrend kellene! XXX

  GETID = None
  for w in words_set:
    if w.startswith( GETID_COMMAND ): # XXX regex+set: lehet egyszerűbben?
      GETID = w[len(GETID_COMMAND):]
      try:
        cur.execute( 'SELECT puzzle FROM ooo WHERE id = {0};'.format( GETID ) )
        words = cur.fetchone()[0].split( "," ) # XXX jó ez? elég ez?
          # [0] -- mert a(z 1 elemű) tuple első eleme kell :)
        # az összes többi megadott szót kukázzuk :)
        msg.append( 'Kakukktojás #{0}.'.format( GETID ) )
      except Exception as e:
        #msg.append( 'exc[{0}]'.format( str(e) ) ) # exception info!
        msg.append( '#{0} feladat nincsen.'.format( GETID ) )
        words = []
      break

  ooo = "" # odd-one-out word (result)

  true_words = []
  oov_words = []

  for w in words:
    if w in model:
      true_words.append( w )
    else:
      oov_words.append( w )

  if oov_words:
    msg.append( 'Kihagyott ritka szavak: ' + ', '.join(oov_words) )

  if len(true_words) < 3:
    msg.append ( ERR_MIN_THREE_TRUE )
  else:
    ooo = model.doesnt_match( true_words )

  # fölső háromszög :: j > i
  dists = ""
  if VERBOSE:
    for i, w1 in enumerate(true_words):
      for j, w2 in enumerate(true_words):
        if j > i:
          dists += ( '[' + w1 + '|' + w2 + ': ' + "{0:5.3f}".format( model.distance( w1, w2 ) ) + ']<br/>' )

  res = (
    '<html><head><title>kakukktojás szóbeágyazással</title></head><body><div style="width: 320px">' +
    ', '.join( true_words + list( map( lambda x: '<del>' + x + '</del>', oov_words ) ) ) + '<br/>' +
    '<i>' + '<br/>'.join( msg ) + '</i>' +
    ( ( '<br/><br/><b style="font-size: 200%">&rarr; ' + ooo + '</b>' ) if ooo else '' ) +
    '<br/>' + dists +
    '</div></body></html>'
  )

  return res

@app.route( '/', methods = ['GET','POST'] )
@cross_origin()
def no_param():
  return ERR_MIN_THREE_TRUE

# from github/danni/linux-conf-au-flask-tute...
if __name__ == '__main__':
  app.run( debug=True )

# run this for development (!) by:
# export FLASK_APP=kkkt.py ; export FLASK_ENV=development ; flask run

