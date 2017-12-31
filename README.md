# Introduction

_youtube-batch_ is a command line Python script that uploads all videos (e.g.: batch upload) in the given folders to Youtube (it should work on any platform -GNU/Linux, BSD, OS X, Windows, ...- that runs Python) using the Python script on GitHub [tokland/youtube-upload](https://github.com/tokland/youtube-upload) which uses the Youtube [APIv3](https://developers.google.com/youtube/v3/).

# Dependencies

* [Python 2.6/2.7/3.x](http://www.python.org).
* [GitHub:tokland/youtube-upload](https://github.com/tokland/youtube-upload)
* Packages: [google-api-python-client](https://developers.google.com/api-client-library/python), [progressbar2](https://pypi.python.org/pypi/progressbar2) (optional).

Check if your operating system provides those packages and you dont want to use `easy_install` as shown the `Install` instructions below, otherwise install them with `pip`:

```
$ sudo pip install --upgrade google-api-python-client progressbar2
```

# Install

First you have to install the Python script [tokland/youtube-upload](https://github.com/tokland/youtube-upload).

```
$ easy_install https://github.com/tokland/youtube-upload/archive/master.zip
```

Or install it manually

```
$ wget https://github.com/tokland/youtube-upload/archive/master.zip
$ unzip master.zip
$ cd youtube-upload-master
$ sudo python setup.py install
```

Then install _youtube-batch_

```
$ easy_install https://github.com/tkersten09/youtube-batch/archive/master.zip
```

Or manually as above

```
$ wget https://github.com/tkersten09/youtube-batch/archive/master.zip
$ unzip master.zip
$ cd youtube-batch-master
$ sudo python setup.py install
```

# Authentication

You'll see that there is no email/password options. Instead, the Youtube API uses [OAuth 2.0](https://developers.google.com/accounts/docs/OAuth2) to authenticate the upload. The first time you try to upload a video, you will be asked to follow a URL in your browser to get an authentication token. If you have multiple channels for the logged in user, you will also be asked to pick which one you want to upload the videos to. You can use multiple credentials, just use the option `--credentials-file`. Also, check the [token expiration](https://developers.google.com/youtube/v3/) policies.

The package includes a default `client_secrets.json` file. If you plan to make a heavy use of the script, please [create and use your own OAuth 2.0 file](https://developers.google.com/youtube/registering_an_application), it's a free service. Steps:

* Go to the Google [console](https://console.developers.google.com/).
* _Create project_.
* Side menu: _APIs & auth_ -> _APIs_
* Top menu: _Enabled API(s)_: Enable all Youtube APIs.
* Side menu: _APIs & auth_ -> _Credentials_.
* _Create a Client ID_: Add credentials -> OAuth 2.0 Client ID -> Other -> Name: youtube-upload -> Create -> OK
* _Download JSON_: Under the section "OAuth 2.0 client IDs". Save the file to your local system.
* Use this JSON as your credentials file: `--client-secrets=CLIENT_SECRETS`

# Examples

* Upload a video:

```
$ youtube-batch --endings="mpg, mp4" "D:\Dateien\upload1" "D:\Dateien\upload2"
```

_Other extra medata available :_

```
--privacy (public | unlisted | private)  
--publish-at (YYYY-MM-DDThh:mm:ss.sZ)  
--location (latitude=VAL,longitude=VAL[,altitude=VAL])  
--thumbnail (string)  
```

* Upload a video using a browser GUI to authenticate:

```
$ youtube-upload --title="A.S. Mutter" --auth-browser anne_sophie_mutter.flv
```

* Use a HTTP proxy

Set environment variables _http_proxy_ and _https_proxy_:

```
$ export http_proxy=http://user:password@host:port
$ export https_proxy=$http_proxy
$ youtube-batch ....
```

# Notes for developers

* Check the [Youtube Data API](https://developers.google.com/youtube/v3/docs/).
* Some Youtube API [examples](https://github.com/youtube/api-samples/tree/master/python) provided by Google.

# Alternatives

* [youtube-upload](https://github.com/tokland/youtube-upload) Its the basis of this script and its uploads videos to Youtube but can not batch-upload all videos in given folders.

* [shoogle](https://github.com/tokland/shoogle) can send requests to any Google API service, so it can be used not only to upload videos, but also to perform any operation regarding the Youtube API.

* [youtubeuploader](https://github.com/porjo/youtubeuploader) uploads videos to Youtube from local disk or from the web. It also provides rate-limited uploads.

# More

* License: [GNU/GPLv3](http://www.gnu.org/licenses/gpl.html).
