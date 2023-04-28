from urllib.request import urlopen
import ssl
release_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
ssl_context = ssl.SSLContext()
response = urlopen(release_url, context=ssl_context)
print(response.read().decode('utf-8').strip())


