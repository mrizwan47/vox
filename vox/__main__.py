import click, os, time
import vox.api as vox

@click.command()
@click.argument( 'text' )
@click.argument( 'language', required=False )

def main( text, language ):

	if language is None:
		language	=	'en'

	vox.say( text, language )

if __name__ == "__main__":
	main()
