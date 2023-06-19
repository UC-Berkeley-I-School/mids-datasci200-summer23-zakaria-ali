from wordscore import score_word

def run_scrabble(rack):

    valid_chars = "abcdefghijklmnopqrstuvwxyz*?"

    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]

        # Error handling for incorrect length rack
        if len(rack) < 2 or len(rack) > 7:
            return "You must input a minimum of 2 characters and a maximum of 7 characters."

        # Error handling for invalid characters
        for char in rack:
            if char not in valid_chars:
                return "You input an invalid character. Only a-z, *, and ? are allowed."

        # Error handling for incorrect
        if len(rack.replace('*', '').strip('?')) > 2:
            return "You have too many wildcard characters."