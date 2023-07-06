import re


class TextProcessingService:
    @staticmethod
    def __lower(text: str) -> str:
        return text.lower()

    @staticmethod
    def __remove_extra_space(text: str) -> str:
        return re.sub(r"(\ {2,})", " ", text)

    @staticmethod
    def __strip_string(text: str) -> str:
        return text.strip()

    @staticmethod
    def __remove_mention(text: str) -> str:
        return re.sub(r"(@[\w|\d]*)", "", text)

    @staticmethod
    def __remove_url(text: str) -> str:
        regex = r"""((?:https?\:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
        return re.sub(regex, "", text)

    @staticmethod
    def __remove_non_alphanumeric_chars(text: str):
        pattens = re.compile(
            "["
            "\uac00-\ud7a3"  # Korean
            "\u3040-\u30ff"  # Japanese
            "\u4e00-\u9FFF"  # Chinese
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U00002500-\U00002BEF"  # chinese char
            "\U00002702-\U000027B0"
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "\U0001f926-\U0001f937"
            "\U00010000-\U0010ffff"
            "\u2640-\u2642"
            "\u2600-\u2B55"
            "\u200d"
            "\u23cf"
            "\u23e9"
            "\u231a"
            "\ufe0f"  # dingbats
            "\u3030"
            "]+",
            flags=re.UNICODE,
        )
        return re.sub(pattens, "", text)

    @staticmethod
    def run(text: str) -> str:
        text = TextProcessingService.__lower(text)
        text = TextProcessingService.__remove_mention(text)
        text = TextProcessingService.__remove_url(text)
        text = TextProcessingService.__remove_non_alphanumeric_chars(text)
        text = TextProcessingService.__remove_extra_space(text)
        text = TextProcessingService.__strip_string(text)

        return text
