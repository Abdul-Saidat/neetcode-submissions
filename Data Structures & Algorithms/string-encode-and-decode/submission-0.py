class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            length = len(st)
            encoded_str += str(length) + "-" + st

        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i != len(s):
            length_part = ""
            while s[i] != "-":
                length_part += s[i]
                i += 1

            length = int(length_part)

            i += 1
            string = s[i:i + length]
            result.append(string)
            i += length

        return result



