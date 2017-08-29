import sys

reload(sys)
sys.setdefaultencoding('utf8')

abstracts_file_name = "chemprot_sample/chemprot_sample_abstracts.tsv"
entities_file_name = "chemprot_sample/chemprot_sample_entities.tsv"
sentences_file_name = "chemprot_sample/chemprot_sentences.tsv"

def load_data():
    f_abstracts = open(abstracts_file_name)
    abstracts = {}
    for line in f_abstracts:
        line_parts = line.split("\t")
        abstract = {}
        text = line_parts[1]
        for i in range(2, len(line_parts)):
            text += " " + line_parts[i]
        abstract['text'] = text
        abstracts[line_parts[0]] = abstract
    f_entities = open(entities_file_name)
    for line in f_entities:
        line_parts = line.split("\t")
        abstract = abstracts[line_parts[0]]
        if 'entities' not in abstract:
            abstract['entities'] = []
        entity = {}
        entity['id'] = line_parts[1]
        entity['type'] = line_parts[2]
        entity['begin'] = line_parts[3]
        entity['end'] = line_parts[4]
        entity['text'] = line_parts[5].strip()
        abstract['entities'].append(entity)
        abstracts[line_parts[0]] = abstract
    f_sentences = open(sentences_file_name)
    for line in f_sentences:
        line_parts = line.split("\t")
        abstract = abstracts[line_parts[0]]
        if 'sentences' not in abstract:
            abstract['sentences'] = []
        sentence = {}
        sentence['text'] = line_parts[1]
        sentence['begin'] = line_parts[2]
        sentence['end'] = line_parts[3].strip()
        abstract['sentences'].append(sentence)
        abstracts[line_parts[0]] = abstract
    print len(abstracts.keys())

load_data()
