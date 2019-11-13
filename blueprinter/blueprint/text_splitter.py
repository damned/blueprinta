class TextSplitter:
    def split(self, all_text):
        main_text = all_text.split('\n')[0]
        lines = main_text.split(' ')
        return lines