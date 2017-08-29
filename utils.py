import nltk

abstracts_file_name = "chemprot_sample/chemprot_sample_abstracts.tsv"

import sys

reload(sys)
sys.setdefaultencoding('utf8')

def sentence_split():
    f_abstract = open(abstracts_file_name)
    out = open("chemprot_sample/chemprot_sentences.tsv", "w")
    for line in f_abstract:
        line_parts = line.split("\t")
        text = line_parts[1]
        for i in range (2,len(line_parts)):
            text += " " + line_parts[i]
        sentences_text = nltk.sent_tokenize(text)
        for sent in sentences_text:
            out.write(line_parts[0] + "\t" + sent + "\t" + str(text.index(sent)) + "\t" + str(text.index(sent) + len(sent)) + "\n")
sentence_split()