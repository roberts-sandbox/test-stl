#!/usr/bin/python


#from flask import Flask
import flask
from flask_bootstrap import Bootstrap
#import markdown
import os
import re



def create_app():
  app = flask.Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()

@app.route( '/' )
def index():
	#html = markdown.markdown(your_text_string)
	retval = ""
	for d in os.listdir( "data/" ):
		retval += "<li>{}\n<ul>\n".format( d )
		portlist = os.listdir( "data/{}/".format( d ) )
		portlist.sort( key=int )
		for di in portlist:
			retval += "<li><a href='/view/{}/{}'>{}</a></li>\n".format( d, di, di )

		retval += "</ul></li>"
	#return 'Hello world'
	retval += "</ul>"
	return flask.render_template( "index.html", content=retval )

@app.route('/view/<proto>/<int:port>', methods=['GET'] )
def view( proto, port ):
	notes = ""

	if( os.path.isdir( "data/{}/{}".format( proto, port ) ) ):
		filename_notes = "data/{}/{}/notes".format( proto, port ) 
		if( os.path.exists( filename_notes ) ):
			notes = open( filename_notes, 'r' ).read().decode("utf-8").replace( "\n", "<br />" )
		else:
			notes = "{} doesn't exist".format( filename_notes )
				
	return flask.render_template( "view.html", proto=proto, port=port, notes=notes )


if __name__ == '__main__':
	app.run( debug=True )

	#("0.0.0.0", 0 ), 
