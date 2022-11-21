from tkinter import *
from tkinter.filedialog import askopenfilename

from moviepy.editor import VideoFileClip

filetypes = (('Video files','*.mp4'),('All files', '*.*'))
    
# Aqui puedes cambiar downloads por la carpeta que quieras 
video=askopenfilename(initialdir=r'C:\Users\M\Downloads\cortavideo',title='Select Video',filetypes=filetypes)
clip=VideoFileClip(video)

print("Ruta del video: " + video)
print("---Escribe los segundos o minutos en los que empieza el corte y donde termina ejemplo 00:04---")
new = clip.subclip(t_start=(input()), t_end=(input()))
new.write_videofile(
# Exportar el video recortado con el mismo nombre y le agrega .mp4
f'{video}.mp4',
codec='libx264',
preset="ultrafast",
# En trhreads cambia el numero de hilos que tenga tu pc 
threads=16,
bitrate=None,
audio_codec=None,
temp_audiofile=None,
audio_fps=44100,
audio_nbytes=2)
print("--------Fin--------")




