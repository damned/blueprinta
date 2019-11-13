class TextSplitter:
    def split(self, all_text):
        main_text = all_text.split('\n')[0]
        lines = self.split_after_minimum(main_text)
        return lines

    def split_after_minimum(self, text, minimum=6):
        lines = []
        word = ''
        for c in text:
            if c == ' ':
                if len(word) >= minimum:
                    lines.append(word)
                    word = ''
                else:
                    word += c
            else:
                word += c

        if len(word) > 0:
            lines.append(word)

        return lines
