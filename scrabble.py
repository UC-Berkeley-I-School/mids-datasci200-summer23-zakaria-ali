from wordscore import score_word

def run_scrabble(rack):

    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]

        # Error handling for empty rack
        if len(rack) == 0:
            return "You must input a minimum of 2 characters"

        # Error handling for invalid character
        if not rack.isalpha() or '*' in rack or '?' in rack:
            return "You input an invalid character. Only a-z, *, and ? are allowed."