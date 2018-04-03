# Detection automation method for data sets with Concept Drift and Scale-free natures
A data sets in security typified by malware and spam messages are constantly changing their nature according to time axis, so it is difficult to implement countermeasures permanently. In this paper, we focus on the Scale-free of a data set with the property of Concept-Drift and propose a method to detect while following automatically the change of data distribution.

<img src="pngs/time.png" width="480px">

First, I want to define some symbols. t is the current time, D(t) is the data-set on the current time. Da(t−n) is a data-set that can be used for learning, Db(t+m) is a data-set we want to detect. Da and Db has both "malignant" and "benign", are NOT labeled, but Da is [Scale-free](https://en.wikipedia.org/wiki/Scale-free_network). And these data-set is [Concept-Drift](https://en.wikipedia.org/wiki/Concept_drift), constantly changing. So we want to automatically detect a malignant in Db using Da.

## Quantitative data
I'll show an example of data-set Da. For example, it is an information of reported from some users regularly. You can not trust 100% reputation from users. Of course, many users accurately report malignant as a malignant, but not all users can judge it accurately. In some cases, many benignities may be included in there. Therefore, the first problem is to label it, which is to separate benign and malignant ones.

<img src="pngs/figure_6.png" width="160px"><img src="pngs/figure_9.png" width="160px">

They are scattered throughout but the malignant ones gather themselves in some place. We want to find "N blue circles" in right figure (N=3 in this example) basing from a model we get with a data-set similar to the left figure. The data inside the blue circles are a malignant, the data outside of it are benign. In short, given data-set (that is Scale-free) like the one on the left figure, we want to draw a blue circle (an arbitrary number) in the right figure.

```
$ python load_dataset0-1.py sample0.txt
$ python load_dataset0-2.py sample0.txt
$ python load_dataset1-1.py sample1.txt
$ python load_dataset1-2.py sample1.txt
$ python load_dataset1-3.py sample1.txt
$ python load_dataset2-1.py sample2.txt sample3.txt
$ python load_dataset2-2.py sample3.txt
$ python load_dataset2-3.py sample3.txt 3
$ python load_dataset2-4.py sample2.txt sample3.txt 3
$ python load_dataset3-1.py sample4.txt
```
<img src="pngs/figure_1.png" width="160px"><img src="pngs/figure_2.png" width="160px"><img src="pngs/figure_3.png" width="160px"><img src="pngs/figure_4.png" width="160px"><img src="pngs/figure_5.png" width="160px"><img src="pngs/figure_6.png" width="160px"><img src="pngs/figure_7.png" width="160px"><img src="pngs/figure_8.png" width="160px"><img src="pngs/figure_9.png" width="160px"><img src="pngs/figure_10.png" width="160px">

1. Delete scattered benign data (load_dataset2-1.py)
2. Count the number of clusters　
3. Set the number of clusters and find the center point of each clusters

This is automatable. Both Da and Db are Concept-Drift, but if you can label Da like this, you can use it to automatically detect some malignants in Db.

## Qualitative data
I also want to do same thing for qualitative data.
```
ECA__: "ECAEA", "ECAAD", "ECACA", "ECABB", "ECACA"
_BAB_: "FBABF", "ABABC", "DBABA"
Other: "ABCDE", "DDFEA", "BCDAA", "FFFED", "AAAAA", "EEEEE", "BBDBB"
```
This is a sample data-set. There are 5 questions, each with 6 patterns (A to F) answers. The problem is finding features that exist in as much (but not all) of the data as possible. In short, We want to find "ECA" and "BAB" from the sample data-set. If there is an algorithm that extracts the common parts of the 2 data, it is possible (refer to [qualitative_data1-1.py](https://github.com/kenjiaiko/secml/blob/master/qualitative_data1-1.py)).

## String
We want to know a common substring or subsequence of malignants, so we could use the [Longest common substring](https://en.wikipedia.org/wiki/Longest_common_substring_problem) or [Longest common subsequence](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) for it. We can use the substring as a feature if we extract longest common substring/subsequence in some strings. The message containing the LCS has a high possibility of malignancy (ex: [Suffix Tree Application 5 Longest common substring](https://www.geeksforgeeks.org/suffix-tree-application-5-longest-common-substring-2/)).

[Suffix trees](https://en.wikipedia.org/wiki/Suffix_tree) provide one of the first linear-time solutions for the Longest common substring problem. Likewise, using the Suffix tree, you can extract common (substring) features from messages. Please refer to [qualitative_data1-2.py](https://github.com/kenjiaiko/secml/blob/master/qualitative_data1-2.py).

Next, let's consider about common subsequence of messages. If the number of generic input columns is arbitrary, Longest common subsequence is [NP-Hard](https://en.wikipedia.org/wiki/NP-hardness). So ingenuity may be necessary depending on the amount of data. Below is a sample algorithm. Please refer to [qualitative_data1-3.py](https://github.com/kenjiaiko/secml/blob/master/qualitative_data1-3.py).
