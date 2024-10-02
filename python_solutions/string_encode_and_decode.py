class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        output = []
        while len(s) > 0:
            marker_index = s.index("#")
            string_length, s = int(s[:marker_index]), s[marker_index + 1:]
            a , s = s[:string_length], s[string_length:]
            output.append(a)
        return output  