"""
Authors:
Alena Zorich (elzorich@uni-koblenz.de)
Igor Maksimovich Fedotov (ifedotov@uni-koblenz.de)
Mariya Chkalova (mchkalova@uni-koblenz.de)
Arsenii Smyrnov (smyrnov@uni-koblenz.de)
"""

#!/usr/bin/env python3
from queue import Queue
from threading import Thread
from iter_corpus_docs import *

class Worker(Thread):
   def __init__(self, queue, queue_results):
       Thread.__init__(self)
       self.queue = queue
       self.queue_results = queue_results


   def process_content(self, title, content, keyword):
       for line in content.split('\n'):
           for word in line.split(' '):
               if (word.lower() == keyword.lower()):
                   self.queue_results.put((title))

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           title, content, keyword = self.queue.get()
           self.process_content(title, content, keyword)
           self.queue.task_done()



def naive_search(filename, keyword):
    """Find documents in a corpus that contain a keyword.

    The search is case-insensitive.

    Args:
        filename: Path to the corpus file.
        keyword: The keyword that returned documents should contain.

    Returns:
        A set of the titles of all documents that contained the word.
    """
    matched_titles = set()
    queue = Queue()
    queue_results = Queue()
    matched_titles = set()
    # Create 8 worker threads
    for x in range(8):
        worker = Worker(queue, queue_results)
            # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    if (keyword != ''):
        docs = iter_corpus_docs(filename)
        for doc in docs:
            queue.put((doc['title'], doc['content'], keyword))
        queue.join()
        while not queue_results.empty():
            matched_titles.add(queue_results.get())
    return matched_titles



if __name__ == '__main__':
    matches = naive_search('simplewiki-20160501-extracted-devel.xml', 'simple')
    for match in matches:
        print('-', match)
    print('({} matches found)'.format(len(matches)))
