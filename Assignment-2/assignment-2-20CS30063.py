import sys
import re
import heapq

word_list = ["able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj", "affected", "affecting", "affects", "after", "afterwards", "again", "against", "ain", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "among", "amongst", "amoungst", "amount", "and", "announce", "another", "any", "anybody", "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "apparently", "appear", "appreciate", "appropriate", "approximately", "are", "aren", "arent", "arise", "around", "aside", "ask", "asking", "associated", "auth", "available", "away", "awfully", "back", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "bill", "biol", "both", "bottom", "brief", "briefly", "but", "call", "came", "can", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "cit", "clearly", "com", "come", "comes", "con", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn", "course", "cry", "currently", "date", "definitely", "describe", "described", "despite", "detail", "did", "didn", "different", "does", "doesn", "doing", "don", "done", "down", "downwards", "due", "during", "each", "edu", "effect", "eight", "eighty", "either", "eleven", "else", "elsewhere", "empty", "end", "ending", "enough", "entirely", "especially", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "exactly", "example", "except", "far", "few", "fifteen", "fifth", "fify", "fill", "find", "fire", "first", "five", "fix", "followed", "following", "follows", "for", "former", "formerly", "forth", "forty", "found", "four", "from", "front", "full", "further", "furthermore", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "goes", "going", "gone", "got", "gotten", "greetings", "had", "hadn", "happens", "hardly", "has", "hasn", "hasnt", "have", "haven", "having", "hed", "hello", "help", "hence", "her", "here", "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself", "hes", "hid", "him", "himself", "his", "hither", "home", "hopefully", "how", "howbeit", "however", "http", "hundred", "ibid", "ignored", "immediate", "immediately", "importance", "important", "inasmuch", "inc", "indeed", "index", "indicate", "indicated", "indicates", "information", "inner", "insofar", "instead", "interest", "into", "invention", "inward", "isn", "itd", "its", "itself", "just", "keep", "keeps", "kept", "know", "known", "knows", "largely", "last", "lately", "later", "latter", "latterly", "least", "les", "less", "lest", "let", "lets", "like", "liked", "likely", "line", "little", "look", "looking", "looks", "los", "ltd", "made", "mainly", "make", "makes", "many", "may", "maybe", "mean", "means", "meantime", "meanwhile", "merely", "might", "mightn", "mill", "million", "mine", "miss", "more", "moreover", "most", "mostly", "move", "mrs", "much", "mug", "must", "mustn", "myself", "name", "namely", "nay", "near", "nearly", "necessarily", "necessary", "need", "needn", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "ninety", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing", "novel", "now", "nowhere", "obtain", "obtained", "obviously", "off", "often", "okay", "old", "omitted", "once", "one", "ones", "only", "onto", "ord", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "owing", "own", "page", "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past", "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "predominantly", "present", "presumably", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "que", "quickly", "quite", "ran", "rather", "readily", "really", "reasonably", "recent", "recently", "ref", "refs", "regarding", "regardless", "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "said", "same", "saw", "say", "saying", "says", "sec", "second", "secondly", "section", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "shan", "she", "shed", "shes", "should", "shouldn", "show", "showed", "shown", "showns", "shows", "side", "significant", "significantly", "similar", "similarly", "since", "sincere", "six", "sixty", "slightly", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub", "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "system", "take", "taken", "taking", "tell", "ten", "tends", "than", "thank", "thanks", "thanx", "that", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "thereof", "therere", "theres", "thereto", "thereupon", "these", "they", "theyd", "theyre", "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those", "thou", "though", "thoughh", "thousand", "three", "throug", "through", "throughout", "thru", "thus", "til", "tip", "together", "too", "took", "top", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twelve", "twenty", "twice", "two", "u201d", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "upon", "ups", "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually", "value", "various", "very", "via", "viz", "vol", "vols", "volumtype", "want", "wants", "was", "wasn", "wasnt", "way", "wed", "welcome", "well", "went", "were", "weren", "werent", "what", "whatever", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever", "whole", "whom", "whomever", "whos", "whose", "why", "widely", "will", "willing", "wish", "with", "within", "without", "won", "wonder", "wont", "words", "world", "would", "wouldn", "wouldnt", "www", "yes", "yet", "you", "youd", "your", "youre", "yours", "yourself", "yourselves", "zero"]


'''
We store the bigrams in dictionary as that keeps them sorted
When size goes over buffer size, we write the bigrams to disk
After writing all, merge the files on disk
Go through the merged file and print the top k bigrams
'''
if __name__ == "__main__":
    # Get the command line arguments
    if len(sys.argv) != 4:
        print("Usage: python assignment-2-20CS30063.py <data file> <buffer size> <value of k>")
        sys.exit(1)
    data_file = sys.argv[1]
    buffer_size = int(sys.argv[2])  # This is in MB, we will convert it to bytes
    buffer_size *= 1024 * 1024
    k = int(sys.argv[3])

    # Read the data file
    last_word = None
    file_count = 0
    bigrams = {}
    with open(data_file, "r") as f:
        for line in f:
            words = re.split(r'[^a-zA-Z0-9]+', line)    # Split the line into words using regex, ignoring non-alphanumeric characters
            for i in range(len(words)):
                words[i] = words[i].lower()
                # If word does not contain at least 3 alphabets, ignore it
                count = 0
                for c in words[i]:
                    if c.isalpha():
                        count += 1
                if count < 3:
                    last_word = None
                    continue
                # If the word is in the stop words list, ignore it
                if words[i] in word_list:
                    last_word = None
                    continue
                # This is a valid word
                if last_word is not None:
                    bigram = (last_word, words[i])
                    if bigram in bigrams:
                        bigrams[bigram] += 1
                    else:
                        bigrams[bigram] = 1
                last_word = words[i]
            # If the buffer is full, sort and write to disk
            if(sys.getsizeof(bigrams) > buffer_size):
                bigrams = sorted(bigrams.items(), key=lambda x: x[0])
                with open(f"temp_{file_count}.txt", "w") as f:
                    for bigram in bigrams:
                        f.write(f"{bigram[0][0]} {bigram[0][1]} {bigram[1]}\n")
                file_count += 1
                bigrams = {}
    # Sort and write the remaining bigrams to disk
    if len(bigrams) > 0:
        bigrams = sorted(bigrams.items(), key=lambda x: x[0])
        with open(f"temp_{file_count}.txt", "w") as f:
            for bigram in bigrams:
                f.write(f"{bigram[0][0]} {bigram[0][1]} {bigram[1]}\n")
        file_count += 1

    # Merge the files and get the output
    with open('output.txt', 'w') as out:
        files = [open(f"temp_{i}.txt", 'r') for i in range(file_count)]
        heap = []
        for i, file in enumerate(files):
            line = file.readline()
            if line:
                key = (line.split()[0], line.split()[1])
                value = int(line.split()[2])
                heapq.heappush(heap, (key, value, i))
        while heap:
            key, value, i = heapq.heappop(heap)
            out.write(f"{key[0]} {key[1]} {value}\n")
            line = files[i].readline()
            if line:
                key = (line.split()[0], line.split()[1])
                value = int(line.split()[2])
                heapq.heappush(heap, (key, value, i))
        for file in files:
            file.close()

    # The bigrams are now written to output.txt, and they are sorted
    # But the reduce step is not done, so we need to combine them at the time of printing
    # We will use a heap to get the top k bigrams
    heap = []
    with open('output.txt', 'r') as f:
        last_key = None
        last_value = 0
        for line in f:
            key = (line.split()[0], line.split()[1])
            value = int(line.split()[2])
            if last_key is not None and last_key != key:
                heapq.heappush(heap, (last_value, last_key))
                last_value = value
                last_key = key
                if len(heap) > k:
                    heapq.heappop(heap)
            else:
                last_value += value
                last_key = key
    # Print the top k bigrams
    heap = sorted(heap, reverse=True)
    for i in range(k):
        if len(heap) == 0:
            break
        print(heap[i][1][0], heap[i][1][1])



    