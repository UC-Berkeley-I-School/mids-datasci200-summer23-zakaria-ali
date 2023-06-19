from wordscore import score_word

def run_scrabble(rack):

    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]

        # Error handling
        if len(rack) == 0:
            return "You must input a minimum of 2 characters"