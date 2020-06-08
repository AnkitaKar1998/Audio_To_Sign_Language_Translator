from nltk.parse.corenlp import CoreNLPServer
import os

java_path = "C:/Program Files/Java/jdk1.8.0_241/bin/java.exe"
os.environ['JAVAHOME'] = java_path

STANFORD = os.path.join("models", "stanford-corenlp-full-2018-10-05")

server = CoreNLPServer(
   os.path.join(STANFORD, "stanford-corenlp-3.9.2.jar"),
   os.path.join(STANFORD, "stanford-corenlp-3.9.2-models.jar"),
)

server.start()