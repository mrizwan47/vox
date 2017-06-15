import os, pygame
from gtts import gTTS

class vox:
	"""Voice of Saira. Vox is a latin word that means Voice or related to voice."""

	def __init__( self, text, lang='en' ):

		self.text			=	text
		self.voice_cache	=	"cache/voices/"
		self.voice_fname	=	"cache/voices/" + text + ".mp3"
		self.lang			=	'en'

		if not os.path.exists( self.voice_cache ):
			os.makedirs( self.voice_cache )

	def say( self ):

		if not self.voice_exists():
			self.generate_voice_cache()

		self.play()


	def generate_voice_cache( self ):
		tts = gTTS(text=self.text, lang=self.lang)
		tts.save( self.voice_fname )


	def play( self ):

		pygame.mixer.init()
		pygame.mixer.music.load( self.voice_fname )
		pygame.mixer.music.play()

		while( pygame.mixer.music.get_busy() ):
			continue

	def voice_exists( self ):

		return os.path.isfile( self.voice_fname )

def say( text, lang="en" ):

	gg		=	vox( text, lang )
	gg.say()
