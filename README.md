# Basis
<img src="pngs/time.png" width="480px">

First, I want to define some symbols. t is the current time, D(t) is the data-set on the current time. Da(t−n) is a data-set that can be used for learning, Db(t+m) is a data-set we want to detect. Da and Db has both "malignant" and "benign", are NOT labeled, but Da is [Scale-free](https://en.wikipedia.org/wiki/Scale-free_network). And these data-set is [Concept-Drift](https://en.wikipedia.org/wiki/Concept_drift), constantly changing. So we want to automatically detect a malignant in Db using Da.

I'll show an example of data-set Da. For example, it is an information of reported from some users regularly. You can not trust 100% reputation from users. Of course, many users accurately report malignant as a malignant, but not all users can judge it accurately. In some cases, many benignities may be included in there. Therefore, the first problem is to label it, which is to separate benign and malignant ones.

<img src="pngs/figure_6.png" width="160px"><img src="pngs/figure_9.png" width="160px">

In short, given data-set like the one on the left figure, we want to draw a blue circle (an arbitrary number) in the right figure. The circles are not necessarily three.

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
```
<img src="pngs/figure_1.png" width="160px"><img src="pngs/figure_2.png" width="160px"><img src="pngs/figure_3.png" width="160px"><img src="pngs/figure_4.png" width="160px"><img src="pngs/figure_5.png" width="160px"><img src="pngs/figure_6.png" width="160px"><img src="pngs/figure_7.png" width="160px"><img src="pngs/figure_8.png" width="160px"><img src="pngs/figure_9.png" width="160px">
