package com.codecamp.yinda;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class LC535 {


    class Codec{
        Map<String, String> map = new HashMap<>();
        private static final String PREFIX = "http://tinyurl.com/";
        // Encodes a URL to a shortened URL.
        public String encode(String longUrl) {
            byte[] array = new byte[6]; // length is bounded by 6
            new Random().nextBytes(array);
            String generatedString = new String(array);
            while(map.containsKey(generatedString)){
                new Random().nextBytes(array);
                generatedString = new String(array);
            }
            if(!map.containsKey(generatedString)){
                map.put(generatedString, longUrl);
            }
            return PREFIX+generatedString;
        }

        // Decodes a shortened URL to its original URL.
        public String decode(String shortUrl) {
            shortUrl = shortUrl.replace(PREFIX, "");
            return map.get(shortUrl);

        }
    }
}
