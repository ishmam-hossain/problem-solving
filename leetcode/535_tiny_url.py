class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        print(longUrl)
        for c in longUrl:
            print(ord(c))

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """


# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.encode(url))
# codec.decode(codec.encode(url))



"""
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. 
There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
can be decoded to the original URL.

"""