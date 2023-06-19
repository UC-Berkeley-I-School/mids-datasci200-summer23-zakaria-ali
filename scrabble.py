from wordscore import score_word

def run_scrabble(rack):
    '''This function takes an input string representing a scrabble rack
    of length 2-7 and returns a list of valid words that can be made.'''

    valid_chars = "abcdefghijklmnopqrstuvwxyz*?"
    valid_words = []

    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()
        data = [datum.strip('\n') for datum in raw_input]

        # Error handling for incorrect length rack
        if len(rack) < 2 or len(rack) > 7:
            return "You must input a minimum of 2 characters and a maximum of 7 characters."

        # Error handling for invalid characters
        for char in rack.lower():
            if char not in valid_chars:
                return "You input an invalid character. Only a-z, *, and ? are allowed."

        # Error handling for incorrect
        if rack.count('*') + rack.count('?') > 2:
            return "You have too many wildcard characters."

        for v_word in data:
            if len(rack) < len(v_word):
                continue
            word_possible = True
            rack_buffer = rack.upper()
            for char in v_word:
                if char in rack_buffer:
                    rack_buffer = rack_buffer.replace(char, '', 1)
                elif '*' in rack_buffer:
                    rack_buffer = rack_buffer.replace('*', '', 1)
                elif '?' in rack_buffer:
                    rack_buffer = rack_buffer.replace('?', '', 1)
                else:
                    word_possible = False
                    break
            if word_possible:
                valid_words.append((score_word(v_word), v_word))

        valid_words = sorted(valid_words, key=lambda x: (-x[0], x[1]))

        return (valid_words, len(valid_words))