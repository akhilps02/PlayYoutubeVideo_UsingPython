import vlc
import pafy

url = "https://www.youtube.com/watch?v=RguA0jevrAc&list=RDMMRguA0jevrAc&start_radio=1"

video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)
media.play()
