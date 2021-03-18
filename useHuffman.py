from HuffmanCoding import HuffmanCoding

# Path for Input File
path = "c:/Users/yusuf/Documents/Often/University Work/Year 1 2020-2021/Term 2/Data Structures and Algorithms/Compression/Tests/sample_alice_french.txt"

# Path for Compressed File
path2 = "c:/Users/yusuf/Documents/Often/University Work/Year 1 2020-2021/Term 2/Data Structures and Algorithms/Compression/Tests/sample_alice_french.bin"

h = HuffmanCoding(path)
h.compress()
h.decompress(path2)
