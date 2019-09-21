# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Akhmadjon Kurbanov
# Collaborators: Sarah Spitz
# Time: 7.5

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title.lower()      # dealing with lower case
        self.description = description.lower() 
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
        
    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
        # validating phrase which is getting passed 
        for char in self.phrase:
            assert char not in string.punctuation, "Invalid phrase: there is puctuation in the phrase"
        
        phrase_splitted = self.phrase.split()
        number_of_word = len(phrase_splitted)
        number_of_spaces = self.phrase.count(' ')

        if number_of_word - number_of_spaces != 1:
            assert True, "Invalid phrase: phrase had wrong amount of white spaces"
    
    # checking if the phrase in text (title, descr.)
    def is_phrase_in(self, text):
        text = text.lower()
        for char in string.punctuation:
            text = text.replace(char, ' ')

        phrase_list = self.phrase.split()
        text_list = text.split() # creating a list with words from text snippet

        for word_in_text in text_list:
            for word_in_phrase in phrase_list:
                if word_in_text == word_in_phrase:
                    if len(phrase_list) == 1: return True
                    phrase_list.remove(word_in_phrase)
                    break
                else:
                    phrase_list = self.phrase.split()
                    break
        return False

# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, NewsStory):
        title = NewsStory.get_title()
        return self.is_phrase_in(title)

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, NewsStory):
            description = NewsStory.get_description()
            return self.is_phrase_in(description)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime.strptime(time, '%d %b %Y %H:%M:%S')
        self.time = self.time.replace(tzinfo=pytz.timezone("EST"))

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, NewsStory):
        self.pubdate = NewsStory.get_pubdate()
        self.pubdate = self.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return  self.pubdate < self.time

class AfterTrigger(TimeTrigger):
    def evaluate(self, NewsStory):
        self.pubdate = NewsStory.get_pubdate()
        self.pubdate = self.pubdate.replace(tzinfo=pytz.timezone("EST"))
        return self.pubdate > self.time

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, NewsStory):
        return not self.trigger.evaluate(NewsStory)    

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, NewsStory):
        return self.trigger1.evaluate(NewsStory) and self.trigger2.evaluate(NewsStory)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    
    def evaluate(self, NewsStory):
        return self.trigger1.evaluate(NewsStory) or self.trigger2.evaluate(NewsStory)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    tr_stories_list = []

    for story in stories: 
        for trigger in triggerlist:
            if trigger.evaluate(story): 
                tr_stories_list.append(story)
           
    return tr_stories_list


#======================
# User-Specified Triggers
#======================

# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    triggers_dict = {}
    triggers_list = []
    
    for line in lines:
        line_list = line.split(',')

        if line_list[0] != 'ADD':
            if len(line_list) == 3:
                trigger_name = line_list[0]
                trigger_type = line_list[1]
                trigger_parameter = line_list[2]

                if (trigger_type == 'TITLE'):
                    triggers_dict[trigger_name] = TitleTrigger(trigger_parameter)

                if (trigger_type == 'DESCRIPTION'):
                    triggers_dict[trigger_name] = DescriptionTrigger(trigger_parameter)
                
                if (trigger_type == 'AFTER'):
                    triggers_dict[trigger_name] = AfterTrigger(trigger_parameter)
                
                if (trigger_type == 'BEFORE'):
                    triggers_dict[trigger_name] = BeforeTrigger(trigger_parameter)

                if (trigger_type == 'NOT'):
                    triggers_dict[trigger_name] = NotTrigger(trigger_parameter)
            
            if len(line_list) == 4:
                trigger_name = line_list[0]
                trigger_type = line_list[1]
                trigger_name_parameter1 = line_list[2]
                trigger_name_parameter2 = line_list[3]

                trigger_parameter1 = triggers_dict.get(trigger_name_parameter1)
                trigger_parameter2 = triggers_dict.get(trigger_name_parameter2)

                if (trigger_type == 'OR'):
                    triggers_dict[trigger_name] = OrTrigger(trigger_parameter1, trigger_parameter2)

                if (trigger_type == 'AND'):
                    triggers_dict[trigger_name] = AndTrigger(trigger_parameter1, trigger_parameter2)
        
        else:
            for trigger_name in line_list:
                if trigger_name!= 'ADD':
                    triggers_list.append(triggers_dict.get(trigger_name))

    return triggers_list
        

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()