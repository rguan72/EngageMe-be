# EngageMe

Winner of 2nd place for Best Use of Google Cloud at MHacks 12!

Engage the audience better by pointing them to only interesting parts of a video.

## Motivation

Our group members noticed that it's often difficult to cut through the noise and get straight to the important parts of videos/lecture recordings. We figured it would be cool to crowdsource this information and direct users to the most interesting/important portions of the video in a seamless manner. We also wanted to do this in a platform agnostic manner.

## What it does:

Tracks viewer engagement and emphasizes the most interesting parts of the video to the user in the progress bar. Users can skip to the parts of the video other viewers found useful, professors can track which parts of their lecture recordings were watched by the largest proportion of users (so they can track which concepts students are struggling with), and video producers can track which parts of the video their viewers find most interesting.

## How it works:

The Chrome extension uses the HTML5 `<video>` tag, looking at when the user takes action to change the part of the video they are at. After the user is done watching this video, we push this information to the back end, which aggregates all user-tracked time data and determines which segments were viewed by at least 50% of the watchers. We then display this with a unique color onto the progress bar. Currently compatible with [Youtube](https://youtube.com) and [UMich's lecture recording website](https://leccap.engin.umich.edu/leccap), but will expand to several other platforms soon!

## API Spec

Spec is published in [Postman](https://documenter.getpostman.com/view/7437194/SW18xFBm?version=latest)

## Quick Start

Add Google Cloud JSON credentials to the root of your repo and a `.env` file with environmental variable `GOOGLE_APPLICATION_CREDENTIALS` containing the path to that JSON file.

Then:

```bash
# Install Python Poetry if not already installed
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python


# install dependencies
$ poetry install

# enter shell
$ poetry shell

# start running application
$ flask run
```

Deploy (to be automated)

```bash
# update dependencies
$ poetry export -f requirements.txt > requirements.txt

# deploy
$ gcloud app beta deploy
```
