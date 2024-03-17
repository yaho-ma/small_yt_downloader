from pytube import YouTube
import os

link = 'https://www.youtube.com/watch?v=NYu1YWYNG9E'

#creating the obj
try:
    youtube_object = YouTube(link)
    print(youtube_object)
    pass
except Exception as error:
    print (f'error: {error}')
    pass

video_title = youtube_object.title
video_thumbnail = youtube_object.thumbnail_url
video_streams = youtube_object.streams
progressive_streams = video_streams.filter(progressive=True)

str = "hello!"


current_folder = os. getcwd() # a current folder

try:
    my_stream = youtube_object.streams.get_by_resolution(progressive_streams)
    my_stream.download(
        output_path=current_folder,
        
    )
    print(f'SUCCESS! the video has been downloaded successfully {current_folder}')
except Exception as error:
    print(f'error while donloading the video {error}')
    pass




# print(video_title, )
# print( video_thumbnail )
#print(f'PROGRESSIVE     video_streams: {progressive_streams}')
# print(path_to_save_video)


#print(video_streams.filter(file_extension='mp4'))


