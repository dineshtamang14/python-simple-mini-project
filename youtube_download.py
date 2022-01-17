from pytube import YouTube


link = input("Paste a link of Video to download: ")
print("Downloading....")

YouTube(link).streams.first().download()
print("Video Downloaded Successfully!")
