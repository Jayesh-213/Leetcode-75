class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        write =0
        read =0 
        while read < n:
            ch = chars[read]
            count =0
            while read < n and chars[read] == ch:
                count +=1
                read +=1
            chars[write] = ch
            write +=1

            if count > 1:
                 for digits in str(count):
                    chars[write] = digits
                    write +=1
        return write

        
