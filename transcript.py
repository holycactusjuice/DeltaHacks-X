import pprint
import os
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

client = OpenAI(
    api_key="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"
  )

class Summarizer:
  # test parameters (replace with user input later)
  url = 'https://www.youtube.com/watch?v=NJZ5YNrXMpE&ab_channel=oliSUNvia'
  #url = 'https://www.youtube.com/watch?v=h6fcK_fRYaI&ab_channel=Kurzgesagt%E2%80%93InaNutshell'
  wordCount = 100
  startTime = 0
  endTime = 0


  # split transcript up into 10000-character chunks
  def chunk_transcript(transcript, chunk_size=10000):
      chunks = [transcript[i:i+chunk_size] for i in range(0, len(transcript), chunk_size)]
      return chunks

  #debug: pprint.pprint(transcriptjson)

  # get transcript from youtube
  def getTranscriptText(transcriptjson, startTime, endTime):
    transcript=''

    result = []

    for item in transcriptjson:
       if int(item['start']) in range(startTime, endTime):
          result.append(item)

    for item in result:
        clip = item['text']
        transcript += f' {clip}' 

    return transcript

  # get summary of transcript using openai (wordcount specified by user)
  @staticmethod
  def getSummary(transcript_chunks, wordCount):
    summary = ""

    # commands for openai
    conversation=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": f"Write a {wordCount} word summary of this video."}]
    
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
  
  @staticmethod
  def getEndtime(transcriptjson):
     return transcriptjson[-1]['start']

  # keep on passing through ai until reaches specified wordcount
  @staticmethod
  def getFinalsummary(url, wordCount, startTime=0, endTime=None):

    video_id = url.replace('https://www.youtube.com/watch?v=', '')
    transcriptjson = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', "en-GB"])

    if endTime == None:
      Summarizer.getEndtime(transcriptjson)

    transcriptText = Summarizer.getTranscriptText(transcriptjson, startTime, endTime)

    # every word has ~6.5 characters on average
    while len(transcriptText)>wordCount*6.5:
        transcript_chunks = Summarizer.chunk_transcript(transcriptText)  
        transcriptText = Summarizer.getSummary(transcript_chunks, wordCount)

    # output to user interface
    print(transcriptText)

    #pprint.pprint(transcriptjson)
    #print(YouTubeTranscriptApi.list_transcripts(video_id))

#print(len(YouTubeTranscriptApi.get_transcript("NJZ5YNrXMpE&ab_channel=oliSUNvia", languages=['en', "en-GB"])))
#print(Summarizer.getFinalsummary('https://www.youtube.com/watch?v=NJZ5YNrXMpE&ab_channel=oliSUNvia', 100, 1700, 3000))