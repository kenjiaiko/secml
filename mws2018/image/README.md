This is a sample code to extract common features from 2d-array-data (like image). In this sample, common feature is '漢', sample4.jpg don't have it. detect_test1.py extracts the common features '漢' from all images, using (AKAZE)[http://www.bmva.org/bmvc/2013/Papers/paper0013/paper0013.pdf].
```
# python detect_test1.py 2/
12 sample1.jpg
35 sample2.jpg
15 sample3.jpg
5 sample4.jpg
43 sample5.jpg
--
12 sample1.jpg
35 sample2.jpg
15 sample3.jpg
2 sample4.jpg
43 sample5.jpg
# python detect_test1.py 3/
15 sample1.jpg
30 sample2.jpg
12 sample3.jpg
7 sample4.jpg
30 sample5.jpg
--
15 sample1.jpg
30 sample2.jpg
12 sample3.jpg
0 sample4.jpg
30 sample5.jpg
# python detect_test1.py 1/
2 sample1.jpg
21 sample2.jpg
3 sample3.jpg
1 sample4.jpg
29 sample5.jpg
--
2 sample1.jpg
21 sample2.jpg
3 sample3.jpg
1 sample4.jpg
29 sample5.jpg
```
