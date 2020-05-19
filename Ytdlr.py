pac=input('Do you have installed the colorama and cfonts??\ty/n\t')
pacins=input("Do you want the embedded pacages installed?\ty/n")
import subprocess
import importlib
import sys
def install(i):
  subprocess.call(['pip','install',i])
  #if you do not want packages installed 
if pac and pacins=='n':
	def prompt1(sel1):
		while sel1 not in range (0,len(form)):
			print("Enter valid index!!!!!\t")
			sel1=eval(input(f"enter the video format index:"))
		return sel1

	print("\t\t\t\t\t\\tYoutube downloader")
	install('pytube3')
	from pytube import YouTube
	yt=YouTube(input(f"Enter the URL ::\t"))
	print(f"Conforming the video title:{yt.title}")
	print(f"the foloowing ideo fromats are available: ")
	form=yt.streams.filter(file_extension='mp4').order_by('resolution')
	for i in form:
		print(f"{form.index(i)}"+"\t....\t"+f"{i}\n")
	sel=prompt1(eval(input("enter the index::\t")))
	option=str(form[sel]).split()
	print (f"you have selected the file:"+f"\n\t\t\t\t{option[2]}"+"\t******\t"+f"{option[3]}"+"\t******\t"+f"{option[4]}")
	video=yt.streams[sel]
	path=input('Enter the path::  \t')
	if path:
		try:	
			video.download(path)
			print('DOWNLOAD COMPLETE !!!'+"\t\t\t")
			print(f'file in path\t\t\t'+f'{path}')
		except Exception as e:
			print(f"failure due to:\t{e}")
			helf=input('Would you lie suggestions??\t y/n\t')
			if helf=='y':
				print("\t\t\t\t\tTry selecting other video resolutions\n\t\t\t\t\tCheck the path of the destination ")

	else:
		try:
			video.download()
			print('DOWNLOAD COMPLETE !!!'+"\n"+"File in default path")
		except Exception as e:
			print(f"failure due to:\t{e}")
			helf=input('Would you lie suggestions??\t y/n\t')
			if helf=='y':
				print("\t\t\t\t\t\tTry selecting other video resolutions\n\t\t\t\t\tCheck the path of the destination ")
else:
  #if you do not have package and want to install
	if pacins=='y' and pac=='n':
		for i in ['pytube3','pdm','colorama']:
			install(i)
 #if you do have package 
	from pytube import YouTube
	from colorama import Fore, Back, Style,init
	from cfonts import render, say
	output1 = render('YouTube', colors=['red', 'white'], align='center',size=[158,48],line_height=1)
	output2 = render('Downloader', colors=['red', 'white'], align='center',size=[158,48],line_height=1)
	compl = render('Download sucessful', colors=['green', 'yellow'], align='center',size=[168,50],line_height=1)
	failed = render('Download Failed', colors=['green', 'white'], align='center',size=[158,48],line_height=2)
	sad = render(':(', colors=['cyan'], align='center',size=[158,50],line_height=1)
	def prompt1(sel1):
			while sel1 not in range (0,len(form)):
				print(Fore.RED+"Enter valid index!!!!!\t"+Fore.RESET)
				sel1=eval(input(f"enter the video format index:"))
			return sel1
	print(output1+"\n"+output2)
	init()

	yt=YouTube(input(f"Enter the URL ::\t"))
	print(f"Conforming the video title:{yt.title}")
	print(f"the foloowing ideo fromats are available: ")
	form=yt.streams.filter(file_extension='mp4').order_by('resolution')
	for i in form:
		print(Fore.GREEN+Style.BRIGHT+f"{form.index(i)}"+"\t....\t"+Fore.WHITE+Style.RESET_ALL+f"{i}\n")
	sel=prompt1(eval(input("enter the index::\t")))
	option=str(form[sel]).split()
	print (f"you have selected the file:"+Back.RED+Fore.YELLOW+f"\n\t\t\t\t{option[2]}"+"\t******\t"+f"{option[3]}"+"\t******\t"+f"{option[4]}"+Fore.RESET+Back.RESET)
	video=yt.streams[sel]
	path=input('Enter the path::  \t')
	if path:
		try:	
			video.download(path)
			print(Fore.WHITE + Back.BLUE +'DOWNLOAD COMPLETE !!!'+Back.RESET+"\t\t\t"+Back.RESET)
			print(Fore.GREEN +Back.RESET+Style.RESET_ALL+f'file in path\t\t\t'+Fore.YELLOW+f'{path}'+Back.RESET)
			print(compl)
		except Exception as e:
			print(Fore.WHITE + Back.RED +f"failure due to:\t{e}"+Back.RESET)
			print(failed+"\n"+sad)
			helf=input('Would you lie suggestions??\t y/n\t')
			if helf=='y':
				print(Fore.YELLOW+"\t\t\t\t\tTry selecting other video resolutions\n\t\t\t\t\tCheck the path of the destination ")

	else:
		try:
			video.download()
			print(Fore.WHITE + Back.BLUE+'DOWNLOAD COMPLETE !!!'+Back.RESET+"\n"+"File in default path")
			print(compl)
			
		except Exception as e:
			print(Fore.WHITE + Back.RED +f"failure due to:\t{e}"+Back.RESET)
			print(failed+"\n"+sad)
			helf=input('Would you lie suggestions??\t y/n\t')
			if helf=='y':
				print(Fore.YELLOW+"\t\t\t\t\t\tTry selecting other video resolutions\n\t\t\t\t\tCheck the path of the destination ")





