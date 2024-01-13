import pprint
import os
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

client = OpenAI(
  api_key="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"
)

# test parameters (replace with user input later)
url = 'https://www.youtube.com/watch?v=NJZ5YNrXMpE&ab_channel=oliSUNvia'
#url = 'https://www.youtube.com/watch?v=h6fcK_fRYaI&ab_channel=Kurzgesagt%E2%80%93InaNutshell'
wordcount = 100

video_id = url.replace('https://www.youtube.com/watch?v=', '')
transcriptjson = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', "en-GB"])


# split transcript up into 10000-character chunks
def chunk_transcript(transcript, chunk_size=10000):
    chunks = [transcript[i:i+chunk_size] for i in range(0, len(transcript), chunk_size)]
    return chunks

#debug: pprint.pprint(transcriptjson)

# get transcript from youtube
def getTranscriptText(transcriptjson):
  transcript=''
  for item in transcriptjson:
      clip = item['text']
      transcript += f' {clip}' 

  return transcript

# get summary of transcript using openai (wordcount specified by user)
def getSummary(transcript_chunks, wordcount):
  summary = ""

  # commands for openai
  conversation=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "assistant", "content": f"Write a {wordcount} word summary of this video."}]
  
  # run it on every chunk of transcript
  for chunk in transcript_chunks:
      conversation.append({"role": "user", "content": chunk})
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=conversation
      )
      summary += f" {response.choices[0].message.content}"

      # Clear user input for the next chunk
      conversation = conversation[:-1]

  return summary

# keep on passing through ai until reaches specified wordcount
def getFinalsummary():
  transcriptText = getTranscriptText(transcriptjson)

  # every word has ~6.5 characters on average
  while len(transcriptText)>wordcount*6.5:
      transcript_chunks = chunk_transcript(transcriptText)  
      transcriptText = getSummary(transcript_chunks, wordcount)

  # output to user interface
  print(transcriptText)

#pprint.pprint(transcriptjson)
print(YouTubeTranscriptApi.list_transcripts(video_id))