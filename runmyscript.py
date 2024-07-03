import download_images

for i in range(5000,6000):
	url = "https://www.google.com/search?q=ai+images&oq=ai+images&aqs=chrome..69i57.1541j0j7&sourceid=chrome&ie=UTF-8" + str(i)
	path = "/Users/alex/Documents/PythonDownloadImg/IMG/ISS"
	download_images.main(url, path)